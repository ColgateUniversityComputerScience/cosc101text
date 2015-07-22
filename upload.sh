#!/bin/bash -x

scp -r _build/html jsommers@cs.colgate.edu:~/public_html/cosc101
scp _build/xetex/spwpbook.pdf jsommers@cs.colgate.edu:~/public_html/cosc101
