/* ─── Chat Panel ─────────────────────────────────────────────── */
const chatPanel    = document.getElementById("chatPanel");
const chatMessages = document.getElementById("chatMessages");
const chatInput    = document.getElementById("chatInput");
const chatSend     = document.getElementById("chatSend");
const chatEmpty    = document.getElementById("chatEmpty");

let chatHistory = [];  // in-memory only
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

  // Add streaming assistant bubble
  const assistantBubble = appendBubble("assistant", "");
  streaming = true;
  chatSend.disabled = true;

  // Show typing indicator temporarily
  const typingEl = document.createElement("div");
  typingEl.className = "chat-typing";
  typingEl.innerHTML = "<span></span><span></span><span></span>";
  chatMessages.appendChild(typingEl);
  scrollToBottom();

  const topicId = currentTopicId || "";
  const url = `/api/chat/stream?message=${encodeURIComponent(text)}&topic_id=${encodeURIComponent(topicId)}`;
  const es = new EventSource(url);

  es.onmessage = e => {
    if (e.data === "[DONE]") {
      es.close();
      typingEl.remove();
      streaming = false;
      chatSend.disabled = false;
      scrollToBottom();
      return;
    }
    try {
      const payload = JSON.parse(e.data);
      typingEl.remove();
      assistantBubble.textContent += payload.token || "";
      scrollToBottom();
    } catch {}
  };

  es.onerror = () => {
    es.close();
    typingEl.remove();
    streaming = false;
    chatSend.disabled = false;
    if (!assistantBubble.textContent) {
      assistantBubble.textContent = "⚠️ Could not connect to chat. Make sure Ollama is running.";
    }
    scrollToBottom();
  };
}

function appendBubble(role, text) {
  const div = document.createElement("div");
  div.className = `chat-msg ${role}`;
  div.textContent = text;
  chatMessages.appendChild(div);
  scrollToBottom();
  return div;
}

function scrollToBottom() {
  if (chatMessages) chatMessages.scrollTop = chatMessages.scrollHeight;
}
