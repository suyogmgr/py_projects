# # wap ask at least 5 users demography 
# # if age < 20 teenageer if > 20 < 50 youths > 50 old

# teenage = []
# youths = []
# eldery = []

# while True:
#     name = input("Enter your name: ").lower()
#     age = input("Enter your age: ")
#     # nationality = input("Enter your natiolanity: ")
#     # religion = input("Enter you religion: ")
    
#     if name == 'shyam':
#         print("Invlaid name")
#         break

#     if name == 'ram':   
#         continue

#     age = int(age)

#     if age < 20 and name:
#         teenage.append(name)
#     elif age >= 20 and age <= 50:
#         youths.append(name)
#     elif age > 50 and name:
#         eldery.append(name)

# for x in teenage:
#     print(x, end=" ")
# else:
#     print("Teenage else")

# print()

# for x in youths:
#     print(x, end=" ")
# else:
#     print("Youths else")

# print()

# for x in eldery:
#     print(x, end=" ")
# else:
#     print("Elderly else")


# tuples = (1,2)
# a,b = tuples


# tuple,list,set,frozenset

# set(tuples)
# list(tuples)

# names = []

# while True:
#     username = input("Enter your name(q to quit): ").strip().lower()

#     if username == 'q':
#         break

#     names.append(username)    
    
# print(names)
# print(list(set(names)))


# name_list = ['ram', 'ram', 'shyam', 'shyam', 'hari', 'hari', 'gita', 'manjil', 'ram']

name_list = [{"name":"Suyog","age":22}, {"name":"Nirjal", "age":22}, {"name":"Samjhana", "age":45}]


name_list.sort(key=lambda x : x["name"])

print("ASC >>>>>>>",name_list)
name_list.sort(reverse=True,key=lambda x : x["age"])

print("DESC >>>>>>>",name_list)


# for k,v in enumerate(name_list):
#     print(k,v)


# for index in range(len(name_list)):
#     print(index, name_list[index])

# bio = "My name is Suyog Rana Magar"


# for i in bio:
#     print(i)

