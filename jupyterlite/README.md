# JupyterLite (Python in the browser, no install)

`python tools/build_site.py --lite` builds JupyterLite with the curriculum notebooks and shipped datasets into `site/lite`.

Requirements: `pip install jupyterlite-core jupyterlite-pyodide-kernel jupyter-server`.

## Notes
* The first load downloads Pyodide and pandas (reported > 70 MiB); on slow links, use the **offline bundle**
  (`python tools/build_offline_bundle.py`) — JupyterLite's offline how-to:
  <https://jupyterlite.readthedocs.io/en/latest/howto/configure/advanced/offline.html>.
* In the browser, install libraries once per session in the first cell: `%pip install pandas matplotlib scikit-learn`
  (or add them to a `jupyterlite_config.json` piplite wheel list for offline use).
* Notebooks find data by walking up from the working directory to a folder containing `datasets/`; the build stages
  `curriculum/` and `datasets/` side by side to make that work.
