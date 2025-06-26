class library_managment_system:
    def _init_(self, book_name, page_no, total_stock):
        self.book_name = book_name
        self.page_no = page_no
        self.__total_stock = total_stock

    def withdrawal(self,amount):
        self.__total_stock -= amount
        print(f"{amount} of books withdrawn,current amount of books:{self.__total_stock}")
    def deposit(self,amount):
        self.__total_stock += amount
        print(f"{amount} books deposited:{self.__total_stock}")
    def __book_details(self):
        print(f"book_name:{self.book_name}")
        print(f"page_no:{self.page_no}")
        print(f"total_stock:{self.__total_stock}")
    def show_details(self):
        self.__book_details()
book1=library_managment_system(book_name="merchant of wings",page_no=989,total_stock=100)
book1.withdrawal(amount=10)
book1.deposit(amount=123)
book1.show_details()