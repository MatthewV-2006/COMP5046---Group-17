import sqlite3
con = sqlite3.connect("Details.db")
cur = con.cursor()
#cur.execute("CREATE TABLE AccountDetails(AccountID, username, password, isAdmin)")
con.close()