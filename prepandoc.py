#!/usr/bin/env python

'''
A filter to fixup and modify some of the latex book content before piping
into pandoc for conversion to epub and html formats (and others).

Basic things to do:
 - pandoc can't handle \input, so we handle those here
 - clean up some of the command markup to play nicely with what pandoc wants
'''

import re
import sys

def spitinput(inpfile):
    inptext = None
    inpfile = inpfile + '.tex'
    try:
        with open(inpfile) as inf:
            inptext = inf.read()
    except:
        print >>sys.stderr,"Can't open {}".format(inpfile)
    return inptext    

def checkinput(s):
    mobj = re.search('\\input{(\S+)}', s)
    if mobj:
        inpfile = mobj.groups()[0]
        return spitinput(inpfile)

    mobj = re.search('\\label{\S+}', s)
    if mobj:
        return ' '

    mobj = re.search('\\includegraphics{(\S+)\.eps}}', s)
    if mobj:
        return '<img src="' + mobj.groups()[0] + '.png">\n'

    return None

def findreplace(fstr, repl, fullstr):
    i = 0
    while True:
        i = fullstr.find(fstr, i)
        if i == -1:
            break
        fullstr = fullstr[:i] + repl + fullstr[i+len(fstr)+1:]
    return fullstr

def cleanotherstuff(s):
    s = findreplace('{\\bf','\\textbf{', s)
    s = findreplace('{\\tt','\\texttt{', s)
    s = findreplace('{\\em','\\textit{', s)
    return s

def main():
    inptext = ''
    for line in sys.stdin:    
        x = checkinput(line)
        if x:
            inptext += x
        else:
            inptext += line
    inptext = cleanotherstuff(inptext)
    print inptext

main()
