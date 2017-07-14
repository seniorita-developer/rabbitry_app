import sqlite3

def connect():
    conn=sqlite3.connect("rabbits.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS rabbit (id INTEGER PRIMARY KEY, name text, date_of_birth text, "
                "sex text, sterilisation text,adopted text, owner text, adress text)")
    conn.commit()
    conn.close()

def insert(name, date_of_birth, sex, sterilisation,adopted, owner, adress):
    conn = sqlite3.connect("rabbits.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO rabbit VALUES (NULL,?,?,?,?,?,?,?)",(name, date_of_birth, sex, sterilisation,adopted, owner, adress))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("rabbits.db")
    cur = conn.cursor()
    cur.execute("SELECT * from rabbit")
    rows=cur.fetchall()
    conn.close()
    return rows

def search (name="", date_of_birth="", sex="", sterilisation="", adopted="", owner="", adress=""):
    conn = sqlite3.connect("rabbits.db")
    cur = conn.cursor()
    cur.execute("SELECT * from rabbit WHERE name=? OR date_of_birth=? OR sex=? OR sterilisation=? "
                "OR adopted=? OR owner=? OR adress=?", (name, date_of_birth, sex, sterilisation,adopted, owner, adress))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("rabbits.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM rabbit WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name, date_of_birth, sex, sterilisation,adopted, owner, adress):
    conn = sqlite3.connect("rabbits.db")
    cur = conn.cursor()
    cur.execute("UPDATE rabbit SET name=? , date_of_birth=? , sex=?, sterilisation=? , adopted=? , owner=?, "
                "adress=? WHERE id=?", (name, date_of_birth, sex, sterilisation,adopted, owner, adress,id))
    conn.commit()
    conn.close()


connect()
#insert("Klapo",01.2016,"Male","No","Yes","Mama","21 Long Street,NY")

#print(search(name="Piko"))
#delete(6)

#update(3,"Klapouch",4.2016,"Male","No","Yes","Mama","21 Long Street,NY")
#print(view())