class Book:
    """ A class to represent a book in the library.
    
    Attributes:
    title(str): The title of the book.
    author (str): The author of the book.
    isbn(str): The unique ISBN of the book.
    """
    def __init__(self,title,auther,isbn):
        self.title=title
        self.auther=auther
        self.isbn=isbn
    def __str__(self):
        return f"Title: {self.title},Auther: {self.auther},ISBN: {self.isbn}"
class User:
    """A class to represent a user in the library.
    
    Attributes:
    name(str): The name of the user.
    user_id(int):The unique number of user.
    """ 
    def __init__(self,name,user_id):
        self.name=name
        self.user_id=user_id
        self.borrowed_books=[]
    def __str__(self):
        return f'User: {self.name} , ID: {self.user_id} , Borrowed Books: {len(self.borrowed_books)} '
user1=User("ali" , "101")
print(user1)
class Library:
    """A class to represent a library.
    
    """
    def __init__(self):
        self.users=[]
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added successful")
    def register_user(self,user):
        self.users.append(user)
        print(f"User '{user.name}' added successful")
    def find_book(self,isbn):
       for book in self.books:
            if book.isbn==isbn:
             return book
       return None
    def find_user(self,user_id):
        for user in self.users:
            if user.user_id==user_id:
             return user
        return None
    def borrow_book(self,user_id,isbn):
        user=self.find_user(user_id)
        book=self.find_book(isbn)
        if user is None or book is None:
            print("ERROR :Book or user not found")
            return
        else:
            user.borrowed_books.append(book)
            print(f"great! '{book.title}'borrowed by {user.name}")
    def return_book(self,user_id,isbn):
        user=self.find_user(user_id)
        book=self.find_book(isbn) 
        if user is None or book is None:
            print("ERROR :Book or user not found")
            return
        
        if book in user.borrowed_books:
            user.borrowed_books.remove(book)
            print(f"success! '{book.title}' returned by {user.name}")
        else:
            print(f"ERROR! {user.name} hasn't borrowed this book")
if __name__=="__main__":
    lib=Library()    
    book1=Book("Harry Potter" , "J.K. Rowling" ,"111")
    book2=Book("1984" ,"George Orwell" , "222")    
    
    user1 = User("Ali" , "101") 
    lib.add_book(book1)
    lib.add_book(book2) 
    lib.register_user(user1) 
    print("\n--- Testing Borrow---")
    lib.borrow_book("101" , "111")
    print(f"Ali's books count : {len(user1.borrowed_books)}")
    
    print("\n---Testing Return ---")
    lib.return_book("101" , "111")
    print(f"ali's books count : {len(user1.borrowed_books)}")
         
        
        
        
        
            
            
            
        
    
    
        
           