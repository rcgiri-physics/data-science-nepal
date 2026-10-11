# 7. Teaching in low-resource classrooms

Most schools in Nepal do not have a well-equipped computer lab with reliable internet. This curriculum was designed for
that reality. This chapter collects practical strategies.

## No computers at all

* **All of Grade 8** and the Track A versions of later units work on paper: tallies, tidy tables on the board,
  hand-drawn graphs, calculators.
* **Printed extracts:** print 10–30 rows of a dataset per group (the synthetic tables are small). Students compute
  summaries by hand, then you reveal the full-table result computed in advance (this book gives them).
* **Unplugged versions** of computational ideas:
  * SQL: one student is the "database" holding district cards; others call out queries.
  * Sorting and median: the "human median" line-up.
  * k-NN: cards on a grid, a ruler for distance.
  * Bootstrap: draw slips with replacement from a bag.
  * Permutation test: shuffle outcome cards between two piles.
  * Overfitting: "memorise last year's paper" role play.
* **Paper spreadsheets:** grid paper with column letters and row numbers teaches cell references and formulas before
  anyone touches a computer.

## One computer and a projector

The teacher (or a rotating student) runs the notebook; everyone else predicts on paper first. This is surprisingly
effective with PRIMM. Use large fonts (`Ctrl +`).

## A small lab (5–15 computers)

Groups of three with roles (driver, navigator, data steward); station rotation with paper activities.

## No or unreliable internet

* Build the **offline school bundle** once (`python tools/build_offline_bundle.py`) and copy it to every computer by USB.
* Pre-download real datasets for the year's exercises in a single trip to an internet connection (respect licences:
  most listed in Appendix A allow classroom copies with credit).
* JupyterLite caches Python after the first load; open it once while online.

## Power cuts

* Keep a paper version of every computer activity (each teacher guide has one).
* Save work often; teach Git (Grade 11) partly because it makes losing work less likely.
* Laptops on battery and phones can keep a small group going.

## Large classes (50+)

* Groups of five with roles; one shared table per group.
* Mini-whiteboards (or slates, or A4 sheets in plastic sleeves) so every student answers Check questions at once.
* Gallery walks instead of presentations: posters on the wall, groups rotate and leave sticky-note feedback.
* Peer marking with the rubric; teacher samples and moderates.

## Multi-grade classes and one-teacher schools

* Same theme, different depth (see chapter 3).
* Older students as data stewards and mentors.
* Shared class dataset for the whole school (e.g. travel to school), analysed at different levels.

## Low cost materials list

| Item | Use |
|---|---|
| graph paper, rulers, coloured pencils | graphs, maps |
| index cards / cut paper slips | sorting, sampling, shuffling, SQL cards |
| a cloth bag or box | random draws |
| dice | random numbers, simulations |
| a stopwatch (phone) | measurement activities |
| tape measure, kitchen scale, thermometer, rain gauge (a straight-sided bottle) | collecting real measurements |
| sticky notes | feedback, gallery walks |

## Equity and access

* Do not make phone or internet access a requirement for homework; always offer the offline fallback.
* Rotate access to computers fairly; track who has used them.
* Watch that boys don't monopolise the keyboard: assign driver roles deliberately.
