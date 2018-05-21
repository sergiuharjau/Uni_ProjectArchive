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
    
    url = "http://maps.googleapis.com/maps/api/geocode/json?address="
    
    city_url = url + city
      
    data = urllib.request.urlopen(city_url)
   
    results = json.loads(data.read().decode())["results"]
    
    if results == []:
        print("Google API prevented us from getting: " + city[:len(city)-1])
        return({"lat" : 0 , "lng" : 0})                    

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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        