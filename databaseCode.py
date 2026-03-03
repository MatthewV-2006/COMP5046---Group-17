# import sqlite3

# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# #cur.execute("CREATE TABLE movie(title, year, score)")
# res = cur.execute("SELECT name FROM sqlite_master")
# print (res.fetchone())
# #res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# #res.fetchone() is None
# # with sqlite3.connect('database.db') as conn:
# #     # interact with database
# #     pass


import sqlite3
con = sqlite3.connect("Details.db")
cur = con.cursor()
#cur.execute("CREATE TABLE AccountDetails(AccountID, username, password, isAdmin)")
con.close()