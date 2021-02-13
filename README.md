# trichromatic_merger
Bash/Python script to call libraw and image magick for the linearization and merging of raw files into trichromatic tiffs. To use together with G2P. Although G2P already does this, Photoshop writes the files to be merged as temporal files in the disk, deleting them afterwards. While the approach works, I find it puts too much strain on the SSD memory of my laptop (with limited writing/deleting cycles) and to extending, my goal is to find a way to do so with temporal files being written into the RAM memory. 

One reference link: https://unix.stackexchange.com/questions/329886/imagemagick-graphicsmagick-how-to-merge-composite-multiple-3-images-without

The main keypoints are:
- Writing the frams to RAM, not SSD
- Multiprocessing would be amazing
- GPU?

Python has de *wand* module that seems promising. I'm sure that for a folder with all files aready, it could be possible to multiprocess the whole thing and obtain the linearized and merged 3chromes directly from the terminal. 
