import pickle
# Python distance lib
import geopy.distance as gpd

with open("codes.pickle", "rb") as f:
    codes = pickle.load(f)

# Create a dict from the list of codes, and save a seperate list of the keys [area codes] for reversing.
codes_dict = {}
for x in codes:
    codes_dict[x[0]] = x
    areacodelist = [cl for cl in codes_dict]
# Reverse the area code list so the matcher break works when looping through the list.
rAClist = sorted(areacodelist, reverse=True)

# Grab the phone codes for testing from user input
first_number = input('enter first area code ')
type(first_number)
second_number = input('enter the second area code ')
type(second_number)

firstcode = []
# For every code in the reversed list (029 -> 0113)
for v in rAClist:
    # Create a range to slice the phone numbers with.
    for matchIndex in (range(3, 7)):
        # TTest whether a code has been written yet and if v matches the sliced user input.
        if len(firstcode) == 0 and v == first_number[:matchIndex]:
            firstcode.append(v)
            break

secondcode = []
for v in rAClist:
    for matchIndex in (range(3, 7)):
        if len(secondcode) == 0 and v == second_number[:matchIndex]:
            secondcode.append(v)
            break
bothcodes = firstcode + secondcode       

# Combine both codes into a list of lists for feeding to gpd.
bothcodeslatlong = ([codes_dict[bothcodes[0]][2:]] + [codes_dict[bothcodes[1]][2:]])
# Do the distance calculation.
distanceinmiles = (gpd.distance(bothcodeslatlong[0], bothcodeslatlong[1]).miles)

print(f'''
Details for the first phone number: ({first_number})
Area code : {bothcodes[0]}
Latitude : {bothcodeslatlong[0][0]}
Longitude : {bothcodeslatlong[0][1]}

Details for the second phone number: ({second_number})
Area code : {bothcodes[1]}
Latitude : {bothcodeslatlong[1][0]}
Longitude : {bothcodeslatlong[1][1]}

The distance between {bothcodes[0]} ({codes_dict[bothcodes[0]][1]}) and {bothcodes[1]} ({codes_dict[bothcodes[1]][1]})
is {distanceinmiles:.2f} miles
''')

# Rudimentary at this point, but, felt I wanted to complete the 'challenge' :>
if int(distanceinmiles) >= 100:
    print('Distance is further than 100 miles')
else:
    print ('Distance is closer than 100 miles')
