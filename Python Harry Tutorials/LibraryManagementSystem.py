class Library:
    def __init__(self):
        self.__books = []
        self.__num_books = 0
    
    def add_book(self,name):
        self.__books.append(name)
        self.__num_books+=1
    
    def remove_book(self,name):
        update_books = list(filter(lambda x:x!=name,self.__books))
        self.__books = update_books
        self.__num_books-=1
                
    def check_books(self):
        if(self.__num_books==len(self.__books)):
            print(f"\nYour library is up to date with total {self.__num_books} books\n")
            for index,book in enumerate(self.__books):
                print(f"{index+1}. {book}")
        else:
            print("Your library system is not proper as it has some error calculating number of books")
            
lib = Library()
lib.add_book("Game Of Thrones")
lib.add_book("Death Note")
lib.add_book("3 idiots")

lib.remove_book("Game Of Thrones")

lib.check_books()