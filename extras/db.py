import sqlite3


stocks = [
    ("GOOG", 100, 490.1),
    ("AAPL", 50, 545.75),
    ("FB", 150, 7.45),
    ("HPQ", 75, 33.2),
]

db = sqlite3.connect("./helper_files/test.db")

cursor = db.cursor()
try:
    cursor.execute("create table portfolio (symbol text, shares integer, price real)")
except sqlite3.OperationalError:
    pass

# cursor.executemany("insert into portfolio values(?, ?, ?)", stocks)

for row in cursor.execute("select symbol, shares from portfolio where price >=500"):
    print(row)
db.commit()
db.close()
