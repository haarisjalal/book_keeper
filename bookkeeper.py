class book(object):
    def __init__(self, title, author):
        self.author = author
        self.title = title
        
def addBook(bookList):
    title = input('What is the name of the book?\n')
    author = input("What is the author's name?\n")
    bookList.append(book(title.upper(), author.title())) #title() capitalizes each word
    
def listBook(bookList):
    for i in bookList:
        print("\"%s\", by %s\n" % (i.title, i.author))
        
def readBooks(bookList):
    bList = []
    f = open(input("Enter the filename."))
    for line in f:
        comma = line.find(",")
        title = line[0:comma].rstrip(',') #substring 1
        author = line[comma+1:].stirp()
        bList.append(book(title.upper(), author.title()))
        if userInput == "yes":
            for i in bList:
                bookList.append(i)
            print("Saved")
        else:
            print("Not Saved")
    f.close()
    
def writeToNew(bookList):
    userInput = input("Enter the filename you'd like to export to.")
    f = open(userInput, 'w') # The w indicates that we are writing to the file
    for i in bookList:
        f.write("%s, %s\n" % (i.title.upper(), i.author.title()))
    f.close()
    
def writeToExisting(bookList):
    userInput = input("Enter the file you'd like to add to")
    f = open(userInput, 'a') # a means that we are appending to the file
    for i in bookList:
        f.write("%s, %s\n" %(i.title.upper(), i.author.title()))
    f.close()
    
bookList = []
running = True

while running == True:
    print("Welcome to Book Keeper\n")
    print("\t\"ADD\" to add a book to your temp list")
    print("\t\"LIST\" to read out your temp list")
    print("\t\"READ\" to read an existing file")
    print("\t\"SAVE\" to save to a new file")
    print("\t\"SAVE EXISTING\" to save to an existing file")
    print("\t\"CLEAR\" to clear your temporary file")
    print("\t\"EXIT\" to exit")
    
    userInput = input()
    if userInput.lower() == "add":
        addBook(bookList)
    elif userInput.lower() == "list":
        listBook(bookList)
    elif userInput.lower() == "read":
        readBooks(bookList)
    elif userInput.lower() == "save new":
        writeToNew(bookList)
    elif userInput.lower() == "save existing":
        writeToExisting(bookList)
    elif userInput.lower() == "clear":
        bookList = []
    elif userInput.lower() == "exit":
        running = False
    else:
        print("The command was invalid")
        
