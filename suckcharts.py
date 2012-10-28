import re
import sys
import urllib

baseurl = 'http://chart.apis.google.com/chart?cht=tx&chl='
outdir = 'tpimg'
seqnum = 0

def process_line(line, pattern, slice, seqnum):
    while True:
        mobj = re.search(pattern, line)
        if not mobj:  
            break
        innertex = mobj.groups()[0][slice:-slice]
        remoteurl = baseurl + innertex
        outfilename = "tpimg/eqn_%02d.png" % (seqnum)
        print >>sys.stderr, seqnum, remoteurl
        urllib.urlretrieve(remoteurl, filename=outfilename)
        seqnum += 1
        imglink = '![' + innertex + '](' + outfilename + ')'
        line = line[:mobj.start()] + imglink + line[mobj.end():]
    return line, seqnum


for line in sys.stdin:
    line = line.strip()
    line, seqnum = process_line(line, '(\$[^\$]+\$)', 1, seqnum)
    line, seqnum = process_line(line, '(\$\$[^\$]+\$\$)', 2, seqnum)
    print line

