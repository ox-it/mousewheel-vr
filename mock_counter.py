#video=about 30 frames per second
import time
import random
import zope.event

def mock():
	import time

	print "STARTING MOCK"

	minincrement=-2
	maxincrement=3
	increment=0
	
	# Use a smaller count for testing purposes
	#maxcount=45000
	maxcount=5000
	
	dist=0 #in metres
	count=0
	timeinterval=1.0/120.0
	print timeinterval
	while count<maxcount:  
  	  #waits 1/120 seconds(time between each check)
  	  time.sleep(timeinterval)
  	  #bias the incrementdelta when limit is approached
  	  if increment>10:
   	     maxincrement=1
  	  if (maxincrement<3 and increment<10):
 	       maxincrement=3
 	  if increment<3:
 	       minincrement=-1
 	  if (minincrement>-2 and increment>3):
 	       minincrement=-2
  	  incrementdelta=random.randrange(minincrement,maxincrement)
  	  #sets new increment to last increment + incrementdelta
  	  newincrement=increment+incrementdelta
   	  #checks if newincrement is bigger than 12 or smaller than 0
   	  while (newincrement>12 or newincrement<0):     
   	     if newincrement>12:     
     	       newincrement=12   
    	     else:   
     	       newincrement=0    
    	  #print("random increment was outside acceptable range, set newincrement to:", newincrement)  #alerts us that new increment is outside acceptable range
 	  #set increment to newincrement
   	  increment=newincrement
  	  #changes count by increment
  	  count=count+increment       
   	  #print(count, "increment:", increment)    #prints count
  	  #time.sleep(0.25)    #gives us time to read the value of count

	  #   create event with count
	  zope.event.notify(increment)
	print "Reached maximum count"
	zope.event.notify(-1)
