import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os

# --- FULL MASTER LIST (ALL WORDS PRESERVED) ---
vocab_list = [
    # --- LIFE ADVANCED / SPECIAL PHRASES ---
    ("leichter gesagt als getan", "easier said than done", "Phrases"),
    ("auf wundersame Weise", "miraculously", "Phrases"),
    ("sich etw. zum Prinzip machen", "to make a point of something", "Phrases"),
    ("aus allen Gesellschaftsschichten", "from all walks of life", "Phrases"),
    ("von Bäumen gesäumt", "tree-lined", "Phrases"),
    ("vor Gericht stehen", "to go on trial", "Phrases"),
    ("geistig", "intellectual", "Phrases"),
    ("handwerklich", "manual", "Phrases"),
    ("sozial", "social", "Phrases"),
    ("das Leitprinzip", "guiding principle", "Phrases"),
    ("der Umfang", "scope", "Phrases"),
    ("die Jacht", "yacht", "Phrases"),

    # --- B1+ / B2 GRAMMAR & VERBS ---
    ("einbehalten", "to withhold", "B2 Verbs"),
    ("abziehen", "to subtract", "B2 Verbs"),
    ("sich etwas aneignen", "to acquire something", "B2 Verbs"),
    ("sich etwas einprägen", "to memorize something", "B2 Verbs"),
    ("sich etwas leisten", "to afford something", "B2 Verbs"),
    ("sich etwas merken", "to remember something", "B2 Verbs"),
    ("sich etwas vorstellen", "to imagine something", "B2 Verbs"),
    ("sich etwas wünschen", "to wish for something", "B2 Verbs"),
    ("den Vertrag verlängern", "to extend the contract", "B2 Verbs"),
    ("etwas bedarf der Schriftform", "something requires the written form", "B2 Verbs"),
    ("sich etwas überlegen", "to think something over", "B2 Verbs"),
    ("sich etwas gönnen", "to treat oneself to something", "B2 Verbs"),
    ("sich etwas leihen", "to borrow something", "B2 Verbs"),
    ("sich etwas erfüllen", "to fulfill for oneself", "B2 Verbs"),

    # --- EINFACH BESSER B2 / DTZ (Vocational) ---
    ("der Arbeitgeber", "employer", "Vocational"),
    ("die Arbeitslosigkeit", "unemployment", "Vocational"),
    ("der Abschluss", "graduation", "Vocational"),
    ("die Absicht", "intention", "Vocational"),
    ("die Abteilung", "department", "Vocational"),
    ("die Beratung", "consultation", "Vocational"),
    ("der Betrieb", "business", "Vocational"),
    ("die Branche", "industry", "Vocational"),
    ("die Bruttovergütung", "gross remuneration", "Vocational"),
    ("die Lohnsteuer", "wage tax", "Vocational"),
    ("der Nettoverdienst", "net earnings", "Vocational"),
    ("die Quittung", "receipt", "Vocational"),
    ("die Rente", "pension", "Vocational"),
    ("das Unternehmen", "company", "Vocational"),
    ("die Steuerklasse", "tax bracket", "Vocational"),
    ("die Integration", "integration", "Vocational"),
    ("der Lebenslauf", "CV", "Vocational"),
    ("die Belegschaft", "workforce", "Vocational"),

    # --- CORE IRREGULAR VERBS ---
    ("abbiegen", "to turn", "Core Verbs"),
    ("abfahren", "to depart", "Core Verbs"),
    ("abgeben", "to hand in", "Core Verbs"),
    ("abhängen von", "to depend on", "Core Verbs"),
    ("abheben", "to withdraw money", "Core Verbs"),
    ("abholen", "to pick up", "Core Verbs"),
    ("ablehnen", "to reject", "Core Verbs"),
    ("absagen", "to cancel", "Core Verbs"),
    ("abstimmen", "to vote", "Core Verbs"),
    ("abwaschen", "to wash up", "Core Verbs"),
    ("achten auf", "to pay attention to", "Core Verbs"),
    ("anfangen", "to start", "Core Verbs"),
    ("anrufen", "to call", "Core Verbs"),
    ("antworten", "to answer", "Core Verbs"),
    ("anziehen", "to put on clothes", "Core Verbs"),
    ("aufhören", "to stop", "Core Verbs"),
    ("aufräumen", "to tidy up", "Core Verbs"),
    ("aufstehen", "to get up", "Core Verbs"),
    ("ausziehen", "to move out", "Core Verbs"),
    ("backen", "to bake", "Core Verbs"),
    ("beantworten", "to answer", "Core Verbs"),
    ("bedienen", "to operate", "Core Verbs"),
    ("sich befinden", "to be located", "Core Verbs"),
    ("beginnen", "to begin", "Core Verbs"),
    ("begreifen", "to understand", "Core Verbs"),
    ("behalten", "to keep", "Core Verbs"),
    ("beißen", "to bite", "Core Verbs"),
    ("bekommen", "to get", "Core Verbs"),
    ("beraten", "to advise", "Core Verbs"),
    ("beschäftigen", "to employ", "Core Verbs"),
    ("bestimmen", "to determine", "Core Verbs"),
    ("besuchen", "to visit", "Core Verbs"),
    ("betreuen", "to look after", "Core Verbs"),
    ("sich bewerben", "to apply", "Core Verbs"),
    ("bezahlen", "to pay", "Core Verbs"),
    ("biegen", "to bend", "Core Verbs"),
    ("bieten", "to offer", "Core Verbs"),
    ("bitten", "to ask", "Core Verbs"),
    ("bleiben", "to stay", "Core Verbs"),
    ("braten", "to fry", "Core Verbs"),
    ("brechen", "to break", "Core Verbs"),
    ("brennen", "to burn", "Core Verbs"),
    ("bringen", "to bring", "Core Verbs"),
    ("denken", "to think", "Core Verbs"),
    ("dürfen", "to be allowed to", "Core Verbs"),
    ("einladen", "to invite", "Core Verbs"),
    ("einschlafen", "to fall asleep", "Core Verbs"),
    ("einziehen", "to move in", "Core Verbs"),
    ("empfehlen", "to recommend", "Core Verbs"),
    ("entscheiden", "to decide", "Core Verbs"),
    ("erfahren", "to learn", "Core Verbs"),
    ("erinnern", "to remind", "Core Verbs"),
    ("erkennen", "to recognize", "Core Verbs"),
    ("erklären", "to explain", "Core Verbs"),
    ("essen", "to eat", "Core Verbs"),
    ("fahren", "to drive", "Core Verbs"),
    ("fallen", "to fall", "Core Verbs"),
    ("fangen", "to catch", "Core Verbs"),
    ("fernsehen", "to watch TV", "Core Verbs"),
    ("finden", "to find", "Core Verbs"),
    ("fliegen", "to fly", "Core Verbs"),
    ("fließen", "to flow", "Core Verbs"),
    ("fressen", "to eat", "Core Verbs"),
    ("frieren", "to freeze", "Core Verbs"),
    ("geben", "to give", "Core Verbs"),
    ("gefallen", "to please", "Core Verbs"),
    ("gehen", "to go", "Core Verbs"),
    ("gelingen", "to succeed", "Core Verbs"),
    ("geschehen", "to happen", "Core Verbs"),
    ("gießen", "to pour", "Core Verbs"),
    ("glauben", "to believe", "Core Verbs"),
    ("haben", "to have", "Core Verbs"),
    ("halten", "to hold", "Core Verbs"),
    ("helfen", "to help", "Core Verbs"),
    ("kennen", "to know", "Core Verbs"),
    ("kochen", "to cook", "Core Verbs"),
    ("kommen", "to come", "Core Verbs"),
    ("können", "to be able to", "Core Verbs"),
    ("lassen", "to let", "Core Verbs"),
    ("laufen", "to run", "Core Verbs"),
    ("lehren", "to teach", "Core Verbs"),
    ("leiden", "to suffer", "Core Verbs"),
    ("leihen", "to lend", "Core Verbs"),
    ("leisten", "to achieve", "Core Verbs"),
    ("lesen", "to read", "Core Verbs"),
    ("liegen", "to lie", "Core Verbs"),
    ("lügen", "to lie", "Core Verbs"),
    ("machen", "to do", "Core Verbs"),
    ("meinen", "to mean", "Core Verbs"),
    ("messen", "to measure", "Core Verbs"),
    ("mögen", "to like", "Core Verbs"),
    ("müssen", "to must", "Core Verbs"),
    ("nehmen", "to take", "Core Verbs"),
    ("nennen", "to call", "Core Verbs"),
    ("öffnen", "to open", "Core Verbs"),
    ("pflegen", "to care for", "Core Verbs"),
    ("probieren", "to try", "Core Verbs"),
    ("produzieren", "to produce", "Core Verbs"),
    ("raten", "to guess", "Core Verbs"),
    ("rechnen", "to calculate", "Core Verbs"),
    ("riechen", "to smell", "Core Verbs"),
    ("rufen", "to call", "Core Verbs"),
    ("sagen", "to say", "Core Verbs"),
    ("schlafen", "to sleep", "Core Verbs"),
    ("schließen", "to close", "Core Verbs"),
    ("schmecken", "to taste", "Core Verbs"),
    ("schneiden", "to cut", "Core Verbs"),
    ("schreiben", "to write", "Core Verbs"),
    ("schwimmen", "to swim", "Core Verbs"),
    ("sehen", "to see", "Core Verbs"),
    ("sein", "to be", "Core Verbs"),
    ("singen", "to sing", "Core Verbs"),
    ("sitzen", "to sit", "Core Verbs"),
    ("sollen", "to should", "Core Verbs"),
    ("spielen", "to play", "Core Verbs"),
    ("sprechen", "to speak", "Core Verbs"),
    ("springen", "to jump", "Core Verbs"),
    ("stehen", "to stand", "Core Verbs"),
    ("stehlen", "to steal", "Core Verbs"),
    ("steigen", "to climb", "Core Verbs"),
    ("sterben", "to die", "Core Verbs"),
    ("studieren", "to study", "Core Verbs"),
    ("suchen", "to search", "Core Verbs"),
    ("tanzen", "to dance", "Core Verbs"),
    ("tragen", "to wear", "Core Verbs"),
    ("treffen", "to meet", "Core Verbs"),
    ("trinken", "to drink", "Core Verbs"),
    ("tun", "to do", "Core Verbs"),
    ("vergessen", "to forget", "Core Verbs"),
    ("vergleichen", "to compare", "Core Verbs"),
    ("verlieren", "to lose", "Core Verbs"),
    ("verstehen", "to understand", "Core Verbs"),
    ("waschen", "to wash", "Core Verbs"),
    ("warten", "to wait", "Core Verbs"),
    ("werden", "to become", "Core Verbs"),
    ("werfen", "to throw", "Core Verbs"),
    ("wissen", "to know", "Core Verbs"),
    ("wohnen", "to live", "Core Verbs"),
    ("wollen", "to want", "Core Verbs"),
    ("zeigen", "to show", "Core Verbs"),
    ("ziehen", "to pull", "Core Verbs"),
]

