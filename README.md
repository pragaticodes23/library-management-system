# Library Management System (Python Project)

A beginner-friendly Python console-based Library Management System that allows users to manage books efficiently using CSV file storage. The system supports adding, viewing, searching, issuing, returning, updating, and deleting books while automatically saving data between program runs.

## Features

• Add new books to the library
• View all books in a formatted table
• Search books by Book ID or Book Name
• Issue books to users
• Return issued books
• Update book details (Name, Author, Genre)
• Delete books with confirmation
• Prevent duplicate Book IDs
• View library statistics:

* Total books
* Available books
* Issued books
  • Automatic data saving using CSV files
  • Automatic data loading when the program starts
  • Handles missing CSV file gracefully

## Concepts Used

• Variables
• Functions
• Loops (for loop, while loop)
• Conditional statements (if-elif-else)
• Lists
• Dictionaries
• File Handling (CSV)
• Exception Handling (FileNotFoundError)
• User Input Handling
• CRUD Operations (Create, Read, Update, Delete)

## 💻 Sample Run

📚 Library Menu

```text
====== LIBRARY MANAGEMENT MENU ======

1. Add Book
2. View Books
3. Search Books
4. Issue Book
5. Return Book
6. Delete Book
7. Update Book
8. Exit
```

📖 Add Book

```text
Enter book id: 101
Enter book name: Atomic Habits
Enter author name: James Clear
Enter genre: Self Help

Book added successfully
```

🔍 Search Book

```text
Enter book_id to search: 101

Book found

ID: 101
BName: Atomic Habits
Author: James Clear
Genre: Self Help
Availability: available
```

📚 Issue Book

```text
Enter book_id to issue: 101

Book found
Book issued successfully
```

✏️ Update Book

```text
Enter book_id to update: 101

Book found

1. Name
2. Author
3. Genre

Enter your choice: 2

Enter new author name: J. Clear

Author name updated successfully
```

📊 Library Statistics

```text
Total books: 10
Available books: 7
Issued books: 3
```

## 🎯 Purpose

This project was built to strengthen core Python programming concepts such as file handling, dictionaries, functions, loops, conditionals, CRUD operations, and data persistence by simulating a real-world Library Management System.

## 👩‍💻 Author

Pragati
