#!/usr/bin/env python
from PIL import Image
from argparse import ArgumentParser
from numpy import zeros
import sys

parser = ArgumentParser(description='Find the location of colored dots in an image')
parser.add_argument('filename',help='Filename of a PNG image to process',metavar='FILENAME')
parser.add_argument('--spotsize',help='Minimum number of contiguous pixels that constitute a dot',type=int,default=10)
parser.add_argument('--verbose','-v',action='count')
parser.add_argument('--output-image',help='If specified, writes an output image with the found centers marked.  If a filename is provided, it will write to that file, otherwise it will overwrite the original.',default=None,required=False,metavar='FILENAME')
args = parser.parse_args()
im = Image.open(args.filename)

try:
    debug = parser.verbose > 0
except AttributeError:
    debug = False

try:
    output_file = args.output_image
    if output_file == None: output_file = args.filename
except AttributeError:
    output_file = False

havehit = zeros(im.size,bool)
pix = im.load()
spotlist = []
searchlist = [(0,-1),(1,0),(0,1),(-1,0)]

def addpoint(p1,p2):
    return (p1[0] + p2[0],p1[1]+p2[1])

def findspot(point,prefix = ' '):
    if debug: print >> sys.stderr,  (x,y)
    try:
        if(havehit[point]):
            if debug: print >> sys.stderr,  prefix + 'Already hit this one.'
            return False
    except IndexError:
        if debug: print >> sys.stderr,  prefix + 'Index out of bounds.'
        return False

    havehit[point] = True
    (R,G,B) = pix[point]
    # If the pixel is predominantly green
    if(G - (R + B) > 100):
        if debug: print >> sys.stderr,  prefix + 'Found point, trying neighbors...'
        pointweight = point
        count = 1
        for add in searchlist:
            foundspot = findspot(addpoint(point,add), prefix + ' ')
            if foundspot:
                (pw, c) = foundspot
                pointweight = addpoint(pointweight,pw);
                count += c;

        return (pointweight, count)
    else:
        if debug: print >> sys.stderr,  prefix + 'This one\'s not colored.'
        return False

for x in range(im.size[0] - 1):
    for y in range(im.size[1] - 1):
        foundpoint = findspot((x,y))
        if foundpoint:
            (pointweight, count) = foundpoint
            if count >= args.spotsize:
                csvline = (pointweight[0] / count,pointweight[1]/count,count)
                print "%d,%d,%d" % csvline
                if output_file:
                    pix[csvline[:2]] = (255,0,255)

if output_file:
    im.save(output_file)

