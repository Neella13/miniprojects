#create a program that manages a dictionary of word meanings.the program should allow users to perform the following actions
dictionary={}
while True:
    print("\n DICTIONARY MANAGEMENT SYSTEM")
    print("1.Add a word")
    print("2.Search for meaning")
    print("3.display all words")
    print("4.update meaning")
    print("5.Delete a word")
    print("6.exit")
    choice=int(input("enter your choice:"))

    if choice==1:
        word=input("enter a word:")
        meaning=input("enter a meaning:")
        dictionary[word]=meaning
        print("word and meaning added to dictinary sussefully!!!")

    elif choice==2:
        word=input("enter the word to search meaning:")
        if word in dictionary:
            print("meaning:",dictionary[word])
        else:
            print("the meaning is not found:")

    elif choice==3:
        print(dictionary)  

    elif choice==4:
        word=input("enter a word u want to update its meaning :")
        meaning=input("enter a meaning to update in dictionary:")
        dictionary[word]=meaning
        print(dictionary)  
        print(" Meaning updated sucessfully!!")

    elif choice==5:
        word=input("enter a word to delete:")
        dictionary.pop(word)
        print(dictionary)
        print("the word is deleted")

    elif choice==6:
        break

    else:
        print("choice is invalid!!")       
