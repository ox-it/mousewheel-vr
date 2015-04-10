# mousewheel-vr

## Installation

Clone repository via

    git clone https://github.com/ox-it/mousewheel-vr.git

Install popcornmix/omxplayer, following the instructions at https://github.com/popcornmix/omxplayer
This is a branched version of omxplayer which provides an interface for single frame stepping


Install pip if needed

    sudo apt-get install python-pip

Install pexpect, zope.event

    pip install pexpect
    pip install zope.event


## Running

Open a terminal in the mousewheel-vr folder and run

    python video.py

This will launch the mock counter and run the video based on its output. The video will be terminated when the counter finishes.
