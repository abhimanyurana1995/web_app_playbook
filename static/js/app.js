/* ─── Tab switching ─────────────────────────────────────────── */
function showTab(tab) {
  document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
  document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
  document.querySelector(`.tab-btn[data-tab="${tab}"]`).classList.add("active");
  document.querySelector(`.tab-panel[data-tab="${tab}"]`).classList.add("active");
}

// Keyboard shortcut: 1-6 switches tabs
const TAB_KEYS = ["python", "sql", "html", "css", "js", "connect"];
document.addEventListener("keydown", e => {
  if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
  const n = parseInt(e.key);
  if (n >= 1 && n <= 6) showTab(TAB_KEYS[n - 1]);
  if (e.key === "Escape") closePanel();
});


/* ─── Slide-in detail panel ─────────────────────────────────── */
let currentTopicId  = null;
let currentTechKey  = null;
let notesSaveTimer  = null;

function openTopic(techKey, topicId) {
  currentTopicId = topicId;
  currentTechKey = techKey;

  // Find the topic data embedded in the page
  const card = document.querySelector(`[data-topic-id="${topicId}"]`);
  if (!card) return;

  // Header
  const panel     = document.getElementById("detailPanel");
  const header    = document.getElementById("dpHeader");
  const body      = document.getElementById("dpBody");
  const notesArea = document.getElementById("dpNotes");
  const notesSaved = document.getElementById("notesSaved");

  header.innerHTML = card.dataset.headerHtml;
  body.innerHTML   = card.dataset.bodyHtml;

  // Bookmark button state
  updateBookmarkBtn(topicId);

  // Load existing note
  loadNote(topicId, notesArea, notesSaved);

  document.getElementById("overlay").classList.add("open");
  panel.classList.add("open");
  document.body.style.overflow = "hidden";

  // Track progress (fire and forget)
  fetch("/api/progress", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({topic_id: topicId, tech_key: techKey})
  }).then(() => loadProgress());

  // Update chat context tag
  const ctxTag = document.getElementById("chatContextTag");
  if (ctxTag) {
    const name = card.querySelector(".tc-name")?.textContent || topicId;
    ctxTag.textContent = `Context: ${name}`;
    ctxTag.style.display = "block";
  }
}

function closePanel() {
  currentTopicId = null;
  currentTechKey = null;
  document.getElementById("overlay").classList.remove("open");
  document.getElementById("detailPanel").classList.remove("open");
  document.body.style.overflow = "";
  const ctxTag = document.getElementById("chatContextTag");
  if (ctxTag) ctxTag.style.display = "none";
}

document.getElementById("overlay")?.addEventListener("click", closePanel);


/* ─── Bookmarks ─────────────────────────────────────────────── */
let bookmarkedIds = new Set();

async function loadBookmarks() {
  const res  = await fetch("/api/bookmarks");
  const data = await res.json();
  bookmarkedIds = new Set(data.bookmarks.map(b => b.topic_id));
  document.querySelectorAll(".tc-star").forEach(el => {
    el.classList.toggle("visible", bookmarkedIds.has(el.closest("[data-topic-id]")?.dataset.topicId));
  });
}

function updateBookmarkBtn(topicId) {
  const btn = document.getElementById("dpBookmarkBtn");
  if (!btn) return;
  btn.classList.toggle("active", bookmarkedIds.has(topicId));
  btn.title = bookmarkedIds.has(topicId) ? "Remove bookmark" : "Bookmark this topic";
}

async function toggleBookmark() {
  if (!currentTopicId) return;
  const btn = document.getElementById("dpBookmarkBtn");

  if (bookmarkedIds.has(currentTopicId)) {
    await fetch(`/api/bookmarks/${currentTopicId}`, {method: "DELETE"});
    bookmarkedIds.delete(currentTopicId);
  } else {
    const card = document.querySelector(`[data-topic-id="${currentTopicId}"]`);
    const name = card?.querySelector(".tc-name")?.textContent || currentTopicId;
    await fetch("/api/bookmarks", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({topic_id: currentTopicId, tech_key: currentTechKey, topic_name: name})
    });
    bookmarkedIds.add(currentTopicId);
  }

  updateBookmarkBtn(currentTopicId);
  // Refresh star indicators
  document.querySelectorAll(".tc-star").forEach(el => {
    el.classList.toggle("visible", bookmarkedIds.has(el.closest("[data-topic-id]")?.dataset.topicId));
  });
}


/* ─── Notes ─────────────────────────────────────────────────── */
async function loadNote(topicId, textarea, savedLabel) {
  if (!textarea) return;
  const res  = await fetch(`/api/notes/${topicId}`);
  const data = await res.json();
  textarea.value = data.note ? data.note.content : "";
  if (savedLabel) savedLabel.style.opacity = "0";
}

function onNoteInput(textarea, savedLabel) {
  clearTimeout(notesSaveTimer);
  if (savedLabel) savedLabel.style.opacity = "0";
  notesSaveTimer = setTimeout(async () => {
    if (!currentTopicId) return;
    await fetch("/api/notes", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        topic_id: currentTopicId,
        tech_key: currentTechKey,
        content: textarea.value
      })
    });
    if (savedLabel) {
      savedLabel.style.opacity = "1";
      setTimeout(() => { savedLabel.style.opacity = "0"; }, 2000);
    }
  }, 800);
}


/* ─── Progress ──────────────────────────────────────────────── */
let viewedIds = new Set();

async function loadProgress() {
  const res  = await fetch("/api/progress");
  const data = await res.json();
  viewedIds  = new Set(data.progress.map(p => p.topic_id));

  const total = document.querySelectorAll("[data-topic-id]").length;
  document.querySelectorAll(".tc-dot").forEach(el => {
    el.classList.toggle("visible", viewedIds.has(el.closest("[data-topic-id]")?.dataset.topicId));
  });

  // Update header badge
  const badge = document.getElementById("progressCount");
  if (badge) badge.textContent = viewedIds.size;
  const total_badge = document.getElementById("progressTotal");
  if (total_badge) total_badge.textContent = total;
}


/* ─── Mode Toggle ────────────────────────────────────────────── */
function setMode(mode) {
  localStorage.setItem("playbook_mode", mode);
  document.querySelectorAll(".mode-btn").forEach(b => {
    b.classList.toggle("active", b.dataset.mode === mode);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  // Restore mode from localStorage (default: reference)
  const mode = localStorage.getItem("playbook_mode") || "reference";
  setMode(mode);

  loadProgress();
  loadBookmarks();
});
