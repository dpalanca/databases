import sqlite3

connection = sqlite3.connect("test_database.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()
# delete the table
# c.execute("DROP TABLE IF EXISTS People")
connection.close()

with sqlite3.connect("test_database.db") as connection:
	c.execute("INSERT INTO People VALUES('John', 'Doe', 21)")
	connection.close()

with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.executescript("""
		DROP TABLE IF EXISTS People;
		CREATE TABLE People(FirstName TEXT, LastName TEST, Age INT);
		INSERT INTO People VALUES('Ron', 'Obvious', '42');
	""")
	connection.close()

people_values = (
			('Ron', 'Obvious', 42),
			('Luigi', 'Vercotti', 43),
			('Arthur', 'Belling', 28)
)

with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)