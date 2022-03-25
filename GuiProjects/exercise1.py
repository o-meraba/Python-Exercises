import sqlite3


con = sqlite3.connect("library.db")
cursor = con.cursor()

def table_create():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookself(Name TEXT, Author TEXT, Publisher TEXT, Pages INT)")
    con.commit()
def add_values_to_library(name, author, publisher, pages):
    cursor.execute("INSERT INTO bookself VALUES(?,?,?,?)",(name,author,publisher,pages))
    con.commit()
def get_values():
    cursor.execute("SELECT * FROM bookself")
    data = cursor.fetchall()
    print("kitaplık tablosunun bilgileri...")
    for i in data:
        print(i)

# name = input("Name: ")
# # author = input("Author")
# # publisher = input("Publisher:")
# # pages = int(input("Pages:"))
# # table_create()
# # add_values_to_library(name,author,publisher,pages)
get_values()
con.close()