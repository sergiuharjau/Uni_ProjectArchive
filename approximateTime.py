hour= input("What is the hour(24 hour format)? ")
if int(hour)<0 or int(hour)>24:
    print("Good try. I meant a real hour.")
    quit()
minutes= input("And how many minutes? ")
if int(minutes) <0 or int(minutes)>=60:
    print("Mate, are you even trying.")
    quit()
if (int(minutes)<7.5 and int(minutes)>0) or (int(minutes)<60 and int(minutes)>52.5):
    minutes=""
else:
    if (int(minutes)>7.5) and (int(minutes)<22.5):
        minutes=" quarter past"
    else:
        if (int(minutes)>22.5) and (int(minutes)<37.5):
            minutes=" half past"
    else:
        if (int(minutes)>37.5) and (int(minutes)<52.5):
            minutes=" quarter to"
if minutes == "quarter to":
    if int(hour)<12:
        hour=int(hour) + 1
        print("The time is about" + str(minutes) + " " + str(hour) + " in the morning")
    else:
        hour=int(hour) - 12
        hour=int(hour) + 1
        print("The time is about" + str(minutes) + " " + str(hour) + " in the afternoon")
else:
    if int(hour)<12:
        print("The time is about" + str(minutes) + " " + str(hour) + " in the morning")
    else:
        hour=int(hour) - 12
        print("The time is about" + str(minutes) + " " + str(hour) + " in the afternoon")
