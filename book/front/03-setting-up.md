# Setting up: from paper to Python

You can start this book with nothing but a pencil. Each later grade adds one tool. Choose the level that matches your
school; every chapter has a version for lower levels.

| Level | What you need | Enough for |
|---|---|---|
| **0. Paper** | notebook, pencil, ruler, graph paper, calculator | all of Grade 8; the Track A parts of Grades 9–12 |
| **1. Spreadsheet** | any computer or phone with LibreOffice Calc, Google Sheets or Excel | Grade 9 Units 1–2, 7; many exercises |
| **2. CODAP** | a web browser (internet for first load) | graphing and exploring in Grades 8–9 |
| **3. Python in the browser** | JupyterLite (works offline once loaded, or from the school bundle) | Grades 9–12 notebooks |
| **4. Python on a computer** | Python 3.10+, pandas, matplotlib, scikit-learn, Jupyter | everything, including Streamlit and Git |

## Level 0: paper

Keep one notebook for the whole year. Draw tables with a ruler; use graph paper for charts. A cheap calculator with
square root is enough. The Grade 8 worksheets in `curriculum/grade-08/unit-01-what-is-data/worksheets/` can be printed.

## Level 1: spreadsheet

* **LibreOffice Calc** — free, works offline, available in English and Nepali interfaces (<https://www.libreoffice.org>).
* **Google Sheets** — free with a Google account; needs internet.
* **Microsoft Excel** — if your school has it.

All formulas in this book (`SUM`, `AVERAGE`, `COUNTIF`, `SUMIF`, `VLOOKUP`, pivot tables) work in all three. To open a
CSV file: File → Open, choose the file, and in the import window choose "comma" as the separator and UTF-8 as the
character set (so that Nepali text displays correctly).

## Level 2: CODAP

**CODAP** (Common Online Data Analysis Platform, <https://codap.concord.org>) is a free tool from the Concord Consortium
for exploring data by dragging: drop a CSV file onto the page, make a graph, drag a column to an axis. No account is
needed. It is ideal for Grade 8 and for anyone who wants to *see* data before coding.

## Level 3: Python in the browser (JupyterLite)

**JupyterLite** runs Python (through Pyodide) entirely inside your web browser: no installation, no server. The project
website hosts a JupyterLite copy of every notebook with the shipped datasets.

1. Open the project website's **Lite** link (or the `lite/` folder of the offline bundle opened with a local web
   server).
2. Open a notebook from `curriculum/grade-XX/unit-…/notebooks/`.
3. Press **Shift + Enter** to run each cell.
4. The first time, the browser downloads Python and pandas (tens of megabytes); after that it is cached.

If a library is missing, run in the first cell: `%pip install pandas matplotlib scikit-learn`.

**Colab** (Google's free notebooks) also works with any notebook from the repository, but needs a Google account and a
good internet connection.

## Level 4: Python on your own computer

1. Install Python 3.10 or newer from <https://www.python.org> (tick "Add Python to PATH" on Windows), or install
   Miniconda/Anaconda.
2. Download the curriculum (the GitHub "Download ZIP" button, or `git clone` the repository).
3. In a terminal, inside the folder:

```bash
python -m venv .venv
```

   then activate it (`.venv\Scripts\activate` on Windows, `source .venv/bin/activate` on macOS/Linux) and install:

```bash
pip install -r requirements.txt jupyterlab
```

4. Start Jupyter with `jupyter lab` and open any notebook.
5. For Grade 10 Unit 7 dashboards: `pip install -r curriculum/grade-10/unit-07-dashboards-with-streamlit/requirements-streamlit.txt`
   and `streamlit run app/air_dashboard.py` inside that unit's folder.
6. For Grade 11 Unit 8: install Git from <https://git-scm.com>.

An old laptop with 4 GB of RAM is enough for everything in this book.

## Schools without internet: the offline bundle

On any computer with internet, a teacher can build a **school bundle** (curriculum, synthetic datasets, licences, and
JupyterLite if built) and copy it to USB sticks:

```bash
python tools/build_offline_bundle.py
```

The result, `dist/school-bundle.zip`, can be copied to every computer in a lab. Real datasets for the exercises can be
downloaded once (Appendix A gives the links and licences) and copied the same way, as long as their licences allow it.

## Getting data files

* **Synthetic practice tables** are in `datasets/<name>/clean/` — for example
  `datasets/census-districts/clean/districts_synthetic.csv`. In this book, code reads them by file name
  (`pd.read_csv("districts_synthetic.csv")`): copy the CSV next to your notebook, or use the notebook's `data_file()`
  helper, which finds it automatically.
* **Real datasets** — see Appendix A. Some (World Bank, OWID, USGS, Open-Meteo, NASA POWER) can be read directly from a
  URL in Python; others (Open Data Nepal, ICIMOD) are downloaded from their web pages.

## If something goes wrong

| Problem | Likely cause | Fix |
|---|---|---|
| `FileNotFoundError` | the CSV is not where the code looks | put the file next to the notebook or give the full path |
| `ModuleNotFoundError: No module named 'pandas'` | library not installed in this environment | `pip install pandas` (or `%pip install pandas` in JupyterLite) |
| Nepali text shows as `???` or boxes | wrong character encoding or font | open/save CSVs as UTF-8; install a Devanagari font such as Noto Sans Devanagari |
| `HTTP Error 403` when reading a URL | the website blocks scripts | add a browser-like user agent (Appendix A, RD-02) or download the file manually |
| The notebook gives different numbers from the book | different random seed or data version | check `random_state`/seed; check the data file's date |
| Everything is slow | very large file or old computer | load fewer columns (`usecols=`), use smaller types (Grade 11 Unit 1) |
