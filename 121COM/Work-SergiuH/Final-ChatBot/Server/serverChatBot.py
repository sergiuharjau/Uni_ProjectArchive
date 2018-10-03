import socket,sys,time

def serverBackbone(port):
    """Function which initializes the chatbot server."""
    host = "127.0.0.1"
        #this is the sever's IP, clients needs it to connect
    port = port
        #server's port, needs to be the same as the client's
    thisSocket = socket.socket()
    thisSocket.bind((host,port))  
        #programming mumble jumble which makes the whole thing work
    thisSocket.listen(3)
        #number of clients that can connect to the server, 3 at the moment
    conn, addr = thisSocket.accept()
        #addr here is the ip address of the user, conn=connect
    print("Client connected.")
    n=0
                  
    from accountServerSide import accountServerSide, infoHub, clientInfoRegister
    #from cursewordDetector import curseCounter  #not my function
    
    dictionary={}
    while n==0 or n==1:
        receivedMess = conn.recv(1024).decode()
        
        if not receivedMess:   #prevents crash 
            return()
        
        receivedMess= receivedMess.split("       ")    #splits at 7 spaces, creates list 
               
        dictionary["username"]=receivedMess[0]    
        dictionary["password"]=receivedMess[1]    
        dictionary["login"]=receivedMess[2]
            
        username = dictionary["username"]
            
        n=accountServerSide(dictionary)    
            
               
        if n == 2:
            returnMess="Wrong"
            n=0
            conn.send(returnMess.encode())
            continue      #wrong credentials
        if n == 7:
            returnMess="Confirmed"    #when the user logs in, pull the userInfoList for him 
            userInfoList= infoHub(username,"","","")
            conn.send(returnMess.encode())
            
        else: 
            returnMess=str(n)   
            conn.send(returnMess.encode())
        
        
    receivedMess = conn.recv(1024).decode()
    
    if not receivedMess:   #prevents crash 
            return()
    
    informationString=""
    
    for word in userInfoList:   #transform the list into a format that we can send over 
        informationString= informationString + " " + word
    informationString=informationString[1:]  #the first character is a blank, delete that 
    
    conn.send(informationString.encode())  
   
        
    
    while True:
        receivedMess = conn.recv(1024).decode()
        if "   456   " in receivedMess:  #this means that the user doesn't have a terminal name 
            
            receivedMess=receivedMess[9:]  #this is the future terminal name 
            infoHub(username,receivedMess,"","")  #index it 
            
            userInfoList[0]=receivedMess #ammend the list
            
            conn.send(userInfoList[0].encode())  #send the terminal name back
            continue
            
        if not receivedMess:  #prevents crash 
            return()                  
        
        receivedMess = receivedMess.lower()    #makes everything in lowercaps, easier to code around it 
        
        returnMess = receivedMess
        
        #returnMess = curseCounter(receivedMess,username)  #checks for swear words 
                                                            #not my function
                       
        if returnMess == receivedMess:
            returnMess = "Whoops, we haven't coded that in yet."
                
        print(userInfoList[0] + " wrote: " + str(receivedMess)) #prints to the server terminal for good measure 
        conn.send(returnMess.encode())
            
    conn.close()

    
if __name__=="__main__":
    try:
        port = 5008
        while True:
            print("Server initialised")
            serverBackbone(port)
    except KeyboardInterrupt:
        print("\nShutting down")
        
        