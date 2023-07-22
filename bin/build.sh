#!/bin/bash






# python3 ../src/zot/zot.py


pdflatex \
    -output-directory=../src/pdf/ \
    -output-format=pdf \
    -file-line-error \
    ../src/tex/main.tex