import sqlite3
sqlDelete = 'DELETE FROM AccountDetails'
with sqlite3.connect('Details.db') as con:
    cur = con.cursor()
    #cur.execute("CREATE TABLE AccountDetails(AccountID, username, password, isAdmin)")
    cur.execute(sqlDelete)
    con.commit()
con.close()