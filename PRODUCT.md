# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

The owner, a long-term buy-and-hold investor, using it alone. Design decisions serve this one reader first.

Two secondary audiences exist but don't drive design: people who publish their own copy from this repo, and people who open the owner's shared link. Shared-link viewers get their own private data but can't use "Ask Claude to refresh prices", so they type prices in by hand.

## Product Purpose

A daily habit: short, specific lessons about the companies on the reader's watchlist (founders, origin stories, products, management, milestones), each rated 1–5. Ratings steer what Claude writes next. Around that core sit the Lens (the watchlist through value-investing questions), a watchlist with a user-set buy rule, highlights and notes, follow-up questions to Claude, and Insights on rating trends.

Success: the reader keeps the habit, understands the watchlist's businesses better over time, and builds a searchable record of what they highlighted and asked.

## Positioning

The lessons are about the reader's own watchlist, written by Claude, and tuned by the reader's own ratings, while about one in three still explores a less-tried category. Follow-ups answer questions about a specific highlighted passage, with the card and price snapshot as context. Everything stays private to the reader.

## Operating Context

- Phone for the daily read: open Lessons, read two lessons, rate them, maybe highlight.
- Desktop for the slower work: Notes, Watchlist, follow-ups, Insights and exports.
- Runs inside claude.ai as a published artifact. It's shipped by re-publishing `app/index.html` from a claude.ai chat.
- Prices come from a snapshot, never live. "Ask Claude to refresh prices" posts a comment to the chat watching the artifact, and Claude writes the snapshot; or the reader types prices in.
- Notes export as Markdown or HTML. The owner's full data is exported through a claude.ai chat into a separate private repo.

## Capabilities and Constraints

- One HTML file with no build step and no framework. Fonts come from Google Fonts. No network access.
- Depends on the artifact runtime (`window.claude`): `db`, `user`, `sample`, `comments`, `downloads`. Each one is optional; when one is missing, the page says what's unavailable and keeps working.
- Tabs: Lessons, Lens, Watchlist, Insights, Notes.
- Newest first everywhere. "Show 2 more" sits at the top. Past days are read-only for generation.
- Highlights and threads anchor to `[data-field]` names (`title`, `body`, `take`, `headline`, `sec:<key>`, `questions`). These names must stay stable.
- Follow-up answers stay under 80 words: one sentence plus at most three bullets.
- Lens sections: competence, moat, management, margin (of safety), invert, ten-year.
- Terms: lesson, lens card, rating, star, highlight, note, follow-up, buy rule, price snapshot, watchlist.
- Testing is Playwright with `sample`, `downloads` and the `days`, `lens` and `market` state stubbed.

## Brand Commitments

- Name: Compound Lessons.
- Voice: concise. UI text and answers are short.
- "Not financial advice" stays visible where prices and the buy rule appear.
- The visual conventions listed in `CLAUDE.md` are the current identity. One rule there is an identity constraint, not a style choice: no Japanese text in the UI.

## Evidence on Hand

- Screenshots: `docs/screenshots/lessons-light.png`, `docs/screenshots/lessons-dark-mobile.png`.
- Prompts: `docs/PROMPTS.md`, generated from the app.
- History of the build: `CHANGELOG.md`.
- Absent, and not to be invented: user counts, testimonials, returns or performance claims of any kind.
- The owner's real data lives in a private repo and never appears here, in screenshots, or in sample content.

## Product Principles

1. Specific over broad. One concrete fact per lesson, with names, years and numbers; say so when unsure.
2. The reader chooses depth. Short by default; more only when they ask for it, through "Show 2 more" or a follow-up.
3. Education, not advice. No buy, sell or hold calls, price targets or predictions. The buy rule is visibly arithmetic on the reader's own settings.
4. The reader's record is the product's memory. Ratings, highlights, notes and threads must never be lost or come loose from their anchors.
5. Degrade in the open. When a capability is missing, explain it and keep the rest working.

## Accessibility & Inclusion

- Every icon button has a label.
- Motion respects `prefers-reduced-motion`.
- Light and dark mode are both first-class; the reader toggles between them.
