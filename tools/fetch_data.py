"""Reproducibly download a real dataset from its ORIGINAL publisher and verify its checksum.

We never re-host real data in this repository. Each dataset folder has a source.yml:

    url: https://.../file.csv        # direct download link (maintainer fills in after checking the licence)
    filename: air_quality.csv
    sha256: ""                       # empty on first fetch; paste the printed value afterwards

Usage:  python tools/fetch_data.py <dataset-folder-name>
"""
from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    folder = ROOT / "datasets" / sys.argv[1]
    src = folder / "source.yml"
    if not src.exists():
        print(f"No {src.relative_to(ROOT)}")
        return 2
    cfg = yaml.safe_load(src.read_text(encoding="utf-8"))
    url = (cfg.get("url") or "").strip()
    if not url:
        print(f"source.yml has no direct 'url' yet. Open the landing page, check the licence, then paste the "
              f"download link:\n  {cfg.get('landing_page')}")
        return 1
    out = folder / "raw" / cfg["filename"]
    out.parent.mkdir(parents=True, exist_ok=True)
    print("downloading", url)
    with urllib.request.urlopen(url, timeout=60) as resp:  # noqa: S310 (https URL from reviewed source.yml)
        data = resp.read()
    digest = hashlib.sha256(data).hexdigest()
    expected = (cfg.get("sha256") or "").strip()
    if expected and digest != expected:
        print(f"CHECKSUM MISMATCH\n expected {expected}\n got      {digest}\nThe source changed; review before using.")
        return 1
    out.write_bytes(data)
    print(f"saved {out.relative_to(ROOT)}  sha256={digest}")
    if not expected:
        print("Paste this sha256 into source.yml so everyone gets identical data.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
