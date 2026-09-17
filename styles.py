"""Styling constants for Rudy's digital twin Gradio app."""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Give me the quick version of Rudy's career story.",
    "What are Rudy's strongest data science and AI skills?",
    "Tell me about a project Rudy is especially proud of.",
    "What kind of roles and problems is Rudy best suited for?",
]

CSS = r"""
:root {
  --twin-gold: #ecad0a;
  --twin-gold-soft: rgba(236, 173, 10, 0.14);
  --twin-blue: #209dd7;
  --twin-blue-soft: rgba(32, 157, 215, 0.14);
  --twin-purple: #753991;
  --twin-purple-soft: rgba(117, 57, 145, 0.16);

  --twin-bg: #090b10;
  --twin-bg-2: #0d1017;
  --twin-surface: rgba(17, 21, 30, 0.92);
  --twin-surface-solid: #11151e;
  --twin-surface-2: #171c27;
  --twin-surface-3: #202634;
  --twin-border: rgba(255, 255, 255, 0.09);
  --twin-border-strong: rgba(255, 255, 255, 0.16);
  --twin-text: #f5f7fb;
  --twin-muted: #98a2b3;
  --twin-subtle: #697386;
  --twin-shadow: 0 24px 80px rgba(0, 0, 0, 0.30);
  --twin-radius-xl: 24px;
  --twin-radius-lg: 18px;
  --twin-radius-md: 14px;
  --twin-radius-sm: 10px;
}

body:not(.dark) {
  --twin-bg: #f5f7fb;
  --twin-bg-2: #edf1f7;
  --twin-surface: rgba(255, 255, 255, 0.92);
  --twin-surface-solid: #ffffff;
  --twin-surface-2: #f7f9fc;
  --twin-surface-3: #edf1f6;
  --twin-border: rgba(16, 24, 40, 0.09);
  --twin-border-strong: rgba(16, 24, 40, 0.16);
  --twin-text: #172033;
  --twin-muted: #667085;
  --twin-subtle: #98a2b3;
  --twin-shadow: 0 24px 70px rgba(34, 48, 73, 0.11);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
html, body, gradio-app {
  min-height: 100%;
  background:
    radial-gradient(circle at 12% -8%, var(--twin-purple-soft), transparent 30%),
    radial-gradient(circle at 92% 4%, var(--twin-blue-soft), transparent 27%),
    linear-gradient(180deg, var(--twin-bg-2), var(--twin-bg)) !important;
}
body { margin: 0; }

footer, .built-with, .show-api, .api-docs { display: none !important; }

.gradio-container {
  width: 100% !important;
  max-width: 1040px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 42px 28px 56px !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}
.gradio-container .main,
.gradio-container .contain,
.gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* Product hero injected by JS */
.twin-hero {
  position: relative;
  overflow: hidden;
  margin-bottom: 20px;
  padding: 28px 30px 26px;
  border: 1px solid var(--twin-border);
  border-radius: var(--twin-radius-xl);
  background:
    linear-gradient(135deg, rgba(117,57,145,.18), rgba(32,157,215,.07) 55%, rgba(236,173,10,.08)),
    var(--twin-surface);
  box-shadow: var(--twin-shadow);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
}
.twin-hero::before {
  content: "";
  position: absolute;
  width: 220px;
  height: 220px;
  right: -74px;
  top: -110px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(236,173,10,.22), transparent 68%);
  pointer-events: none;
}
.twin-hero-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  margin-bottom: 18px;
}
.twin-brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: var(--twin-muted);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.twin-live-dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: #42d392;
  box-shadow: 0 0 0 5px rgba(66, 211, 146, .10);
}
.twin-feedback-btn {
  appearance: none;
  min-height: 36px !important;
  padding: 0 13px !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 999px !important;
  background: rgba(255,255,255,.03) !important;
  color: var(--twin-muted) !important;
  font: 600 12px/1 Inter, ui-sans-serif, sans-serif !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  transition: transform .18s ease, color .18s ease, border-color .18s ease, background .18s ease !important;
}
.twin-feedback-btn:hover {
  transform: translateY(-1px);
  color: var(--twin-text) !important;
  border-color: var(--twin-border-strong) !important;
  background: rgba(255,255,255,.06) !important;
}
.twin-identity {
  display: flex;
  align-items: center;
  gap: 17px;
}
.twin-avatar {
  position: relative;
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  width: 58px;
  height: 58px;
  border-radius: 18px;
  color: #fff;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -.03em;
  background: linear-gradient(135deg, var(--twin-purple), var(--twin-blue));
  box-shadow: 0 12px 35px rgba(32,157,215,.18);
}
.twin-avatar::after {
  content: "AI";
  position: absolute;
  right: -5px;
  bottom: -5px;
  padding: 3px 5px;
  border: 2px solid var(--twin-surface-solid);
  border-radius: 7px;
  background: var(--twin-gold);
  color: #1d1600;
  font-size: 8px;
  font-weight: 900;
  letter-spacing: .06em;
}
.twin-copy { max-width: 760px; }
.twin-title {
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  color: var(--twin-text) !important;
  font-size: clamp(28px, 4vw, 42px) !important;
  line-height: 1.06 !important;
  font-weight: 780 !important;
  letter-spacing: -.045em !important;
}
.twin-title .accent {
  background: linear-gradient(90deg, var(--twin-gold), #ffd86b);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.twin-subtitle {
  max-width: 720px;
  margin: 10px 0 0;
  color: var(--twin-muted);
  font-size: 15px;
  line-height: 1.65;
}
.twin-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 20px;
}
.twin-tag {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 7px 10px;
  border: 1px solid var(--twin-border);
  border-radius: 999px;
  background: rgba(255,255,255,.025);
  color: var(--twin-muted);
  font-size: 11px;
  font-weight: 650;
}
.twin-tag::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 999px;
  background: var(--twin-blue);
}
.twin-tag:nth-child(2)::before { background: var(--twin-purple); }
.twin-tag:nth-child(3)::before { background: var(--twin-gold); }
.twin-tag:nth-child(4)::before { background: #42d392; }
.twin-original-title { display: none !important; }

/* Clean Gradio chrome */
.block, .form {
  background: transparent !important;
  box-shadow: none !important;
}
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container { display: none !important; }

/* Chat shell */
.chatbot,
.chatbot.block {
  min-height: 500px !important;
  max-height: 64vh !important;
  overflow: hidden !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-xl) !important;
  background: var(--twin-surface) !important;
  box-shadow: var(--twin-shadow) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}
.chatbot .placeholder,
.chatbot .placeholder * {
  color: var(--twin-muted) !important;
}
.chatbot .placeholder {
  max-width: 440px;
  margin: auto;
  padding: 36px 24px !important;
  text-align: center;
  line-height: 1.65;
}

/* Message rows */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap,
.bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}
.message-row {
  padding: 5px 14px !important;
}
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  max-width: min(78%, 720px) !important;
  padding: 11px 14px !important;
  border: 0 !important;
  border-radius: 16px !important;
  box-shadow: none !important;
  font-size: 14px !important;
  line-height: 1.6 !important;
}

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message-row[data-role="user"] .bubble {
  background: linear-gradient(135deg, #168fc8, var(--twin-blue)) !important;
  color: #fff !important;
  border-bottom-right-radius: 5px !important;
  box-shadow: 0 9px 25px rgba(32,157,215,.16) !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-bottom-left-radius: 5px !important;
}

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  margin: 0 0 9px !important;
  color: inherit !important;
  font-size: 14px !important;
  line-height: 1.6 !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }
.message-row .message a,
.message-row .message-bubble a,
.message-row .bubble a {
  color: var(--twin-gold) !important;
  text-decoration: none !important;
  border-bottom: 1px solid currentColor;
}
.message-row .message code,
.message-row .message-bubble code,
.message-row .bubble code {
  border-radius: 6px !important;
  background: rgba(255,255,255,.06) !important;
  color: inherit !important;
}

/* Composer */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
  align-items: stretch !important;
  gap: 9px !important;
  margin-top: 12px !important;
}
textarea,
input[type="text"] {
  min-height: 54px !important;
  padding: 15px 16px !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-lg) !important;
  background: var(--twin-surface) !important;
  color: var(--twin-text) !important;
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
  font-size: 14px !important;
  line-height: 1.45 !important;
  box-shadow: 0 8px 30px rgba(0,0,0,.08) !important;
  transition: border-color .18s ease, box-shadow .18s ease, background .18s ease !important;
}
textarea:hover,
input[type="text"]:hover { border-color: var(--twin-border-strong) !important; }
textarea:focus,
input[type="text"]:focus {
  outline: none !important;
  border-color: rgba(32,157,215,.65) !important;
  box-shadow: 0 0 0 4px var(--twin-blue-soft), 0 10px 30px rgba(0,0,0,.08) !important;
}
textarea::placeholder,
input::placeholder { color: var(--twin-subtle) !important; }

/* Buttons */
button {
  cursor: pointer;
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
  transition: transform .16s ease, background .16s ease, border-color .16s ease, color .16s ease, box-shadow .16s ease !important;
}
button:not(.icon-button):not(.twin-feedback-btn) {
  min-height: 48px !important;
  border-radius: var(--twin-radius-md) !important;
}
button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  min-width: 54px !important;
  min-height: 54px !important;
  padding: 0 16px !important;
  border: 1px solid rgba(236,173,10,.9) !important;
  border-radius: var(--twin-radius-lg) !important;
  background: linear-gradient(135deg, #f6c23e, var(--twin-gold)) !important;
  color: #171207 !important;
  box-shadow: 0 10px 24px rgba(236,173,10,.16) !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  transform: translateY(-1px);
  background: linear-gradient(135deg, #ffd76d, #f1b816) !important;
  box-shadow: 0 13px 30px rgba(236,173,10,.22) !important;
}
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 19px !important;
  height: 19px !important;
  margin: 0 auto !important;
  color: #171207 !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* Prompt examples */
.examples,
.examples-holder,
[data-testid="examples"] {
  margin-top: 15px !important;
  padding: 0 !important;
  background: transparent !important;
}
.examples::before,
.examples-holder::before,
[data-testid="examples"]::before {
  content: "Try asking";
  display: block;
  margin: 0 0 9px 2px;
  color: var(--twin-subtle);
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .07em;
  text-transform: uppercase;
}
.examples table,
.examples-table {
  width: 100% !important;
  border: 0 !important;
  background: transparent !important;
}
.examples button,
.example,
.examples td button,
[data-testid="examples"] button {
  min-height: 40px !important;
  padding: 9px 12px !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 999px !important;
  background: rgba(255,255,255,.025) !important;
  color: var(--twin-muted) !important;
  font-size: 12px !important;
  font-weight: 550 !important;
  letter-spacing: 0 !important;
  line-height: 1.35 !important;
  text-align: left !important;
  text-transform: none !important;
  box-shadow: none !important;
}
.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {
  transform: translateY(-1px);
  border-color: rgba(32,157,215,.45) !important;
  background: var(--twin-blue-soft) !important;
  color: var(--twin-text) !important;
}

/* Chat utility actions */
.icon-button,
.chatbot .icon-button {
  min-height: 0 !important;
  padding: 5px !important;
  border: 0 !important;
  border-radius: 8px !important;
  background: transparent !important;
  color: var(--twin-subtle) !important;
}
.icon-button:hover,
.chatbot .icon-button:hover {
  background: rgba(255,255,255,.045) !important;
  color: var(--twin-text) !important;
}

/* Feedback toast */
.twin-toast {
  position: fixed;
  left: 50%;
  bottom: 26px;
  z-index: 9999;
  transform: translate(-50%, 18px);
  opacity: 0;
  pointer-events: none;
  padding: 10px 14px;
  border: 1px solid var(--twin-border-strong);
  border-radius: 999px;
  background: var(--twin-surface-solid);
  color: var(--twin-text);
  box-shadow: var(--twin-shadow);
  font-size: 12px;
  transition: opacity .22s ease, transform .22s ease;
}
.twin-toast.show {
  opacity: 1;
  transform: translate(-50%, 0);
}

/* Scrollbars */
::-webkit-scrollbar { width: 9px; height: 9px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  border: 2px solid transparent;
  border-radius: 999px;
  background: var(--twin-border-strong);
  background-clip: padding-box;
}
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); background-clip: padding-box; }
::selection { background: rgba(236,173,10,.85); color: #171207; }

@media (max-width: 720px) {
  .gradio-container { padding: 18px 12px 34px !important; }
  .twin-hero { padding: 21px 18px 20px; border-radius: 20px; }
  .twin-hero-top { margin-bottom: 15px; }
  .twin-identity { align-items: flex-start; gap: 13px; }
  .twin-avatar { width: 48px; height: 48px; border-radius: 15px; font-size: 18px; }
  .twin-title { font-size: 28px !important; }
  .twin-subtitle { font-size: 14px; line-height: 1.55; }
  .twin-tags { margin-top: 16px; gap: 6px; }
  .twin-tag { padding: 6px 9px; font-size: 10px; }
  .chatbot, .chatbot.block { min-height: 440px !important; max-height: 60vh !important; border-radius: 20px !important; }
  .message-row { padding-inline: 8px !important; }
  .message-row .message,
  .message-row .message-bubble,
  .message-row .bubble { max-width: 88% !important; }
}

@media (max-width: 460px) {
  .twin-feedback-btn { padding: 0 10px !important; }
  .twin-feedback-btn .feedback-long { display: none; }
  .twin-avatar { display: none; }
  .twin-title { font-size: 26px !important; }
  .twin-tag:nth-child(4) { display: none; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    transition-duration: .01ms !important;
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
  }
}
"""

