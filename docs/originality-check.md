# Originality check — 2026-10-12

## Method
- **Pattern scan** of all 170 Markdown files in `book/` and `curriculum/` for long quoted passages (60+ characters),
  well-known stock phrases from statistics textbooks, and famous textbook examples (Anscombe's quartet, Simpson's
  paradox, Titanic, Gapminder and others).
- **Book list review:** the descriptions in `book/beyond/03-books.md` were read to make sure they are short, in our
  own words and not copied publisher blurbs.
- **Web spot-check** of distinctive sentences (a sampling definition and the Anscombe's quartet description) for
  exact-phrase matches.

## Result
- **Quoted passages:** all are project-written examples (Nepali census questions, class surveys, "spot the flawed
  claim" items, teacher prompts). None are quotations from other works.
- **Stock phrases:** none found.
- **Famous examples:** credited where used. Anscombe (1973) and the Datasaurus Dozen (Matejka & Fitzmaurice, 2017)
  are cited in [THIRD_PARTY.md](../THIRD_PARTY.md); Gapminder and Hans Rosling are named and linked.
- **Web spot-check:** no exact-phrase matches. Other sites explain the same ideas in different words, which is
  expected for standard concepts.
- **Fix made:** Anscombe's correlation is now written as *r* ≈ 0.82 (exact value 0.816).

## Limits
This was a targeted check, not an automated comparison of every sentence against other textbooks. Paid books,
courses and close paraphrase would not be caught. Ideas and standard explanations are not copyrightable, but sources
the lessons follow should still be credited in [THIRD_PARTY.md](../THIRD_PARTY.md). Please report anything that
looks uncredited by opening an issue.
