import urllib.request, json

url = "http://maps.googleapis.com/maps/api/geocode/json?address="

def sanitizeInput(city_raw):
    city_list = city_raw.split() 
    city = ""

    for element in city_list:
        city += element 
        city +="+"
    
    return city 

city1_raw = input ("First city: ")
city2_raw = input ("Second city: ")

city1 = sanitizeInput(city1_raw)
city2 = sanitizeInput(city2_raw)

c1_url = url + city1 + "&sensor=false"
c2_url = url + city2 + "&sensor=false"

data1 = urllib.request.urlopen(c1_url)
data2 = urllib.request.urlopen(c2_url)

coordinates1 = json.loads(data1.read().decode())["results"][0]["geometry"]["location"]
coordinates2 = json.loads(data2.read().decode())["results"][0]["geometry"]["location"]


print(coordinates1)
print(coordinates2)

medianLAT = ( coordinates1["lat"] + coordinates2["lat"] ) / 2 
medianLNG = ( coordinates1["lng"] + coordinates2["lng"]) / 2 

print("Median Lat: %f \nMedian Lng: %f" % (medianLAT, medianLNG)) 