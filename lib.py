class Library:
    def __init__(self,book_name,author):
        self.book_name=book_name
        self.author=author
        self.is_available=True
        
    def check_out(self):
        if self.is_available:
            self.is_available=False
            print(f"'{self.book_name}'has been checked out")
        else:
            print(f"Sorry,'{self.book_name}'is already checked out")
                
        def return_book(self):
                    if not self.is_available:
                        self.is_available=True
                        print(f"'{self.book_name}'has been returned.")
                    else:
                        print(f"'{self.boo_name}'was not checked out.")
                        
                        def display_book(self):
                            status="Available"if self.is_avaiable else "Not available"
                            print(f"Book Name: {self.book_name}")
                            print(f"Author:{self.author}")
                            print(f"Status")
                            print("-"*30)
                             
                            #-----------main programme------------
                            book1=Library("Python Programming","Guido van Rossum")
                            book2=Library("C++ Programming","Bjarne Stroustrup")
                            
                            #------------display books--------------- 
                            book1.display_book()
                            book2.display_book()
                            
                            #check out a book
                            book1.check_out()
                            book2.check_out()
                            
                            #return the book
                            book1.return_book()
                            book2.return_book()