import csv                                              
print("======LIBRARY MANAGEMENT SYSTEM======")
library=[]

# Load existing library data from CSV file
try:
    f=open("library.csv","r")
    rd=csv.reader(f)
    for i in rd:
        if not i:
            continue
        if i[0]=="ID":
            continue
        
        book = {"ID": int(i[0]),
                "BName": i[1],
                "Author": i[2],
                "Genre": i[3],
                "Availability": i[4]}
        library.append(book)
    f.close()
        
except FileNotFoundError:
    print("No existing library data found. Starting with an empty library.")
    
# Save current library data to CSV file
def save_data():                                        
    f=open("library.csv","w")
    wr=csv.writer(f)
    wr.writerow(['ID','BName','Author','Genre','Availability'])
    for book in library:
        wr.writerow([
            (book['ID']),
            (book['BName']),
            (book['Author']),
            (book['Genre']),
            (book['Availability'])
            ])
          
    f.close()
    
# Main program loop        
while True:                                               
    print("=====================================")
    print("=======LIBRARY MANAGEMENT MENU=======")
    print("=====================================")
    print("1. Add book")
    print("2. View books")
    print("3. Search books")
    print("4. Issue book")
    print("5. Return book")
    print("6. Delete book")
    print("7. Update book")
    print("8. Exit")
    print("======================================")
    choice=int(input("Enter your choice(1-8):"))
    
    # Add a new book
    if choice==1:
        book_id=int(input("Enter book id:"))
        found=False
        for book in library:
            if book_id==book['ID']:
                found=True
                break
        if found:
            print("Book ID already exists.Cannot add other book.")
        else:
            book_name=input("Enter book name:")
            author_name=input("Enter author name:")
            genre=input("Enter genre:")
            status=input("Enter status(issued/available):")
            book={"ID":book_id ,"BName":book_name ,"Author":author_name ,"Genre":genre ,"Availability":status }
            library.append(book)
            print("Book added successfully")
            save_data()


    # View all books and library statistics
    elif choice==2:
        if not library:
            print("library is empty")
        else:
            count_available=0
            count_issued=0
            print("\nID | BName | Author | Genre | Availability")
            print("===============================================")
            for book in library:
                print(book['ID'], "|", book['BName'], "|", book['Author'], "|", book['Genre'], "|", book['Availability'])
                if book['Availability'] == 'available':
                    count_available += 1
                elif book['Availability'] == 'issued':
                    count_issued += 1
            print("===============================================")
            print("Total books:", len(library))
            print("Available books:", count_available)
            print("Issued books:", count_issued) 


    # Search a book by ID or name           
    elif choice==3:
        search_id=int(input("Enter book_id to search:"))
        search_name=input("Enter book_name to search:")
        found=False
        
        for book in library:
            if search_id==book['ID'] or search_name==book['BName']:
                print("Book found")
                print('ID:',book['ID'])
                print('Bname:',book['BName'])
                print('Author:',book['Author'])
                print('Genre:',book['Genre'])
                print('Availability:',book['Availability'])
                found=True
                break
            
        if not found:
                print("Book not found")


    # Issue a book            
    elif choice==4:
        issue_id=int(input("Enter book_id to issue:"))
        found=False
        
        for book in library:
            if issue_id==book['ID']:
                print("book found")
                found=True
                if book['Availability']=='issued':
                    print("Book already issued")
                else:
                    book['Availability']='issued'
                    print("Book issued successfully")
                save_data()
                break
    
        if not found:
                print("Book not found")
                

    # Return a book
    elif choice==5:
        return_id=int(input("Enter book_id to return:"))
        found=False
        
        for book in library:
            if return_id==book['ID']:
                print("Book found")
                found=True
                if book['Availability']=='available':
                    print("Book is already available")
                else:
                    book['Availability']='available'
                    print("Book returned successfully")
                save_data()
                break
    
        if not found:
                print("Book not found")


    # Delete a book with confirmation                
    elif choice==6:
        delete_id=int(input("Enter book_id to delete:"))
        found=False
        for book in library:
            if delete_id==book['ID']:
                ch=input("Are you sure (Y/N)")
                if ch in "Yy":
                    library.remove(book)
                    print("Book deleted successfully")
                    save_data()
                else:
                    print("Deletion cancelled")
                found=True
                break
        if not found:
                print("Book not found")


    # Update book details            
    elif choice==7:
        update_id=int(input("Enter book_id to update:"))
        found=False
        for book in library:
            if update_id==book['ID']:
                print("Book found")
                found=True
                choice_1=int(input("What do you want to update?\n"
                                 "1.Name\n"
                                 "2.Author\n"
                                 "3.Genre\n"
                                 "Enter your choice:"))
                if choice_1==1:
                    new_name=input("Enter new book name:")
                    book['BName']=new_name
                    print("Book name updated successfully")

                elif choice_1==2:
                    new_author=input("Enter new author name:")
                    book['Author']=new_author
                    print("Author name updated successfully")

                elif choice_1==3:
                    new_genre=input("Enter new genre:")
                    book['Genre']=new_genre
                    print("Genre updated successfully")

                else:
                    print("Invalid update choice")

                save_data()
                break
        if not found:
            print("Book not found")


    # Exit the program                        
    elif choice==8:
        print("Thank you for using LIBRARY MANAGEMENT SYSTEM")
        break

    else:
        print("invalid choice")

    
