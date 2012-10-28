#!/bin/bash -x

for file in book.css book.js cosc101-solvingproblemswithpython.html cosc101-solvingproblemswithpython.pdf cosc101-solvingproblemswithpython.epub figs
do
    scp -r ${file} jsommers@cs.colgate.edu:~/public_html/cosc101
done
