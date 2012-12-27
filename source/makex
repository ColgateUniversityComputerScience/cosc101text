BOOKNAME = cosc101-solvingproblemswithpython

# all book chapters, in the order in which they're assembled into 
# the various final products.

INPTEXT = book.txt wayofprogram.txt varexpr.txt usingfunctions.txt conditionals.txt functionsindepth.txt programdesign.txt iteration.txt strings.txt recursion.txt fileio.txt lists.txt dictionaries.txt tuples.txt datastruct.txt oo.txt search.txt sort.txt debugging.txt postfix.txt

# JS: removed tkinter.txt.  it doesn't add anything particularly
# fundamental and uses the odd and semibroken gui.py.

all: html epub pdf

html:
	cat ${INPTEXT} | pandoc -t html -H header.html --webtex --standalone --smart --css=book.css --number-sections --table-of-contents --section-divs --indented-code-classes=python -o ${BOOKNAME}.html

epub: 
	cat ${INPTEXT} | pandoc -t epub --webtex --self-contained --table-of-contents --smart --section-divs --indented-code-classes=python --epub-cover-image=epubcover.png -o ${BOOKNAME}.epub
	python patchebookfigs.py ${BOOKNAME}.epub

pdf:
	cat ${INPTEXT} | pandoc -t latex -H header.tex --table-of-contents --number-sections -o ${BOOKNAME}.tex
	pdflatex ${BOOKNAME}
	pdflatex ${BOOKNAME}



tidy:
	rm -f *~
	rm -f ${BOOKNAME}.aux
	rm -f ${BOOKNAME}.out 
	rm -f ${BOOKNAME}.log 
	rm -f ${BOOKNAME}.toc 
	rm -f ${BOOKNAME}.tex 

clean:
	rm -f ${BOOKNAME}.* *~
