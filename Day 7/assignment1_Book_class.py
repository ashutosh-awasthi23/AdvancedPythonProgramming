class Book:
    # class variable
    number_of_copies_available = 10

    def __init__(self, t, a, y, av):
        self.title = t
        self.author = a
        self.__year = y
        self.__available = av

    @staticmethod
    def s_statement():
        return "Books are human's best friend"

    @classmethod
    def availability(cls):
        print(f"The number of copies available {cls.number_of_copies_available}")

    def change_year(self, year):
        self.__year = year
    
    def display(self):
        print(f"Author : {self.author}\nTitle :{self.title}\nYear :{self.__year}\nAvailable:{self.__available}")
        print()

    def borrow_book(self):
        if not self.__available:
            print(f"{self.title} is not available")
        else:
            print(f"{self.title} borrowed successfully")
            self.__available = False

    def return_book(self):
        self.__available = True
        print(f"{self.title} is available now")


book1 = Book("The Choice", "Edith Eager", 2017, True)
book2 = Book("The Ant", "Ashutosh", 2016, True)
# book1.display()
# book2.display()
# book1.borrow_book()
# book1.borrow_book()
# book1.return_book()
# Book.availability()
# print(f"\"{Book.s_statement()}\"")

book1.display()
# book1.__year = 1995
book1.change_year(1995)
book1.display()

