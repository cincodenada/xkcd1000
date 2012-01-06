#Summary
My ultimate goal is to have a website where users can click on a person in the image and add notes to it - perhaps associate it with a comic number that it references, or just add commentary.  That's not even started yet, but the first step of that is to know where the people are.  

#What's done so far
Thanks to the [Google+ discussion](https://plus.google.com/111588569124648292310/posts/j6w9DkYApya), I had an image with 100 of the 102 people marked with green dots.  I found the two missing people based on Randall's comments, and filled them in, which resulted in the xkcd_1000_preproc_fixed.png, based on [Carsten Orthbandt's](https://plus.google.com/100130718459580387989) original image.  
To get the dots into machine-readable form, I wrote a Python script to find all the dots and their centers.  I know it's a script that's been written a million times and much more efficient than this, but I needed an excuse to brush up on my Python anyway, and this works splendidly.  It's not the best code I've ever written or the most efficient possible, but it did its job.
##Script details
You feed the script an image with green dots in it, and it spits out a CSV stream and, optionally, an image.
* The output image (xkcd_marked.png here) is a modified version of the input image that has pink pixels showing where it found the centers of the dots
* The output CSV stream (piped to pointlist.csv here) is a list of `x,y,dotsize`, where `dotsize` is the number of pixels that make up the dot, and `x` and `y` are the coordinates for the center of the dot.

#What's Next
The next step from here, of course, is to hack together some HTML5/JS that lets you click on the original image, it finds the closest pixel in the list or some such, and then lets you notate that person (give it a title, etc).  I've got real work to do right now, so that won't get done for a while, but if anyone else wants to jump in, feel free!  All this is CC-BY-NC just like xkcd.
