#createDatabase.py
# Python code to demonstrate table creation and  
# insertions with SQL 
  
# importing module 
import sqlite3 

# connecting to the database  
connection = sqlite3.connect("ActionCastle.db") 
  
# cursor  
crsr = connection.cursor() 
  
# SQL command to create a table in the database 
sql_command = "DROP TABLE IF EXISTS Locations;"
crsr.execute(sql_command)

sql_command = """
CREATE TABLE IF NOT EXISTS Locations (  
    lID VARCHAR(20) PRIMARY KEY,  
    lName VARCHAR(20),  
    lDescription VARCHAR(30),  
    lEndGame BIT
    );
"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO Locations(lID, lName, lDescription, lEndGame)
    VALUES
    ('LOCATION_COTTAGE','Cottage','You are standing in a small cottage & I am testing the fucking database', 0),
    ('LOCATION_GARDEN_PATH', 'Garden Path', 'You are standing on a lush garden path. There is a cottage here.', 0),
    ('LOCATION_CLIFF', 'Cliff', 'There is a steep cliff here. You fall off the cliff and lose the game. THE END.', 0),
    ('LOCATION_FISHING_POND', 'Fishing Pond', 'You are at the edge of a small fishing pond.', 0);
"""
crsr.execute(sql_command)


# SQL command to insert the data in the table 
# sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
# crsr.execute(sql_command) 
  
# another SQL command to insert the data in the table 
# sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
#crsr.execute(sql_command) 
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 