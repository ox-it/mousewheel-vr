runningtotal=0
def shouldAdvanceFrame(extracount):
    runningtotal+=extracount
    if runningtotal>50:
        runningtotal-=50
        return True
    else:
        return False
    
extraCount = 8      #receive from programme
result = shouldAdvanceFrame(extraCount)

if result is True:
    video.gotonextframe()
else:
    satisfiesprogramme=0   #here only to fill up 'else' block
