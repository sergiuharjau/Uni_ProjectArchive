import sys,time

#Taken from stackoverflow

def slow_type(message):
    """Print the input (a string) in a human-like way."""
    typing_speed = 170 #wpm
    for l in message:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(10.0/typing_speed)
    print ("")

