import pandas as pd

class BookLover():
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
        self.num_books=num_books
        self.book_list=book_list if book_list is not None else pd.DataFrame({'book_name':[],'book_rating':[]})
    
    
    def add_book(self, book_name, rating):
        if book_name in list(self.book_list['book_name'].values):
            print(f"{book_name} is already in the book list")
        else:
            new_book=pd.DataFrame({'book_name':[book_name], 'book_rating':[rating]})
            self.book_list=pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books +=1
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    def num_books_read(self):
        return self.num_books
    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]
    
# test my BookLover class directly in the .py file
if __name__ == '__main__':
    
    #test
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 2)
    test_object.add_book("Human Acts", 5)
    test_object.add_book("Vegeterian", 5)
    
    print(test_object.book_list)
    print("Has you read 'Vegeterian'?:", test_object.has_read("Vegeterian"))
    print("Number of books read:", test_object.num_books_read())
    print("Favorite books:", test_object.fav_books())
        