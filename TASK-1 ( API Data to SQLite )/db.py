import sqlite3

class  Database:
    def __init__(self):
        self.con = sqlite3.connect('Product.db')
        self.cur = self.con.cursor()
        
    def createTable(self):
        # Create table Products (ID INT PRIMARY KEY, Name TEXT NOT NULL, Price REAL)
        self.cur.execute("CREATE TABLE IF NOT EXISTS Products(ID INTEGER PRIMARY KEY ,title TEXT NOT NULL, price REAL, brand TEXT NOT NULL, category TEXT NOT NULL)")

    def insertProducts(self,products):
        data = []
        for product in products:
            id = product["id"]
            title = product["title"]
            price = product["price"]
            brand = product["brand"]
            category = product["category"]
            data.append((id, title, price, brand, category))
        self.con.executemany("INSERT INTO Products VALUES (?,?,?,?,?)",data)
        self.con.commit()

    def getAllProducts(self):
        res = self.cur.execute("SELECT * FROM Products")
        entry = res.fetchall()
        return entry