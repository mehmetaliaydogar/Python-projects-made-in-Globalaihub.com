class Library:
    def __init__(self, book_name, author, release_date, number_of_pages):
        self.book_name = book_name
        self.author = author
        self.release_date = release_date
        self.number_of_pages = number_of_pages

    def list_books(self):
        with open("books.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(f"Book Name: {line.split(',')[0]}, Author: {line.split(',')[1]}, Release Date: {line.split(',')[2]}, Number Of Pages: {line.split(',')[3]}")


    def add_book(self):
        with open("books.txt", "a+") as file:
            file.write(f"{self.book_name},{self.author},{self.release_date},{self.number_of_pages}\n")


    def delete_book(self):
        with open("books.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if self.book_name not in line:
                    file.write(line)

def lib():
    while True:
        print("***MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("q) Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book = Library("", "", "", "")
            book.list_books()

        elif choice == "2":
            book_name = input("Book Name: ")
            author = input("Author: ")
            release_date = input("Release Date (Year): ")
            number_of_pages = input("Number Of Pages: ")

            book = Library(book_name, author, release_date, number_of_pages)
            book.add_book()

        elif choice == "3":
            book_name = input("Enter the book title to remove: ")

            book = Library(book_name, "", "", "")
            book.delete_book()

        elif choice == "q":
            break

        else:
            print("Invalid Selection!")

if __name__ == "__main__":
    lib()

