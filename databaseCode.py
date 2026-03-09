import sqlite3
sqlDelete = 'DELETE FROM AccountDetails'
sqlGetID = 'SELECT AccountID from AccountDetails ORDER BY AccountID DESC LIMIT 1'
sqlGetrow = 'SELECT * from AccountDetails ORDER BY AccountID DESC'
sqlGetMax = 'SELECT MAX(CAST(AccountID AS INTEGER)) FROM AccountDetails'

sqlFulltable = 'SELECT * from AccountDetails'

with sqlite3.connect('Details.db') as con:
    cur = con.cursor()
    #cur.execute("CREATE TABLE AccountDetails(AccountID, username, password, isAdmin)")
    #cur.execute(sqlDelete)
    # cur.execute(sqlGetrow)
    # getId = cur.fetchone()[0]
    # print(getId)
    # Id = int(getId)
    # print(Id)

    cur.execute(sqlFulltable)
    FullTable = cur.fetchall()
    print(FullTable)

    cur.execute(sqlGetMax)
    highestID = cur.fetchone()[0]
    print(highestID)

    con.commit()
con.close()