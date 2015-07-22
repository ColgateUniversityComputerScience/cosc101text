#!/bin/bash 
sphinx-build -b latex -d _build/doctrees . _build/xetex && pushd _build/xetex; xelatex spwpbook && xelatex spwpbook && xelatex spwpbook && popd