# Category colours
CATEGORY_COLORS = {
    "Phrases":    "#9B59B6",
    "B2 Verbs":   "#E67E22",
    "Vocational": "#2980B9",
    "Core Verbs": "#27AE60",
}

# Theme palette
BG         = "#1A1A2E"
CARD_BG    = "#16213E"
HEADER_BG  = "#0F3460"
ACCENT     = "#E94560"
GOLD       = "#F5A623"
GREEN      = "#2ECC71"
RED_WRONG  = "#E74C3C"
TEXT_LIGHT = "#ECF0F1"
TEXT_DIM   = "#95A5A6"
ENTRY_BG   = "#0D1B2A"
DE_COLOR   = "#5DADE2"   # blue tint for DE→EN mode indicator
EN_COLOR   = "#58D68D"   # green tint for EN→DE mode indicator
BOTH_COLOR = "#F39C12"   # amber for mixed mode


class VocabMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🇩🇪 Vocab Schatz – Mastery Pro v11 (Bidirectional)")
        self.root.geometry("720x900")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.data_file   = "vocab_master_v11.json"
        self.known_words = self.load_progress()

        # State
        self.streak      = 0
        self.correct_cnt = 0
        self.wrong_cnt   = 0
        self.hint_idx    = 0
        self.mc_mode     = tk.BooleanVar(value=False)
        self.timer_id    = None
        self.time_left   = 20
        self.cur_de      = ""
        self.cur_en      = ""
        self.cur_cat     = ""
        self.cur_answer  = ""   # the correct answer for the current direction
        self.cur_prompt  = ""   # what is shown as the question

        # Direction: "de_to_en", "en_to_de", "mixed"
        self.direction   = tk.StringVar(value="de_to_en")

        self._build_ui()
        self.load_next_word()

    # ─────────────────────────────── UI BUILD ────────────────────────────────

    def _build_ui(self):
        # ── Header ──
        hdr = tk.Frame(self.root, bg=HEADER_BG, height=90)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        tk.Label(hdr, text="🇩🇪  Vocab Schatz", font=("Helvetica", 22, "bold"),
                 bg=HEADER_BG, fg=TEXT_LIGHT).pack(side="left", padx=20, pady=18)

        self.lbl_streak = tk.Label(hdr, text="🔥 0", font=("Helvetica", 16, "bold"),
                                   bg=HEADER_BG, fg=GOLD)
        self.lbl_streak.pack(side="right", padx=20)
        self.lbl_score = tk.Label(hdr, text="✅0  ❌0", font=("Helvetica", 11),
                                  bg=HEADER_BG, fg=TEXT_DIM)
        self.lbl_score.pack(side="right", padx=10)

        # ── Progress bar row ──
        prow = tk.Frame(self.root, bg=BG)
        prow.pack(fill="x", padx=30, pady=(14, 0))
        self.lbl_stats = tk.Label(prow, text="Mastery: 0%", font=("Helvetica", 10, "bold"),
                                  bg=BG, fg=TEXT_DIM)
        self.lbl_stats.pack(side="left")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Fancy.Horizontal.TProgressbar", thickness=10,
                         troughcolor="#0D1B2A", background=ACCENT, borderwidth=0)
        self.progress = ttk.Progressbar(prow, style="Fancy.Horizontal.TProgressbar",
                                        orient="horizontal", length=400, mode="determinate")
        self.progress.pack(side="right", pady=4)

        # ── Direction selector row ──
        drow = tk.Frame(self.root, bg=BG)
        drow.pack(fill="x", padx=30, pady=(10, 0))

        tk.Label(drow, text="Direction:", font=("Helvetica", 10, "bold"),
                 bg=BG, fg=TEXT_DIM).pack(side="left", padx=(0, 10))

        self.btn_de_en = self._make_radio_btn(drow, "🇩🇪 → 🇬🇧  German → English", "de_to_en", DE_COLOR)
        self.btn_de_en.pack(side="left", padx=4)

        self.btn_en_de = self._make_radio_btn(drow, "🇬🇧 → 🇩🇪  English → German", "en_to_de", EN_COLOR)
        self.btn_en_de.pack(side="left", padx=4)

        self.btn_both = self._make_radio_btn(drow, "🔀  Mixed", "mixed", BOTH_COLOR)
        self.btn_both.pack(side="left", padx=4)

        # Direction indicator label
        self.lbl_dir = tk.Label(self.root, text="", font=("Helvetica", 10, "bold"),
                                bg=BG, fg=DE_COLOR)
        self.lbl_dir.pack(anchor="w", padx=32, pady=(4, 0))

        # ── Mode toggle & timer row ──
        mrow = tk.Frame(self.root, bg=BG)
        mrow.pack(fill="x", padx=30, pady=(6, 0))
        tk.Checkbutton(mrow, text="  🎲 Multiple-Choice mode", variable=self.mc_mode,
                       font=("Helvetica", 10, "bold"), bg=BG, fg=TEXT_LIGHT,
                       selectcolor=HEADER_BG, activebackground=BG,
                       command=self.load_next_word).pack(side="left")
        self.lbl_timer = tk.Label(mrow, text="⏱ 20", font=("Helvetica", 12, "bold"),
                                  bg=BG, fg=GOLD)
        self.lbl_timer.pack(side="right")

        # ── Main card ──
        self.card = tk.Frame(self.root, bg=CARD_BG, bd=0,
                             highlightbackground=ACCENT, highlightthickness=2)
        self.card.pack(padx=30, pady=14, fill="both", expand=True)

        # Category badge + direction mini-badge
        badge_row = tk.Frame(self.card, bg=CARD_BG)
        badge_row.pack(anchor="ne", padx=16, pady=(14, 0))

        self.lbl_dir_badge = tk.Label(badge_row, text="DE→EN", font=("Helvetica", 9, "bold"),
                                      bg=DE_COLOR, fg="white", padx=8, pady=3)
        self.lbl_dir_badge.pack(side="right", padx=(4, 0))

        self.lbl_cat = tk.Label(badge_row, text="", font=("Helvetica", 9, "bold"),
                                bg=CARD_BG, fg="white", padx=10, pady=3)
        self.lbl_cat.pack(side="right")

        # Prompt language label (small, above the main word)
        self.lbl_prompt_lang = tk.Label(self.card, text="",
                                        font=("Helvetica", 10, "italic"),
                                        bg=CARD_BG, fg=TEXT_DIM)
        self.lbl_prompt_lang.pack(pady=(8, 0))

        # Prompt word (what to translate)
        self.lbl_word = tk.Label(self.card, text="", font=("Helvetica", 30, "bold"),
                                 bg=CARD_BG, fg=TEXT_LIGHT, wraplength=580,
                                 justify="center")
        self.lbl_word.pack(pady=(4, 4))

        # Instruction / feedback
        self.lbl_feedback = tk.Label(self.card, text="", font=("Helvetica", 13),
                                     bg=CARD_BG, fg=TEXT_DIM, wraplength=560)
        self.lbl_feedback.pack(pady=4)

        # Answer entry (type mode)
        self.entry = tk.Entry(self.card, font=("Helvetica", 17), justify="center",
                              bd=0, bg=ENTRY_BG, fg=TEXT_LIGHT,
                              insertbackground=ACCENT, relief="flat")
        self.entry.pack(pady=8, padx=60, ipady=12, fill="x")
        self.entry.bind("<Return>", lambda e: self.check_answer())

        # Multiple-choice frame
        self.mc_frame = tk.Frame(self.card, bg=CARD_BG)
        self.mc_frame.pack(pady=6, padx=40, fill="x")
        self.mc_buttons = []
        for i in range(4):
            btn = tk.Button(self.mc_frame, text="", font=("Helvetica", 11),
                            bg=HEADER_BG, fg=TEXT_LIGHT, relief="flat",
                            cursor="hand2", pady=9, wraplength=540,
                            command=lambda x=i: self.mc_check(x))
            btn.pack(fill="x", pady=4)
            self.mc_buttons.append(btn)

        # Action buttons
        btn_row = tk.Frame(self.card, bg=CARD_BG)
        btn_row.pack(pady=10)

        self.btn_check = self._make_btn(btn_row, "✔  CHECK", ACCENT, self.check_answer)
        self.btn_check.pack(side="left", padx=8)

        self.btn_hint = self._make_btn(btn_row, "💡  HINT", GOLD, self.give_hint)
        self.btn_hint.pack(side="left", padx=8)

        self.btn_skip = self._make_btn(btn_row, "⏭  SKIP", "#555", self.load_next_word)
        self.btn_skip.pack(side="left", padx=8)

        self.btn_done = tk.Button(self.card, text="✅  Archive as Learned",
                                  font=("Helvetica", 10, "bold"), fg=GREEN,
                                  bg=CARD_BG, relief="flat", cursor="hand2",
                                  activeforeground=GREEN, activebackground=CARD_BG,
                                  command=self.mark_done)
        self.btn_done.pack(pady=(4, 16))

        # Footer
        tk.Button(self.root, text="⟳  RESET ALL PROGRESS",
                  command=self.restore, fg=TEXT_DIM, bg=BG,
                  relief="flat", font=("Arial", 8),
                  activeforeground=ACCENT, activebackground=BG,
                  cursor="hand2").pack(side="bottom", pady=8)

    def _make_radio_btn(self, parent, text, value, color):
        """A styled radio-button-like toggle."""
        btn = tk.Radiobutton(
            parent, text=text, variable=self.direction, value=value,
            font=("Helvetica", 9, "bold"),
            bg=BG, fg=color,
            selectcolor=HEADER_BG,
            activebackground=BG, activeforeground=color,
            indicatoron=True,
            command=self.on_direction_change
        )
        return btn

    def _make_btn(self, parent, text, color, cmd):
        btn = tk.Button(parent, text=text, font=("Helvetica", 11, "bold"),
                        bg=color, fg="white", relief="flat", cursor="hand2",
                        padx=18, pady=10, command=cmd)
        btn.bind("<Enter>", lambda e, b=btn, c=color: b.configure(bg=self._dim(c, 1.15)))
        btn.bind("<Leave>", lambda e, b=btn, c=color: b.configure(bg=c))
        return btn

    def _dim(self, hex_color, factor):
        h = hex_color.lstrip("#")
        r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (min(255, int(r*factor)),
                                  min(255, int(g*factor)),
                                  min(255, int(b*factor)))

    # ─────────────────────────────── DIRECTION ───────────────────────────────

    def on_direction_change(self):
        """Called when direction radio changes – reload word, keep scores."""
        self.load_next_word()

    def _pick_direction_for_word(self):
        """Returns 'de_to_en' or 'en_to_de' for the current card."""
        d = self.direction.get()
        if d == "mixed":
            return random.choice(["de_to_en", "en_to_de"])
        return d

    def _update_direction_ui(self, word_dir):
        if word_dir == "de_to_en":
            badge_text = "DE→EN"
            badge_color = DE_COLOR
            prompt_lang = "🇩🇪  Translate from German"
            dir_label   = "🇩🇪 → 🇬🇧  Type the English translation"
        else:
            badge_text = "EN→DE"
            badge_color = EN_COLOR
            prompt_lang = "🇬🇧  Translate from English"
            dir_label   = "🇬🇧 → 🇩🇪  Type the German translation"

        self.lbl_dir_badge.config(text=badge_text, bg=badge_color)
        self.lbl_prompt_lang.config(text=prompt_lang, fg=badge_color)
        self.lbl_dir.config(text=dir_label, fg=badge_color)
        self.lbl_feedback.config(
            text="Type your answer and press ENTER or CHECK", fg=TEXT_DIM)

    # ─────────────────────────────── PROGRESS ────────────────────────────────

    def load_progress(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_progress(self):
        with open(self.data_file, "w") as f:
            json.dump(self.known_words, f)

    # ─────────────────────────────── TIMER ───────────────────────────────────

    def _stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def _start_timer(self):
        self._stop_timer()
        self.time_left = 20
        self._tick()

    def _tick(self):
        self.lbl_timer.config(text=f"⏱ {self.time_left}",
                               fg=RED_WRONG if self.time_left <= 5 else GOLD)
        if self.time_left <= 0:
            self.lbl_feedback.config(text=f"⌛ Time's up!  →  {self.cur_answer}", fg=RED_WRONG)
            self.streak = 0
            self._update_score_display()
            self.root.after(1800, self.load_next_word)
            return
        self.time_left -= 1
        self.timer_id = self.root.after(1000, self._tick)

    # ─────────────────────────────── WORD LOAD ───────────────────────────────

    def load_next_word(self):
        self._stop_timer()
        active = [v for v in vocab_list if v[0] not in self.known_words]
        total   = len(vocab_list)
        learned = len(self.known_words)

        perc = (learned / total * 100) if total else 0
        self.progress["value"] = perc
        self.lbl_stats.config(text=f"Mastery: {int(perc)}%  ({learned}/{total})")

        if not active:
            self._show_complete()
            return

        self.cur_de, self.cur_en, self.cur_cat = random.choice(active)
        self.hint_idx = 0

        # Decide direction for this card
        word_dir = self._pick_direction_for_word()
        self._active_word_dir = word_dir   # remember for check_answer

        if word_dir == "de_to_en":
            self.cur_prompt = self.cur_de
            self.cur_answer = self.cur_en
        else:
            self.cur_prompt = self.cur_en
            self.cur_answer = self.cur_de

        # Update direction UI
        self._update_direction_ui(word_dir)

        # Category badge
        cat_col = CATEGORY_COLORS.get(self.cur_cat, "#555")
        self.lbl_cat.config(text=f" {self.cur_cat} ", bg=cat_col)

        self.lbl_word.config(text=self.cur_prompt, fg=TEXT_LIGHT)

        self.entry.delete(0, tk.END)
        self.card.configure(highlightbackground=ACCENT)

        if self.mc_mode.get():
            self._setup_mc(word_dir)
            self.entry.pack_forget()
            self.btn_check.config(state="disabled")
            self.mc_frame.pack(pady=6, padx=40, fill="x")
        else:
            self.mc_frame.pack_forget()
            self.entry.pack(pady=8, padx=60, ipady=12, fill="x")
            self.btn_check.config(state="normal")
            self.entry.focus_set()

        self._start_timer()

    def _setup_mc(self, word_dir):
        if word_dir == "de_to_en":
            pool = [v[1] for v in vocab_list if v[1] != self.cur_en]
            correct = self.cur_en
        else:
            pool = [v[0] for v in vocab_list if v[0] != self.cur_de]
            correct = self.cur_de

        distractors = random.sample(pool, 3)
        choices = distractors + [correct]
        random.shuffle(choices)
        self._mc_choices = choices
        self._mc_correct = correct
        for i, btn in enumerate(self.mc_buttons):
            btn.config(text=choices[i], bg=HEADER_BG, fg=TEXT_LIGHT, state="normal")

    def _show_complete(self):
        self._stop_timer()
        self.lbl_word.config(text="🏆  ALL WORDS MASTERED!", fg=GOLD)
        self.lbl_feedback.config(
            text="Incredible! You've learned everything in the Schatz!", fg=GREEN)
        self.lbl_cat.config(text=" Complete! ", bg=GREEN)
        self.lbl_prompt_lang.config(text="")
        self.entry.pack_forget()
        self.mc_frame.pack_forget()

    # ─────────────────────────────── ANSWER CHECK ────────────────────────────

    def _normalise(self, text):
        """Lowercase; strip 'to ' prefix for verbs when checking."""
        t = text.strip().lower()
        return t

    def _answers_match(self, guess, correct):
        g = self._normalise(guess)
        c = self._normalise(correct)
        # also accept without "to " for English verbs
        c_alt = c[3:] if c.startswith("to ") else c
        # also accept without articles for German nouns (der/die/das/den/dem)
        c_alt2 = c
        for art in ("der ", "die ", "das ", "den ", "dem ", "ein ", "eine "):
            if c.startswith(art):
                c_alt2 = c[len(art):]
                break
        return g in (c, c_alt, c_alt2)

    def check_answer(self):
        guess = self.entry.get().strip()
        if not guess:
            return
        if self._answers_match(guess, self.cur_answer):
            self._on_correct()
        else:
            self._on_wrong()

    def mc_check(self, idx):
        chosen = self._mc_choices[idx]
        if self._answers_match(chosen, self._mc_correct):
            self.mc_buttons[idx].config(bg=GREEN)
            self._on_correct()
        else:
            self.mc_buttons[idx].config(bg=RED_WRONG)
            for i, btn in enumerate(self.mc_buttons):
                if self._answers_match(self._mc_choices[i], self._mc_correct):
                    btn.config(bg=GREEN)
            for btn in self.mc_buttons:
                btn.config(state="disabled")
            self._on_wrong(skip_next=False)
            self.root.after(1600, self.load_next_word)

    def _on_correct(self):
        self._stop_timer()
        self.streak += 1
        self.correct_cnt += 1
        self._update_score_display()
        streak_txt = f"🔥 {self.streak} streak!" if self.streak > 1 else "Correct! 🎉"
        self.lbl_feedback.config(text=streak_txt, fg=GREEN)
        self.card.configure(highlightbackground=GREEN)
        self._flash_card(GREEN)
        self.root.after(900, self.load_next_word)

    def _on_wrong(self, skip_next=True):
        self._stop_timer()
        self.streak = 0
        self.wrong_cnt += 1
        self._update_score_display()
        self.lbl_feedback.config(text=f"✗  Answer: {self.cur_answer}", fg=RED_WRONG)
        self.card.configure(highlightbackground=RED_WRONG)
        self._flash_card(RED_WRONG)
        if skip_next:
            self.root.after(1600, self.load_next_word)

    def _flash_card(self, color, n=4):
        if n <= 0:
            return
        current = self.card.cget("highlightbackground")
        next_col = CARD_BG if current != CARD_BG else color
        self.card.configure(highlightbackground=next_col)
        self.root.after(100, lambda: self._flash_card(color, n - 1))

    def _update_score_display(self):
        self.lbl_streak.config(text=f"🔥 {self.streak}")
        self.lbl_score.config(text=f"✅{self.correct_cnt}  ❌{self.wrong_cnt}")

    # ─────────────────────────────── HINT ────────────────────────────────────

    def give_hint(self):
        target = self.cur_answer.lower()
        # strip leading verb/article for hint reveal
        base = target
        if target.startswith("to "):
            base = target[3:].strip()
        else:
            for art in ("der ", "die ", "das ", "den ", "dem ", "ein ", "eine "):
                if target.startswith(art):
                    base = target[len(art):]
                    break
        self.hint_idx += 1
        if self.hint_idx <= len(base):
            revealed = base[:self.hint_idx]
            hidden   = "•" * (len(base) - self.hint_idx)
            self.lbl_feedback.config(text=f"💡  {revealed}{hidden}", fg=GOLD)
        else:
            self.lbl_feedback.config(text=f"Answer: {self.cur_answer}", fg=GOLD)

    # ─────────────────────────────── ARCHIVE ─────────────────────────────────

    def mark_done(self):
        if self.cur_de and self.cur_de not in self.known_words:
            self.known_words.append(self.cur_de)
            self.save_progress()
            self.load_next_word()

    def restore(self):
        if messagebox.askyesno("Reset Progress",
                               "Remove ALL archived words and start fresh?"):
            self.known_words  = []
            self.correct_cnt  = 0
            self.wrong_cnt    = 0
            self.streak       = 0
            self._update_score_display()
            if os.path.exists(self.data_file):
                os.remove(self.data_file)
            self.load_next_word()


if __name__ == "__main__":
    root = tk.Tk()
    app  = VocabMasterApp(root)
    root.mainloop()
