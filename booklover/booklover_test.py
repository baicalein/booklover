import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover=BookLover("Angie", "email@email", "Korean Novel")
        booklover.add_book("Human Acts", 5)
        self.assertIn("Human Acts", booklover.book_list['book_name'].values)
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover=BookLover("Angie", "email@email", "Korean Novel")
        booklover.add_book("Human Acts", 5)
        booklover.add_book("Human Acts", 5)
        self.assertEqual(booklover.book_list['book_name'].value_counts().get("Human Acts"),1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklover=BookLover("Angie", "email@email", "Korean Novel")
        booklover.add_book("Human Acts", 5)
        self.assertTrue(booklover.has_read("Human Acts"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover=BookLover("Angie", "email@email", "Korean Novel")
        booklover.add_book("Human Acts", 5)
        self.assertFalse(booklover.has_read("Gold"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklover=BookLover("Angie", "email@email", "Korean Novel")
        booklover.add_book("Human Acts", 5)
        booklover.add_book("Vegeterian", 5)
        booklover.add_book("White", 2)
        expect=3
        self.assertEqual(booklover.num_books_read(), expect)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover=BookLover("Angie", "email@email", "Korean Novel")
        booklover.add_book("Human Acts", 5)
        booklover.add_book("Vegeterian", 5)
        booklover.add_book("White", 2)
        fav_books = booklover.fav_books()
        expect= booklover.book_list[booklover.book_list['book_rating'] > 3]
        self.assertEqual(len(fav_books), len(expect))
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)