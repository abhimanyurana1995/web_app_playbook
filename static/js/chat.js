/* ─── Chat Panel ─────────────────────────────────────────────── */
const chatPanel    = document.getElementById("chatPanel");
const chatMessages = document.getElementById("chatMessages");
const chatInput    = document.getElementById("chatInput");
const chatSend     = document.getElementById("chatSend");
const chatEmpty    = document.getElementById("chatEmpty");

let chatHistory = [];  // [{role: "user"|"assistant", content: "..."}]
let streaming   = false;

function openChat() {
  chatPanel?.classList.add("open");
}

function closeChat() {
  chatPanel?.classList.remove("open");
}

document.getElementById("chatFab")?.addEventListener("click", openChat);
document.getElementById("chatClose")?.addEventListener("click", closeChat);

// Suggestion pills click → send that text
document.querySelectorAll(".chat-suggestion").forEach(el => {
  el.addEventListener("click", () => {
    chatInput.value = el.textContent;
    sendMessage();
  });
});

chatInput?.addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

chatInput?.addEventListener("input", () => {
  chatInput.style.height = "auto";
  chatInput.style.height = Math.min(chatInput.scrollHeight, 120) + "px";
});

chatSend?.addEventListener("click", sendMessage);

async function sendMessage() {
  const text = chatInput?.value.trim();
  if (!text || streaming) return;

  chatInput.value = "";
  chatInput.style.height = "auto";

  // Hide empty state
  if (chatEmpty) chatEmpty.style.display = "none";

  // Add user bubble
  appendBubble("user", text);
  chatHistory.push({ role: "user", content: text });

  // Add streaming assistant bubble
  const assistantBubble = appendBubble("assistant", "");
  streaming = true;
  chatSend.disabled = true;

  // Typing indicator
  const typingEl = document.createElement("div");
  typingEl.className = "chat-typing";
  typingEl.innerHTML = "<span></span><span></span><span></span>";
  chatMessages.appendChild(typingEl);
  scrollToBottom();

  const topicId = currentTopicId || "";
  let fullResponse = "";

  try {
    const res = await fetch("/api/chat/stream", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: text,
        topic_id: topicId,
        history: chatHistory.slice(0, -1)   // all turns except the current user msg
      })
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const reader  = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer    = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split("\n");
      buffer = lines.pop();   // keep incomplete last line

      for (const line of lines) {
        if (!line.startsWith("data: ")) continue;
        const raw = line.slice(6);
        if (raw === "[DONE]") {
          if (typingEl.parentNode) typingEl.remove();
          chatHistory.push({ role: "assistant", content: fullResponse });
          streaming = false;
          chatSend.disabled = false;
          scrollToBottom();
          return;
        }
        try {
          const payload = JSON.parse(raw);
          if (typingEl.parentNode) typingEl.remove();
          fullResponse += payload.token || "";
          assistantBubble.innerHTML = marked.parse(fullResponse);
          scrollToBottom();
        } catch {}
      }
    }
  } catch (err) {
    if (!assistantBubble.textContent) {
      assistantBubble.textContent = "⚠️ Could not connect to chat. Make sure Ollama is running.";
    }
  } finally {
    if (typingEl.parentNode) typingEl.remove();
    streaming = false;
    chatSend.disabled = false;
    scrollToBottom();
  }
}

function appendBubble(role, text) {
  const div = document.createElement("div");
  div.className = `chat-msg ${role}`;
  if (role === "assistant" && text) {
    div.innerHTML = marked.parse(text);
  } else {
    div.textContent = text;
  }
  chatMessages.appendChild(div);
  scrollToBottom();
  return div;
}

function scrollToBottom() {
  if (chatMessages) chatMessages.scrollTop = chatMessages.scrollHeight;
}
