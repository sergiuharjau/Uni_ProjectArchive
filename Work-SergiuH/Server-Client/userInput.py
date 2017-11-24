
import sys,time

def emotionHandler(message):
  """Takes the user's message and outputs a response"""
  emotions=["afraid","angry","sad","disgusted","happy","surprised","eager","okay","good","fine"]
  i=-1
  sentMsg=""
  for word in emotions:
    i+=1
    if i <4:
      if word in message:
        if "?" in message:
          sentMsg="No, I'm actually quite fine, thank you :)"
        else:
          sentMsg="I am sorry you are " + str(emotions[i]) +" :("
    elif i>=4:
      if word in message:
        if "?" in message:
          sentMsg="Yeah, sure am!"
        else:
          sentMsg="Glad you're feeling " + str(emotions[i]) +"!"
    if sentMsg=="":
      sentMsg="Sorry, we haven't coded that in yet. :/"
      v=1
    
  return(sentMsg) 


def slow_type(message):
    typing_speed = 170 #wpm
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(10.0/typing_speed)
    print ("")

