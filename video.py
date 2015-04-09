from pyomxplayer import OMXPlayer
import time
import zope.event

omx = OMXPlayer('smaller.mp4', None, start_playback=True)

time.sleep(0.5)

#paused
omx.toggle_pause()

count = 0
while(count<100):
    omx.step()
    time.sleep(0.1)
    count+=1

omx.stop()