import socket,sys,time

def clientBackbone():
    host = "127.0.0.1"
    port = 5007
        #credentials needed to connect to the server
    thisSocket = socket.socket()
    thisSocket.connect((host,port))
        #crucial bit of coding
    user=input("What's your name? ")
    message = input(user + ": ")
        #we initialise it here in order to prevent an error
    while message != "end":    #keeps the conversation open until the user types end
          thisSocket.send(message.encode())
   #send the message to the server
          receivedMess = thisSocket.recv(1024).decode()
        
          # This is the same deal like with the server, this is where we will input the actual "music"
          # At the moment I will just put a placeholder print function, to see that it works
          from userInput import slow_type
         
          print("Zach: ",end="")
  
          slow_type(receivedMess)
          message = input(user + ": ")
              #we ask the user to input some more text, keep the conversation open
    thisSocket.close()
        #when the user types end, the loop breaks, and the connection closes
    print("I hope you enjoyed our services!")
        #this is where we print a final statement to the user

if True:
    clientBackbone()
        
        

        