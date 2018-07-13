import gspread
from oauth2client.service_account import ServiceAccountCredentials
       
class Budget:
    rent = 150 
    
    rentFund = 0 
    buffer = 0 
    holiday = 0 
    leisure = 0 
    
    def __init__(self):
        
        self.initiateConnection() 
        self.getPreviousFunds() 
        self.getSheetsInputs() 
      
        Budget.leisure -= self.leisure 
        Budget.holiday -= self.holiday
        
        self.rentPaid = 0 
        self.necPaid = 0 
        
        self.holidayAdded = 0 
        self.leisureAdded = 0 

        self.allowance = 20

    def initiateConnection(self):
        
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("Spreadsheet Updater-bdd3fd26a51b.json", scope)
        gc = gspread.authorize(credentials)

        self.wks = gc.open("Budget Planner").sheet1 
        
        self.weekRow = int(input("What week? ")) + 3  # Week 0 = Row 3 
        self.weekNumber = self.weekRow - 3 
    
    def getPreviousFunds(self):
        
        Budget.rentFund = float(self.wks.cell( self.weekRow, 4).value)
        Budget.buffer   = float(self.wks.cell( self.weekRow, 5).value)
        Budget.holiday  = float(self.wks.cell( self.weekRow, 6).value)
        Budget.leisure  = float(self.wks.cell( self.weekRow, 7).value)
    
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
        self.wks.update_cell(self.weekRow + 1, 4, Budget.rentFund)
        self.wks.update_cell(self.weekRow + 1, 5, Budget.buffer)
        self.wks.update_cell(self.weekRow + 1, 6, Budget.holiday)
        self.wks.update_cell(self.weekRow + 1, 7, Budget.leisure)
        
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
                Budget.buffer += 0.5 * money 
                self.holidayAdded += 0.2 * money 
                self.leisureAdded += 0.3 * money 
                
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
        
        if self.holidayAdded < 7 and Budget.buffer > 70: 
            Budget.buffer -= 7 - self.holidayAdded
            self.holidayAdded = 7
        if self.leisureAdded < 15 and Budget.buffer > 70:
            Budget.buffer -= 15 - self.leisureAdded
            self.leisureAdded = 15
            
        Budget.holiday += self.holidayAdded
        Budget.leisure += self.leisureAdded
        
        Budget.rentFund += self.rentPaid 

        self.writeToSheets() 
        
        print("All good!")
        
if __name__ == "__main__":
    week = Budget()
    week.finishWeek() 
        