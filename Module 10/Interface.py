from abc import Abc, abstractmethod

class Printable(ABC):#THIS IS THE INTERFACE WITH ONLU ABSTRACT METHODS IN IT
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, tittle,author):
        self.tittle=tittle
        self.author=author

    def print_info(self):
        print(f"Book:{self.tittle} by {self.author}")

libri = Book("Hija e maleve","Ismail Kadare")
libri.print_info()
