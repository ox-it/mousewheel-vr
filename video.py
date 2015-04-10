from pyomxplayer import OMXPlayer
import time
import zope.event
from mock_counter import mock
from threading import Thread

# Keep track of running total count since last frame increment
# TODO - the method can't see runningtotal. Put all this in a class.

#method to decide whether to increment frame
def shouldAdvanceFrame(extracount):
    shouldAdvanceFrame.runningtotal+=extracount
    if shouldAdvanceFrame.runningtotal>50:
        shouldAdvanceFrame.runningtotal-=50
        return True
    else:
        return False

shouldAdvanceFrame.runningtotal=0


# Create event handler and subscribe to event
def handleEvent(count):
    #print "received count", count
    if count < 0:
	# We've reached the end of the input
	print "Finished. Total frames: ", handleEvent.numFrames
	omx.toggle_pause()
	omx.stop()
    
    elif shouldAdvanceFrame(count):
    	omx.step()
	blah =1
	handleEvent.numFrames += 1
handleEvent.numFrames = 0


# Initialise video
omx = OMXPlayer('smaller.mp4', '--no-osd', start_playback=False)

# Get the video started, then wait a short while before beginning the mock thread
omx.step()
time.sleep(1)	

#subscribe to events
zope.event.subscribers.append(handleEvent)
print "subscribed"

#Start up the mock
thread = Thread(target=mock)
thread.start()