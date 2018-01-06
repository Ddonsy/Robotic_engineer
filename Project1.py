# Developer: Awantha Jayasiri
# Version:1.0

#Test_address=1600 Amphitheatre Parkway, Mountain View, CA

# Import basic python libraries
import urllib
import   json, time

# Geocoding from Google
base_add1="https://maps.googleapis.com/maps/api/geocode/json"
api_key1="AIzaSyAIDJzrlNokl_U0xU9fkEuN9_0ERVV2MLc"

#Geocoding from HERE
base_add2="https://geocoder.cit.api.here.com/6.2/geocode.json"
app_id="kZXILl2iXMyFg55fJ3Ep"
app_code="hX9oBaIno7fPWH4CXuGG4g"

# Enter the address you want to get the lat, lng
var = raw_input("Enter the address:")
var.replace(" ","+")
print("You entered " + var)

# URL constructing for google
GeoUrl1 = base_add1 +"?address="+var
# URL constructing for HERE
GeoUrl2 = base_add2 +"?searchtext="+var+"&app_id="+app_id+"&app_code="+app_code

# First check whether google geocoding works. If not try HERE geocoding
response = urllib.urlopen(GeoUrl1)
jsonRaw = response.read()
jsonData = json.loads(jsonRaw)

# Check status codes
if jsonData['status'] == 'OK':
     latitude = jsonData['results'][0]['geometry']['location']['lat']
     longitude = jsonData['results'][0]['geometry']['location']['lng']
     print 'Latitude:', latitude
     print 'Longitude:', longitude
elif jsonData['status'] == 'ZERO_RESULTS':
    print 'a non-existent address, Please check your address.'
elif jsonData['status'] =='INVALID_REQUEST':
    print 'Query is missing something. Please check'
else:   # For OVER_QUERY_LIMIT, REQUEST_DENIED and ERROR: try HERE geocoding
    response = urllib.urlopen(GeoUrl2)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    print 'Latitude:', jsonData['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    print 'Longitude:',jsonData['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']

