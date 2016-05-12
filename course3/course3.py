import sqlite3

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Verions REAL, Skill TEXT)")
    
def enter_data():
    c.execute("INSERT into example VALUES ('Python',2.7,'Beginner')")
    c.execute("INSERT into example VALUES ('Python',3.3,'Intermediate')")
    c.execute("INSERT into example VALUES ('Python',3.5,'Expert')")
    conn.commit()
    
    
enter_data()


#conn.close()