import sqlite3 
  

class LMS:
    
    Book_ID=0
    BookName=''
    AuthorName=''
    NumberOfCopies=''
    
    
    def book_exists(self,cursor, book_id):
        cursor.execute("SELECT COUNT(*) FROM Book WHERE BookID=?", (book_id,))
        count = cursor.fetchone()[0]
        return count > 0

    def Add_Book(self):
        Database = sqlite3.connect("Project_database.db")
        cursor = Database.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS Book (BookID INTEGER PRIMARY KEY, Book_Name TEXT NOT NULL, Author_Name TEXT, Number_of_copies TEXT NOT NULL)")

        while True:
          try:
            self.Book_ID = int(input("Enter BookID: "))
            if self.Book_ID <= 0:
                print("Invalid input. BookID must be greater than 0.")
                continue
            break
          except ValueError:
            print("Invalid input. Please enter avalid integer value for the BookID.")

        if self.book_exists(cursor, self.Book_ID):
            print("This BookID already exists in the database.")
        else:
           self.BookName = input("Enter Book Name: ")
           self.AuthorName = input("Enter Author Name: ")
           self.NumberOfCopies = input("Enter Number of copies: ")

           cursor.execute("INSERT INTO Book (BookID, Book_Name, Author_Name, Number_of_copies) VALUES (?, ?, ?, ?)", (self.Book_ID, self.BookName, self.AuthorName, self.NumberOfCopies))
           print("Book added successfully!")

        Database.commit()
        Database.close()
        
        
        
    def Display_Books(self):
        Database = sqlite3.connect("Project_database.db")
        cursor = Database.cursor()
        cursor.execute("select * from Book")
        books = cursor.fetchall()
        
        if len(books) > 0:
            print("\nBooks in the database:\n")
            for book in books:
               print("BookID:", book[0])
               print("Book Name:", book[1])
               print("Author Name:", book[2])
               print("Number of Copies:", book[3])
               print("--------------------")
        else:
            print("No books found in the database.")
        
        Database.close()


    def Delete_Book(self):
        Database = sqlite3.connect("Project_database.db")
        cursor = Database.cursor()

        print("1. Delete one Book")
        print("2. Delete All Books")
        choice2 = int(input("Enter your choice: "))

        if choice2 == 1:
            self.Book_ID = int(input("Enter BookID: "))

            if self.book_exists(cursor, self.Book_ID):
                cursor.execute("DELETE FROM Book WHERE BookID=?", (self.Book_ID,))
                print("Book deleted successfully!")
            else:
                print("Book not found in the database.")
        elif choice2 == 2:
             confirm = input("Are you sure you want to delete all books? Enter (y) To confirm OR any character to cancel : ")

             if confirm == 'y' or confirm == 'Y':
                cursor.execute("DELETE FROM Book")
                print("All books deleted successfully!")
        else:
             print("Your choice is unavailable.")

        Database.commit()
        Database.close() 


    def Update_Book(self):
         Database = sqlite3.connect("Project_database.db")
         cursor = Database.cursor()

         try_again = 'y'

         while try_again == 'y' or try_again == 'Y':
             self.Book_ID = int(input("Enter the ID of the book you want to update: "))

             if self.book_exists(cursor, self.Book_ID):
                  self.BookName = input("Enter updated Book Name: ")
                  self.AuthorName = input("Enter updated Author Name: ")
                  self.NumberOfCopies = int(input("Enter updated Number of copies: "))

                  cursor.execute("UPDATE Book SET Book_Name=?, Author_Name=?, Number_of_copies=? WHERE BookID=?", (self.BookName, self.AuthorName, self.NumberOfCopies, self.Book_ID))
                  Database.commit()
                  print("Book updated successfully!")
                  try_again = 'N'
             else:
                  print("Book not found in the database.")
                  try_again = input("If you want to try again enter (y) else enter any character : ")
        

         Database.close()



    def Check_book(self):
         Database = sqlite3.connect("Project_database.db")
         cursor = Database.cursor()

         print("Check Book")
         self.Book_ID = int(input("Enter BookID: "))

         cursor.execute("SELECT * FROM Book WHERE BookID=?", (self.Book_ID,))
         result = cursor.fetchall()

         if len(result) > 0:
            print("Book exists in the database.")
         else:
           print("Book does not exist in the database.")

         Database.close()


optin='y'   
while(optin=='y' or optin=='Y'):  
    print("                                             Control Panel                     ")
    print("1\ Add Book")
    print("2\ Display Books")
    print("3\ Update Book")
    print("4\ Delete Books")
    print("5\ Check a book")
    print("6\ Exist from system")
    
    
    choise=int(input("please enter your choise : "))
    
    instance=LMS()
    
    if choise==1:
         instance.Add_Book()
    elif choise==2:
         instance.Display_Books()
    elif choise==3:
         instance.Update_Book()   
    elif choise==4:
         instance.Delete_Book()
    elif choise==5:
         instance.Check_book() 
    elif choise==6:
        print("Thank you for using our system")
        break; 
    else: 
         print("The choise you entered is not available")

    optin=input("Do you want to do something else ? enter (y) OR any character to Exist ")
    