import urllib.request, json

def sanitizeInput(city_raw):
    city_list = city_raw.split() 
    city = ""

    for element in city_list:
        city += element 
        city +="+"
    
    return city 


def determineCities():
    """Receives input from the user, returns said input as a list."""
    
    numberCities = int(input("How many cities? "))
    
    citiesList = [] 
    
    for i in range(numberCities):
        citiesList.append(input("City " + str(i+1) + ": "))
       
    return citiesList

def getCoordinates(city):
    
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    
    city_url = url + city + "&key=AIzaSyDKGESVCnLJSfToUDSST5Ydx8ei9bf4ttM"
      
    data = urllib.request.urlopen(city_url)
   
    results = json.loads(data.read().decode())["results"]
    
    if results == []:
        print("Google API prevented us from getting: " + city[:len(city)-1])
        return(getCoordinates(city))                    

    coordinates = results[0]["geometry"]["location"]

    return coordinates 
    
def getMedian(allCoordinates):
    
    longitude = 0 
    latitude = 0 
    
    for coordDict in allCoordinates:
        longitude += coordDict["lng"]
        latitude += coordDict["lat"]
        
    medianLng = longitude / len(allCoordinates)
    medianLat = latitude / len(allCoordinates)
    
    return({"lat" : medianLat , "lng" : medianLng})
    
def findCityAt(coordinates, lookAT = -1, factor = 0.01):
    
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="
    
    latitude = coordinates["lat"] 
    longitude = coordinates["lng"] 
    ##print(lookAT)
    if lookAT == -1:
        pass
    elif lookAT == 0: #North
        latitude += factor #increments by 0.01 every time we go back to North 
    elif lookAT == 1: #East
        longitude += factor 
    elif lookAT == 2: #South
        latitude -= factor
    elif lookAT == 3: #West
        longitude -= factor   
    
    location_url = url + str(latitude) + "," + str(longitude) + "&key=AIzaSyDKGESVCnLJSfToUDSST5Ydx8ei9bf4ttM"
    
    data = urllib.request.urlopen(location_url)
   
    results = json.loads(data.read().decode())["results"]
    
    if results == []:
        print("That may be in the ocean.")
        print("Here's the coordinates though!")
        print(str(round(coordinates["lat"],2)) + " , " + str(round(coordinates["lng"],2)))
        return("Undefined", "Undefined")
    
    address_components = results[0]["address_components"]
    
    city = "Undefined"
    
    for i in range(len(address_components)):
        if "locality" in address_components[i]["types"]:
            city = address_components[i]["long_name"]
        if "country" in address_components[i]["types"]:
            country = address_components[i]["long_name"]
    
    if city == "Undefined":
        lookAT += 1 
        if lookAT > 3:
            lookAT = 0
            factor += 0.01
        return ( findCityAt({"lat" : latitude , "lng" : longitude } , lookAT , factor ) )
    
    return ( city, country )  

def findInDatabase(city, country, coordinates):
    
    f1 = open("/home/codio/workspace/worldcitiespop.txt", "r", encoding = "ISO-8859-1")
	
    bigList = f1.readlines() 

    for line in bigList:
        if city.lower() in line and country.lower() in line:
            if str(round(coordinates["lat"],1)) in line and str(round(coordinates["lng"],1)) in line:
                print(line)
    
if __name__ == "__main__":
    
    citiesList = determineCities()
    
    sanitizedCities = [] 
    
    for city in citiesList:
        sanitizedCities.append(sanitizeInput(city))
    
    allCoordinates = [] 
    
    for city in sanitizedCities:
        allCoordinates.append(getCoordinates(city))
    
    median = getMedian(allCoordinates)
    
    googleURL = "https://www.google.co.uk/maps/place/"
    
    link = googleURL + str(median["lat"]) + "," + str(median["lng"]) + "/"
        
    print(link)
    
    city, country = findCityAt({"lat" : 44.308271, "lng" : 26.686003})
               
    print(city, country)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        