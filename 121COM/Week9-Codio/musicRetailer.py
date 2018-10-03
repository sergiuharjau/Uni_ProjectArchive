import random 

class Retailer():
    
    __basketArtists = [] 
    __basketSongs = []
    __sale = 0
    price = 0 
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title 
        self.price += Retailer.price + 1 * (1-Retailer.__sale)
        Retailer.__basketArtists.append(artist)
        Retailer.__basketSongs.append(title)
        
    def getPrice(self):
        return(self.price)
    
    def getBasket(self):
        ans1 = ""
        ans2 = ""   
        for word in Retailer.__basketArtists:
            ans1 += word + ", "
        for word in Retailer.__basketSongs:
            ans2 += word + ", "
        price = self.price 
        ans1 = ans1[0:len(ans1)-2] #gets rid of the last comma 
        ans2 = ans2[0:len(ans2)-2] #gets rid of the last comma 
        return("\nCurrent artists: " + ans1 + "\nCurrent songs: " + ans2 +"\nPriced at: £" + str(price))
    
    def addSong(self, artist, title):
        Retailer.__init__(self, artist, title)

class RealLife(Retailer): 
    
    shipping_cost = 0.3 
    
    def __init__(self,artist,title):
        self.eta_delivery = random.randint(1,7)
        Retailer.__init__(self, artist, title)
        self.price += RealLife.shipping_cost 
        
    def getDelivery(self):
        return("Days until delivery: " + str(self.eta_delivery))
    
    def addSong(self, artist, title):
        Retailer.addSong(self,artist,title)
        self.price += RealLife.shipping_cost 
    
class CD(RealLife): 
    
    def __init__(self, artist, title):
        RealLife.__init__(self, artist, title)

class Vinyl(RealLife):
    
    def __init__(self, artist, title):
        RealLife.__init__(self, artist, title)
        self.cover = None 
        self.size = "medium"
        
    def setCover(self, cover):
        self.cover = cover 
        
    def setSize(self, size):
        if size == 1: 
            self.size = "small"
        elif size == 2:
            self.size = "medium"
        elif size == 3:
            self.size = "large"
            
    def vinylCheck(self):
        return("Your vinyl is " + self.size + " sized and has a cover of '" + str(self.cover) + "'")

class Download(Retailer):
    
    online_reduction = 0.3
    
    def __init__(self, artist, title):
        Retailer.__init__(self, artist, title)
        self.price -= Download.online_reduction
        self.sizeMB = random.randint(1,10)
        
    def getBasket(self):
        ans = Retailer.getBasket(self)
        return(ans + "\nSize in MB: " + str(self.sizeMB))
           
    def addSong(self, artist, title):
        Retailer.addSong(self,artist,title)
        self.price -= Download.online_reduction
        
        
v1 = Download("Ed Sheeran", "I see fire")
v1.addSong("Kendrick Lamar", "Money Trees")

v1 = CD("Rogers", "Test")

print(v1.getBasket())
