import sqlite3
con = sqlite3.connect("Details.db")
cur = con.cursor()
#cur.execute("CREATE TABLE AccountDetails(AccountID, username, password, isAdmin)")
cur.execute("DELETE FROM AccountDetails WHERE AccountID = 0")
con.close()