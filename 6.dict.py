N110016 = {"Name": "Siri", "Age": "22", "Branch": "CSE", "Office": "Yes"}
N110012 = {"Name": "Siri", "Age1": "21", "Bsranch": "ECE", "Office1": "No"}
print N110016["Name"]
N110016.update(N110012)
print N110016
for x in N110016:
    val = N110016[x]
    N110016[x] = val.upper()
    print('Changed what', x, 'points to: from', val, 'to', N110016[x])