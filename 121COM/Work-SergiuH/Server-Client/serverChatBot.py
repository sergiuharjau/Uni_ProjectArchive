import socket,sys,time

def serverBackbone():
    """Function which initializes the chatbot server."""
    host = "127.0.0.1"
        #this is the sever's IP, clients needs it to connect
    port = 5007
        #server's port, needs to be the same as the client's
    thisSocket = socket.socket()
    thisSocket.bind((host,port))  
        #programming mumble jumble which makes the whole thing work
    thisSocket.listen(3)
        #number of clients that can connect to the server, 3 at the moment
    conn, addr = thisSocket.accept()
        #addr here is the ip address of the user, conn=connect
    print("Client connected.")
    while True: #repeats the loop forever, until being told otherwise
        receiveMess = conn.recv(1024).decode()
        if not receiveMess:
        break    #this ends the looop when the clients disconnects
          
        from userInput import emotionHandler
            
            returnMess=emotionHandler(receiveMess)
          
          #   This is where the main body of our chatbot will be, where we call other functions, and so on
          #   At the moment I am printing some things back to the user for us to see that it does work
          #   In the future though, we need to figure out ways to actually get the music playing, and do that
        
        print("The user wrote: " + str(receiveMess))
              #this gets printed to the server, in the future this will be pointless
          #returnMess="We have received your message, but we still can't read it, sadly. Check again later."
       #this is what actually gets printed to the user, at the moment a placeholder
          conn.send(returnMess.encode())
    conn.close()

    
if 1==1:
    serverBackbone()
        
        