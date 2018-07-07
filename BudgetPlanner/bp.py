       
class Budget:
    rent = 150 
    
    rentFund = 0 
    buffer = 0 
    holiday = 0 
    leisure = 0 
    
    def __init__(self):
              
        self.weekNumber = -1
        
        self.loadFromDB() 
     
        self.necessities = float(input("\n\nNecessities spent: "))
        self.holiday = float(input("Holiday spent: ")) 
        self.leisure = float(input("Leisure spent: "))
        Budget.leisure -= self.leisure 
        Budget.holiday -= self.holiday
        
        self.rentPaid = 0 
        self.necPaid = 0 
        
        self.holidayAdded = 0 
        self.leisureAdded = 0 
        
        self.work = int(input("Work money: "))
        self.sideHustle = int(input("Hustle money: ")) 
        self.allowance = 20

    
    def moneyIN(self, money):
       
        print("\nMoney in " + str(money))
    
        if money > Budget.rent - self.rentPaid:
            if self.rentPaid != Budget.rent: 
                print("Paying rent: " + str(Budget.rent - self.rentPaid))
                money -= (Budget.rent - self.rentPaid)  
                print("Money left: " + str(money))
                self.rentPaid = Budget.rent 
                          
            if money > self.necessities - self.necPaid:
                if self.necPaid != self.necessities:
                    print("Paying necessities: " + str(self.necessities - self.necPaid))
                    money -= (self.necessities - self.necPaid) 
                    print("Money left: " + str(money))
                    self.necPaid = self.necessities
                print("Distributing: " + str(money))
                Budget.buffer += 0.5 * money 
                self.holidayAdded += 0.2 * money 
                self.leisureAdded += 0.3 * money 
                
            else: 
                print("Paying it all to necessities. " + str(money))                
                self.necPaid += money
                
        else:
            print("Paying it all to rent. " + str(money))
            self.rentPaid += money 

     
    def overview(self):
        print("\nWeek " + str(self.weekNumber))
        print("\nNecessities spent: " + str(self.necessities))
        print("Leisure spent: " + str(self.leisure))
        print("\nWork money: " + str(self.work))
        print("Holiday added: " + str(self.holidayAdded))
        print("Leisure added: " + str(self.leisureAdded))
        print("\nState of Rent Fund: " + str(Budget.rentFund))
        print("State of Buffer: " + str(Budget.buffer))
        print("State of Holiday: " + str(Budget.holiday))
        print("State of Leisure: " + str(Budget.leisure))
    
    def indexToDB(self):
        f1 = open("database.txt" , "w")
        
        values = [] 
        
        values.append(self.weekNumber)
        values.append(Budget.rentFund)
        values.append(Budget.buffer)
        values.append(Budget.holiday)
        values.append(Budget.leisure)
        
        print("\nThis is what we are indexing to the database.")
        for element in values:
            print(round(element,2), end ="; ")
        print("")
        for element in values:
            f1.write(str(round(element,2)) + "\n")
            
        f1.close() 
    
    def loadFromDB(self):
        f1 = open("database.txt" , "r")
        rawValues = f1.readlines() 

        values = [] 
        
        for element in rawValues:
            values.append(element.replace('\n',''))
         
        print("\nThese are the values we have imported.")
        print(values)
        
        self.weekNumber = float(values[0]) + 1 
        Budget.rentFund = float(values[1])
        Budget.buffer = float(values[2])
        Budget.holiday = float(values[3])
        Budget.leisure = float(values[4])
        
        f1.close() 
        
    def finishWeek(self):
        
        self.moneyIN(self.work)
        self.moneyIN(self.sideHustle)
        self.moneyIN(self.allowance)

        if self.rentPaid < Budget.rent: 
            print("\nMissing " + str(Budget.rent - self.rentPaid) + " of rent")
            print("Taking it from Buffer.")
            payIN = Budget.rent - self.rentPaid
            self.moneyIN(payIN)
            Budget.buffer -= payIN 
        if self.necPaid < self.necessities:
            print("\nMissing " + str(self.necessities - self.necPaid) + " of necessities")
            print("Taking it from Buffer.")
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
        
        self.overview() 
        
        self.indexToDB() 
        
if __name__ == "__main__":
    week = Budget()
    week.finishWeek() 
        