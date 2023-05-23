listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (type exit to leave and see the list): ")
    if newWord == "":
        break
    elif newWord == "exit":
        print(listToPrint, sep=",")
    else:
        listToPrint.append(newWord)

