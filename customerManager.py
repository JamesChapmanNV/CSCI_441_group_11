import mysqlManager


def insert_customer(infos): 
    try:
        data = (infos)
        insertCommand = ("INSERT IGNORE INTO draftGroups(infos) "
                        "VALUES (%s, %s, %s, %s)")
        
        mysqlManager.cursor.execute(insertCommand, data)
        mysqlManager.connection.commit()  
    except:
        print('error in insert_customer')