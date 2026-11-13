# assets/code/log — scripts run by /log on 2026-11-13

- `make_final.py` (output `make_final.out`) derives `final/final.md` from `answers/answer-2.md`. It moves out §1 and §10, which become `sources/independence.md` and `audits/response-to-audit-1.md`, and redirects two cross-references.
- `extract_tags.py` (output `extract_tags.out`) lists every provenance tag in `final/final.md`; `sources/provenance.md` was built from that list.
- `make_assets.py` assembled `assets/code/`.
- `make_tex.py` with `tags.lua` builds `final/final.tex` with the house template. `latexmk.out` and `final.log` are the build output and the compile log.
- `latex_clean.py` (output `latex_clean.out`) is the report-only gate `latex_clean`. It changed nothing.
