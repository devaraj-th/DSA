class Library:

    total_number_of_books = 0

    def __init__(self):
        self.books = []
    
    def add_book(self,title,author):
        print(f"The book is added to the library {title} and author of the book{author}")
        self.books.append({'title':title,'author':author})
        Library.total_number_of_books +=1
    def remove_book(self,title):
        print(f'the book is removed from the library {title}')
        Library.total_number_of_books -=1
        

    def display_books(self):
        for book in self.books:
            print(book)


    @staticmethod
    def get_total_books():

        print(Library.total_number_of_books)


library1 = Library()
library2 = Library()

library1.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library1.add_book("1984", "George Orwell")

library2.add_book("To Kill a Mockingbird", "Harper Lee")

print("Library 1 Books:")
library1.display_books()

print("\nLibrary 2 Books:")
library2.display_books()

print("\nTotal Books Across All Libraries:")
print(Library.get_total_books())  # Should output 3

library1.remove_book("1984")
print("\nTotal Books Across All Libraries After Removal:")
print(Library.get_total_books())  # Should output 2

    


        