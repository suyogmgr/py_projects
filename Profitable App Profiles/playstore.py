import csv

with open("googleplaystore.csv") as gp:
    android_app = csv.reader(gp)
    android = list(android_app)
    android_headers = android[0]
    android = android[1:]

with open("AppleStore.csv") as ap:
    appple_app = csv.reader(ap)
    apple = list(appple_app)
    apple_headers = apple[0]
    apple = apple[1:]


def explore_data(dataset, start, end, row_and_columns = False):
    dataset_slice = dataset[start:end]

    for row in dataset_slice:
        print(row)

    if row_and_columns:
        print(f"\nNo of rows is {len(dataset)}")
        print(f"No of columns is {len(android_headers)}")


print(android_headers)
#explore_data(android, 0, 3, True)


#This row has a rating of 19 which is not possible 
#print(android[10472])

#Deleting the row no 10472

# print(len(android))
# del android[10472]
# print(len(android))


#printing the names of duplicate apps in google play store
'''
for app in android:
    name = app[0]
    if name == "Instagram":
        print(app)
'''

#printing all the duplicate apps 


unique_app = []
duplicate_app = []

for app in android:
    name = app[0]

    if name in unique_app:
        duplicate_app.append(name)
    else:
        unique_app.append(name)

print(f"The no of Unique apps are {len(unique_app)}")
print(f"The no of duplicate apps are {len(duplicate_app)}")
print(f"Some duplicate apps are {duplicate_app[:15]}")


