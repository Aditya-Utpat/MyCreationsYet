mass = int(input('Enter weight of parcel:'))
if mass <= 10:
    charge = 15*mass
elif mass <= 20:
    charge = 25*mass
elif mass >30:
    charge = 35*mass
print('The charge is',charge)
