import re
import os
import sys
import urllib
import zipfile


def get_img_object(remoteurl):
    fp = urllib.urlopen(remoteurl)
    filecontents = fp.read()
    fp.close()
    return filecontents


def copyfile(fname, inzip, outzip):
    outzip.writestr(fname,inzip.read(fname))


def writefile(fname, contents, outzip):
    outzip.writestr(fname, contents)


def main(ebookfile):
    seqnum = 0
    zipout = zipfile.ZipFile('tmp.zip','w',zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(ebookfile, 'r') as ebook:

        for fname in ebook.namelist():
            if '.xhtml' in fname:
                print >>sys.stderr, 'Processing',fname
                fp = ebook.open(fname)
                fullcontents = ''
                for line in fp:
                    while True:
                        mobj = re.search('\"(http://chart.apis.google.com/\S+)\"', line)
                        if not mobj:
                            break

                        fullurl = mobj.groups()[0]
                        fullurl = fullurl.replace('&amp;','&')
                        fullurl = urllib.unquote_plus(fullurl)
                        img = get_img_object(fullurl)

                        outfilename = "images/eqn_%02d.png" % (seqnum)
                        print >>sys.stderr, seqnum, outfilename, fullurl
                        writefile(outfilename, img, zipout)

                        line = line[:mobj.start()] + '"' + outfilename + '"' + line[mobj.end():]
                        seqnum += 1
                    fullcontents += line
                fp.close()
                writefile(fname, fullcontents, zipout)
            else:
                copyfile(fname, ebook, zipout)

    zipout.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
        os.unlink(sys.argv[1])
        # os.rename(sys.argv[1],sys.argv[1]+'.old')
        os.rename('tmp.zip',sys.argv[1])
    else:
        print >>sys.stderr, "Need a zip file name for the ebook."

