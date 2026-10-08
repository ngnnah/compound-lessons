# Changelog

How the app grew, roughly in order.

- **Daily lessons:** three tickers a day, 1–5 ratings, history by date, rating-based personalization.
- **Batches:** two lessons to start, then "Show 2 more" as often as you like.
- **How it's doing:** price snapshot on each card and a user-set buy rule ($1,000–$10,000 by default).
- **Price refresh:** a manual price form, then an "Ask Claude to refresh prices" button using artifact comments.
- **Fixes:** frozen db objects broke appends after a reload. Data is now deep-copied on load. Errors are visible, with details and a retry.
- **Design:** seigaiha waves, ōgi fans and uroko triangles, Instrument Serif and Figtree, and a light/dark toggle.
- **Readable lessons:** short paragraphs plus bullets, with round bullets that don't look expandable.
- **Tabs:** Lessons, Watchlist (prices and buy rule merged) and Insights. Past days are read-only.
- **Notes:** highlights in three colors, notes, a Notes tab with search and filters, and Markdown/HTML export.
- **Lens:** watchlist cards through value-investing questions, with section stars, ratings and history.
- **Notes on Lens cards**, plus Lessons/Lens filters.
- **Follow-ups:** ask Claude about a passage or a card, with concise answers, stored threads and export.
- **Ordering:** newest lessons and lens cards first, the "Show more" button at the top, and notes sorted by latest activity.
