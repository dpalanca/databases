import sqlite3

# get person data from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
person_data = (first_name, last_name, age)

people_values = (
			('Ron', 'Obvious', 42),
			('Luigi', 'Vercotti', 43),
			('Arthur', 'Belling', 28)
	)

# execute insert statement for supplied person data
"""
with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.execute("INSERT INTO People VALUES(?, ?, ?)", person_data)
	c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?", (45, 'Luigi', 'Vercotti'))
	connection.close()
"""

with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.execute("DROP TABLE IF EXISTS People")
	c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
	c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
	# select all first and last names from people over age 30
	c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
	# fetchall() fetches the results of the SELECT query
	for row in c.fetchall():
		print(row)
	
	print("All entries:")
	c.execute("SELECT FirstName, LastName FROM People")

	while True:
		row = c.fetchone()
		if row is None:
			break
		print(row)