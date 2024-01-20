class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def set_details(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"
    

# Create a book instance
book1 = Book("Sherlock Holmes", "Harper Lee", "Fiction")

# Set details
book1.set_details("1984", "George Orwell", "Dystopian")

# Display details
print(book1.display_details())