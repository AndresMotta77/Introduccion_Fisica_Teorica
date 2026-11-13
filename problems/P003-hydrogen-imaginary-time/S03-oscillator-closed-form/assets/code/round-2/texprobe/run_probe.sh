#!/bin/bash
# run_probe.sh -- compile the two probes and report errors / missing characters.
# pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian). Run from texprobe/: bash run_probe.sh
for f in probe_house probe_auditor; do
  rm -f $f.aux $f.log $f.pdf
  pdflatex -interaction=nonstopmode $f.tex > /dev/null 2>&1
  echo "=== $f: PDF produced: $([ -f $f.pdf ] && echo yes || echo no)"
  echo "    TeX errors: $(grep -c '^!' $f.log); missing-character warnings: $(grep -c 'Missing character' $f.log)"
  grep '^l\.[0-9]' $f.log | sed 's/^/    error at /'
done
pdftoppm -r 110 -png probe_house.pdf probe_house
echo "rendered probe_house.pdf to probe_house-1.png (inspected visually)"
