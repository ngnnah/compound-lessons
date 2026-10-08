# Architecture

One self-contained HTML file (`app/index.html`): CSS, markup and plain JavaScript, with no build step and no framework. Fonts load from Google Fonts. The seigaiha, fan and uroko patterns are SVG generated in JavaScript from the current theme's colors and re-drawn when the theme changes.

## Runtime capabilities

The page runs as a Claude published artifact and uses these runtime capabilities:

| Capability | Used for |
| --- | --- |
| `db` | Saving lessons, lens cards, ratings, notes, threads, settings and the price snapshot |
| `user` | Addressing the viewer's private rows (`data/users/<id>`) |
| `sample` | Asking Claude to write lessons, lens cards and follow-up answers |
| `comments` | The "Ask Claude to refresh prices" button, which sends a comment to the Claude chat watching the artifact |
| `downloads` | Exporting notes as `.md` or `.html` |

Every capability is optional at runtime. When one is missing, the page explains what's unavailable and keeps working where it can.

## Data model

Everything lives in one private collection per viewer, `data/users/<viewer-id>`:

| Document | Shape |
| --- | --- |
| `settings` | `{ watchlist: string[], rule: { min, max, fullAt, earningsDays } }` |
| `market` | `{ asOf, source, quotes: { TICKER: { price, high52, low52, pe, oneYearPct, nextEarnings, asOf? } } }` |
| `day_YYYY-MM-DD` | `{ date, tickers, lessons[], ratings[], annotations[], threads[], createdAt }` |
| `lens_YYYY-MM-DD` | `{ date, order, cards[], ratings[], stars[][], annotations[], threads[], createdAt }` |

- **Lesson:** `{ ticker, company, category, title, body, takeaway }`. `body` uses plain lines, and lines starting with `- ` render as bullets.
- **Lens card:** `{ ticker, company, headline, sections: { competence, moat, management, margin, invert, tenyear }, questions[] }`.
- **Annotation:** `{ id, li, field, start, end, quote, color, note, at, edited? }`. `li` is the card index. `field` is `title`, `body`, `take`, `headline`, `sec:<key>` or `questions`, and it's `null` for a whole-card note. Offsets are re-anchored by searching for `quote` if the text shifts.
- **Thread:** `{ id, li, field, start, end, quote, messages: [{ role, text, at }], at }`.

Data read from `db` comes back frozen, so the page deep-copies it before treating it as mutable state.

## Generation

- **Lessons:** two per batch, rotating through the day's three tickers. The prompt includes the rating profile (averages by category and ticker, loved and disliked titles) and recent titles to avoid repeats. Replies are parsed tolerantly, and a failed parse retries once.
- **Lens:** two cards per batch, rotating through the whole watchlist from a date-based starting point. Starred sections get more depth. Guardrails: no invented quotes, no claims about what Buffett or Munger think of a specific company, nothing about Berkshire's holdings, no buy, sell or hold calls.
- **Follow-ups:** a multi-turn `sample` call. The first user turn carries the instructions, the card text, the highlighted passage and the price snapshot. Answers are capped at about 80 words: one sentence plus at most three bullets.

See [PROMPTS.md](PROMPTS.md) for the exact text.

## Prices

The page can't reach the internet. Prices arrive in two ways:

1. **Refresh button:** posts a comment to the artifact asking Claude to refresh. Claude looks up the latest closes in the chat and writes the `market` document. The page subscribes to that document and updates live.
2. **Manual entry:** the "Enter a price yourself" form writes the same document.

## Buy rule

`amount = min + (max − min) × clamp(belowHigh / fullAt, 0, 1)`, rounded to $50. The buy is split into two halves when earnings fall within `earningsDays`. It's arithmetic on the user's settings, not a prediction.
