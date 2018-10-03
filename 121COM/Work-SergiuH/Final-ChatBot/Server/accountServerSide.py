import pickle

def accountServerSide(dictionary):
    """Takes input as dictionary, returns an integer which tells the server what to do.
    Handles main accountServerSide operations."""
    if __name__=="__main__":
        x=input("Do you want to delete the database?\n")
        if x == "Yes, I do, avocados are great.":     #deletes the database if x is this 
            f1=open("database.txt","w")
            print("You monster.")
            f1.close()
            return()       #if someone deletes the database, stops the program 
        else:
            print("Nah.")
            
    username=dictionary["username"]     #pulls out values to use 
    password=dictionary["password"]
    login=str(dictionary["login"])
    
    f1= open("database.txt", "r")
        #we open it in read mode
    string1= f1.read()
        #we read it as a stirng
    list1=string1.split()
        #we make it into a list
    f1.close()
    
    x=len(list1)
    
    listUser=list1[0:int(x/2)]
    listPass=list1[int(x/2):x]
    
    if login == "False":
        if username in listUser:
            return(1)
        
        clientInfoRegister(username)  #registers with the infoHub 
        
        listUser.append(username)
        listPass.append(password)
        
        f1=open("database.txt","w")        
        list1=listUser+listPass    
        string1=" ".join(list1)       
        f1.write(string1)
        f1.close()
        
        return(0)
    
    else:
        i=-1
        for element in listUser:
            i+=1
            if element == username:
                if listPass[i] == password:
                    return(7)
    return(2)


def clientInfoRegister(username):
    """Function which indexes the infoHub when a user first logs in"""
    dictionaryInfo={}   
    
    try:
        f2=open("clientInfo.txt","rb")
        dictionaryInfo = pickle.load(f2)  
        f2.close()
    except EOFError:
        pass            #this takes care of the error when the user creates an account for the first time
    dictionaryInfo[username]=["","",""] #starts with no values 
    f3=open("clientInfo.txt","wb")
    pickle.dump(dictionaryInfo,f3)    #saves the dictionary of all users
    f3.close()
    
    return()

def infoHub(username,terminalName,curseCounter,placeholder):
    """Function which takes care of the user info database. Call with input: (username,"","","") 
    to get back the userInfoList. If you call it with any input, it will override the existing one."""
    f2=open("clientInfo.txt","rb")
    dictionaryInfo = pickle.load(f2)  #loads the dictionary of all users info 
    f2.close()
    
    list1 = dictionaryInfo[username]  #loads the list of the user 
    
    if terminalName:
        list1[0] = terminalName   #if any of the variables exists, it overrides the existng one in the list 
    elif curseCounter:
        list1[1] = curseCounter
    elif placeholder:
        list1[2] = placeholder
    else:                          #if we call the function with no inputs, it gives us the userInfoList 
        print("User info:" + str(list1))  #prints so we have a better idea 
        return(list1)
    
    dictionaryInfo[username]=list1        #if the user ammended the list, index it to the big dictionary 
    
    #print(dictionaryInfo)           #print it for good measure 
    
    f3=open("clientInfo.txt","wb")
    pickle.dump(dictionaryInfo,f3)         #save it 
    f3.close()
    

if __name__=="__main__": 
    try:
        dictionary={"username":"sergiu","password":"test1","login":"False"}
        print(accountServerSide(dictionary))
        print(infoHub("sergiu","","",""))
    except KeyboardInterrupt:
        print("Shutting down.")
