import sqlite3
con = sqlite3.connect("Details.db")
cur = con.cursor()
#cur.execute("CREATE TABLE AccountDetails(AccountID, username, password, isAdmin)")
sql = 'DELETE FROM AccountDetails WHERE AccountID = ?'
cur.execute(sql, (0,))
con.commit()
con.close()