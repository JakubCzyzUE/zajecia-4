class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Biblioteka w {self.city}, adres: {self.street} {self.zip_code}, telefon: {self.phone}, godziny otwarcia: {self.open_hours}'


class Order:
    def __init__(self, employee: str, student: str, books: str, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f'dane zamówienia:  Pracownik: {self.employee}   Student: {self.student}   Książki: {self.books}    data zamówienia: {self.order_date}'


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f'dane pracownika:  Imie: {self.first_name} Nazwisko: {self.last_name} Data zatrudnienia: {self.hire_date} Data urodzenia: {self.birth_date}' \
               f' Miasto: {self.city} Ulica: {self.street} Kod pocztowy: {self.zip_code} telefon kontaktowy: {self.phone}'
class Book:
    def __init__(self, library: str, publication_date: str, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f'dane książki:  biblioteka: {self.library}, data publikacji: {self.publication_date}, imie autora: {self.author_name}' \
               f' nazwisko autora: {self.author_surname}, liczba stron: {self.number_of_pages}'

    l1 = Library('Katowice', 'Szkolna', '40-000', 'od 8 do 20', 732332132)
    print(l1.__str__())

    o1 = Order("K.Nowak", "Jacek Kowalski", "Księga Dżungli, Harry Potter", "10.10.2021")
    print(o1.__str__())

    e1 = Employee("Jarek", "Nowak", "10.12.2019", "10.01.1994", "Katowice", "Bogucicka", "40-000", 730321123)
    print(e1.__str__())

    b1 = Book("Katowice","10.10.1990","John","Doe",100)
