
import string as str

def short(twttr):
    vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    temp = ""
    for s in twttr:
        if s in vowels:
            temp += ""
        elif s.isdigit() == True:
            temp += ""
        elif s in str.punctuation:
            temp += ""
        else:
            temp += s
    return temp

def main():
    twttr = input("Input: ")
    print(short(twttr))



if __name__ == "__main__":
    main()


# temp = ""
# vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
# str_usr = "su4584eve..r"
# for s in str_usr:
#     if s in vowels:
#         temp += ""
#     elif s.isdigit() == True:
#         temp += ""
#     elif s in str.punctuation:
#         temp += ""
#     else:
#         temp += s
    
# print(temp)
