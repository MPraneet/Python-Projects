 # create a library class
# display book #lend book
# add book
# return book

# Harry library = library(listofbooks , library_name)
# dictionary (books-nameofpersons)
# create a main function and run an infinite while loop asking users for their inputs
# Users for their input

class Library:
    def __init__(self,list,name):
        self.bookslist = list
        self.name = name
        self.lendDict ={}

    def displayBooks(self):
        print(f"We have following books in our Library:{self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self,users,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book database has been updated. You can take book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.bookslist.append(book)
        print("Book has been added to the book-list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['python','Rich-daddy','Harry-Potter','C++ basics','Java Basics'],"CodeWithHarry")
    while(True):
        print(f"Welcome to the {harry.name}library. Enter your choice to continue  ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book \n")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            continue
        else:
            user_choice =int(user_choice)


        if user_choice==1:
            harry.displayBooks()
        elif user_choice==2:
            book= input("Enter a input you want to lend:")
            user=input("Enter your name:")
            harry.lendBook(user,book)
        elif user_choice==3:
            book=input("Enter the book you want to add:")
            harry.addBook(book)
        elif user_choice==4:
            book=input("Enter the book you want to return:")
            harry.returnBook(book)
        else:
            print("Not a valid Option.")

        user_choice2=" "
        print("Press q to quit and c to continue")
        if user_choice2=="q":
            exit()
        elif user_choice2=="c":
            continue
