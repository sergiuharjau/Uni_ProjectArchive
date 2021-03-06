import gspread
from oauth2client.service_account import ServiceAccountCredentials
       
class Budget:  
    rentFund = 0 
    buffer = 0 
    holiday = 0 
    leisure = 0 
    
    rent = 150 
  
    distributeB = 0.0
    distributeH = 0.3   #must add up to 1
    distributeL = 0.7   #200 quid in buffer already
    
    minimumB = 50
    minimumH = 7
    minimumL = 10 
    
    def __init__(self, userInput):
        
        self.initiateConnection(userInput) 
        self.getPreviousFunds() 
        self.getSheetsInputs() 
      
        Budget.leisure -= self.leisure 
        Budget.holiday -= self.holiday
        
        self.rentPaid = 0 
        self.necPaid = 0 
        
        self.holidayAdded = 0 
        self.leisureAdded = 0 

        self.allowance = 20

    def initiateConnection(self, userInput):
        
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("Spreadsheet Updater-bdd3fd26a51b.json", scope)
        gc = gspread.authorize(credentials)

        self.wks = gc.open("Budget Planner 2").sheet1 
        
        self.weekRow = userInput + 6  # Week -3 = Row 3  
        self.weekNumber = userInput 
    
    def getPreviousFunds(self):
        
        Budget.rent     = float(self.wks.cell( self.weekRow, 4).value) #rent to pay 
        Budget.buffer   = float(self.wks.cell( self.weekRow, 5).value)
        Budget.holiday  = float(self.wks.cell( self.weekRow, 6).value)
        Budget.leisure  = float(self.wks.cell( self.weekRow, 7).value)
        #Budget.rentLeft = float(self.wks.cell( self.weekRow, 17).value) #rent left 
    
    def getSheetsInputs(self):
        
        # Inputs = I  J K / M  N 
        #          9 10 11 13 14 
        self.necessities = float(self.wks.cell( self.weekRow,  9).value)
        self.holiday     = float(self.wks.cell( self.weekRow, 10).value)
        self.leisure     = float(self.wks.cell( self.weekRow, 11).value)
        self.work        = float(self.wks.cell( self.weekRow, 13).value)
        self.sideHustle  = float(self.wks.cell( self.weekRow, 14).value)
    
    def writeToSheets(self):
        
        #Outputs = D E F G 
        #          4 5 6 7 
        #no longer updating rent fund 
        self.wks.update_cell(self.weekRow + 1, 5, round(Budget.buffer,2))
        self.wks.update_cell(self.weekRow + 1, 6, round(Budget.holiday,2))
        self.wks.update_cell(self.weekRow + 1, 7, round(Budget.leisure,2))
        #self.wks.update_cell(self.weekRow + 1, 17, round(Budget.rentLeft - Budget.rent,2))
        
    def moneyIN(self, money):
       
        #print("\nMoney in " + str(money))
    
        if money > Budget.rent - self.rentPaid:
            if self.rentPaid != Budget.rent: 
                #print("Paying rent: " + str(Budget.rent - self.rentPaid))
                money -= (Budget.rent - self.rentPaid)  
                #print("Money left: " + str(money))
                self.rentPaid = Budget.rent 
                          
            if money > self.necessities - self.necPaid:
                if self.necPaid != self.necessities:
                    #print("Paying necessities: " + str(self.necessities - self.necPaid))
                    money -= (self.necessities - self.necPaid) 
                    #print("Money left: " + str(money))
                    self.necPaid = self.necessities
                #print("Distributing: " + str(money))
                Budget.buffer += Budget.distributeB * money 
                self.holidayAdded += Budget.distributeH * money 
                self.leisureAdded += Budget.distributeL * money 
                
            else: 
                #print("Paying it all to necessities. " + str(money))                
                self.necPaid += money
                
        else:
            #print("Paying it all to rent. " + str(money))
            self.rentPaid += money 
 
    def finishWeek(self):
        
        self.moneyIN(self.work)
        self.moneyIN(self.sideHustle)
        self.moneyIN(self.allowance)

        if self.rentPaid < Budget.rent: 
            #print("\nMissing " + str(Budget.rent - self.rentPaid) + " of rent")
            #print("Taking it from Buffer.")
            payIN = Budget.rent - self.rentPaid
            self.moneyIN(payIN)
            Budget.buffer -= payIN 
        if self.necPaid < self.necessities:
            #print("\nMissing " + str(self.necessities - self.necPaid) + " of necessities")
            #print("Taking it from Buffer.")
            payIN = self.necessities - self.necPaid
            self.moneyIN(payIN)
            Budget.buffer -= payIN
        
        if self.holidayAdded < Budget.minimumH and Budget.buffer > Budget.minimumB: 
            Budget.buffer -= Budget.minimumH - self.holidayAdded
            self.holidayAdded = Budget.minimumH
        if self.leisureAdded < Budget.minimumL and Budget.buffer > Budget.minimumB:
            Budget.buffer -= Budget.minimumL - self.leisureAdded
            self.leisureAdded = Budget.minimumL
            
        Budget.holiday += self.holidayAdded
        Budget.leisure += self.leisureAdded
        
        Budget.rentFund += self.rentPaid 

        self.writeToSheets() 
        
if __name__ == "__main__":
    userInput = int(input("What week? "))
    if userInput == -100:
        weekUpTo = int(input("Up to what week? ")) + 1 
        for weekNumber in (-3,-2,-1):
            print("Working on " + str(weekNumber)) 
            week=Budget(weekNumber)
            week.finishWeek()           
        for weekNumber in range(weekUpTo):
            print("Working on " + str(weekNumber)) 
            week=Budget(weekNumber)
            week.finishWeek()
    else:
        week = Budget(userInput)   
        week.finishWeek() 
    print("All good!")
        