JS = r"""
() => {
  document.title = "Rudy's AI Twin";

  const getInput = () => {
    const areas = document.querySelectorAll('textarea');
    return areas.length ? areas[areas.length - 1] : null;
  };

  const setInput = (text) => {
    const area = getInput();
    if (!area) return false;
    const setter = Object.getOwnPropertyDescriptor(
      window.HTMLTextAreaElement.prototype,
      'value'
    )?.set;
    if (setter) setter.call(area, text);
    else area.value = text;
    area.dispatchEvent(new Event('input', { bubbles: true }));
    area.dispatchEvent(new Event('change', { bubbles: true }));
    area.focus();
    return true;
  };

  const showToast = (message) => {
    let toast = document.querySelector('.twin-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'twin-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    window.clearTimeout(window.__twinToastTimer);
    window.__twinToastTimer = window.setTimeout(() => toast.classList.remove('show'), 1900);
  };

  const buildHero = () => {
    const container = document.querySelector('.gradio-container');
    if (!container || container.querySelector('.twin-hero')) return;

    const firstTitle = container.querySelector('h1');
    if (firstTitle) firstTitle.classList.add('twin-original-title');

    const hero = document.createElement('section');
    hero.className = 'twin-hero';
    hero.setAttribute('aria-label', "Rudy's AI Twin introduction");
    hero.innerHTML = `
      <div class="twin-hero-top">
        <div class="twin-brand"><span class="twin-live-dot"></span> Digital Twin · Online</div>
        <button class="twin-feedback-btn" type="button" aria-label="Give feedback about this AI twin">
          <span>✦</span>&nbsp;<span class="feedback-long">Give </span>feedback
        </button>
      </div>
      <div class="twin-identity">
        <div class="twin-avatar" aria-hidden="true">R</div>
        <div class="twin-copy">
          <h1 class="twin-title">Meet <span class="accent">Rudy's AI Twin</span></h1>
          <p class="twin-subtitle">
            Ask me about Rudy's career, data science and AI work, projects, technical strengths,
            professional interests, or how to get in touch. Think of me as an interactive version
            of the resume — with considerably better conversation skills.
          </p>
        </div>
      </div>
      <div class="twin-tags" aria-label="Topics you can ask about">
        <span class="twin-tag">Career & experience</span>
        <span class="twin-tag">Data science & AI</span>
        <span class="twin-tag">Projects & impact</span>
        <span class="twin-tag">Professional fit</span>
      </div>
    `;

    container.insertBefore(hero, container.firstChild);

    const feedback = hero.querySelector('.twin-feedback-btn');
    feedback?.addEventListener('click', () => {
      const prompt = "I have feedback about this AI twin: ";
      if (setInput(prompt)) showToast('Feedback mode ready — type your note and send it.');
      else showToast('Start a chat and share your feedback there.');
    });
  };

  const improveInput = () => {
    const area = getInput();
    if (!area) return;
    if (!area.dataset.twinPlaceholder) {
      area.dataset.twinPlaceholder = '1';
      area.setAttribute('placeholder', "Ask Rudy's AI twin anything about his career, work, or projects…");
      area.setAttribute('aria-label', "Message Rudy's AI Twin");
    }
  };

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => {
    buildHero();
    improveInput();
    document.querySelectorAll('textarea').forEach(watchTextarea);
  };

  setTimeout(() => {
    scan();
    getInput()?.focus();
  }, 280);

  let scheduled = false;
  new MutationObserver(() => {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => {
      scheduled = false;
      scan();
    });
  }).observe(document.body, { childList: true, subtree: true });
};
"""
