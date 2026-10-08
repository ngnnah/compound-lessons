# Compound Lessons: handoff

A daily investing-lessons app built as one HTML file that runs as a **Claude published artifact**. See `README.md` for features and `docs/ARCHITECTURE.md` for the runtime, data model and prompts.

## Repos
- `compound-lessons` (public): the app, docs and scripts. **No personal data, ever.**
- A separate private repo holds the owner's exported data. Never copy any of it into this repo.

## Where things are
- `app/index.html`: the whole app (CSS, markup, JS, prompts). No build step, no framework.
- Prompts live inline in the app. After editing one, run `python3 scripts/extract_prompts.py` to regenerate `docs/PROMPTS.md`.
- Tabs: Lessons, Lens, Watchlist, Insights, Notes.

## Runtime constraints
- **Claude runtime:** the app depends on `window.claude` capabilities (`db`, `user`, `sample`, `comments`, `downloads`). Opened locally, it loads but can't generate or save.
- **Testing:** load the file in Playwright and stub `sample`, `downloads` and the `days`, `lens` and `market` state, the way earlier sessions did.
- **Network:** the page has none. Prices come from the `market` doc, written by Claude in chat (the refresh button sends a comment) or entered by hand.
- **Frozen data:** `db` returns frozen objects. Deep-copy on load, which is already done; keep it that way.
- **Shipping changes:** re-publish the edited file from a claude.ai chat, updating the existing artifact.

## Conventions to keep
- **Highlight anchoring:** annotations and threads anchor to `[data-field]` elements by `start`/`end`/`quote`. Keep `data-field` names stable: `title`, `body`, `take`, `headline`, `sec:<key>`, `questions`.
- **Ordering:** newest first everywhere (cards, notes). "Show 2 more" sits at the top, and past days are read-only for generation.
- **Follow-up answers:** strictly concise, under 80 words, one sentence plus at most 3 bullets.
- **Lens guardrails:** no invented Buffett or Munger quotes or views on specific companies, nothing about Berkshire holdings, no buy, sell or hold calls.
- **Design:** indigo, washi and vermilion; seigaiha, fan and uroko patterns generated as SVG in JS; Instrument Serif plus Figtree; light/dark toggle; round dot bullets. **No Japanese text in the UI.**
- **Accessibility:** keep labels on icon buttons and support reduced motion.

## Owner preferences
Concise answers and UI text. Ship small, focused changes and verify them in Playwright before committing.
