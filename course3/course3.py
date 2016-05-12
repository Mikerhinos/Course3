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
    
def enter_dynamic_data():
    lang = input("What language ? : ")
    version = float(input("What version ? : "))
    skill = input("What skill level ? : ")
    c.execute("INSERT into example (Language, Verions, Skill) VALUES (?,?,?)", (lang,version,skill))
    conn.commit()
    
def read_from_database():
    what_skill = input("What skill ? : ")
    what_language = input("What language ? : ")
    #Alternative with concatenate way :
    #sql = "SELECT * FROM example WHERE Skill = '"+what_skill+"' AND Language = '"+what_language+"'"
    #for row in c.execute(sql):
    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"
    for row in c.execute(sql,[(what_skill),(what_language)]):
        print(row)
    
read_from_database()


conn.close()