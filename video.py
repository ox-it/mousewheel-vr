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

# Initialise video
omx = OMXPlayer('smaller.mp4', None, start_playback=False)

# Create event handler and subscribe to event
def handleEvent(count):
    print "got an event!"
    if shouldAdvanceFrame(count):
    	omx.step()
	#print "step!"

#subscribe to events
zope.event.subscribers.append(handleEvent)

print "subscribed"

time.sleep(1)

#Start up the mock
thread = Thread(target=mock)
thread.start()


#kill the video after too long
time.sleep(100)
omx.stop()