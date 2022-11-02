from src import mysqlManager


def insert_masseuse(masseuseId,name,address,email,phone): 
    try:
        data = (str(masseuseId),name,address,email,str(phone))
        insertCommand = ("INSERT IGNORE INTO masseuses(masseuseId,name,address,email,phone) "
                        "VALUES (%s, %s, %s, %s, %s)")
        mysqlManager.cursor.execute(insertCommand, data)
        mysqlManager.connection.commit()  
    except:
        print('error in insert_masseuse')

def delete_masseuse(masseuseId): 
    try:
        command = ("DELETE FROM masseuses where masseuseId = %s" % masseuseId)
        mysqlManager.cursor.execute(command)
        mysqlManager.connection.commit()  
    except:
        print('error in delete_masseuse')

def get_masseuse_name(masseuseId): 
    try:
        data = (str(masseuseId), )
        command = ("Select name from masseuses "
                "where masseuseId = %s ")
        mysqlManager.cursor.execute(command, data)
    except:
        print('error in get_masseuse Select')
    
    name = mysqlManager.cursor.fetchone()
    #returns an tuple ('name',)
    #Access name string at index 0
    return name[0]

def get_all_masseuse_names(): 
    try:
        command = ("SELECT distinct name FROM masseuses")
        mysqlManager.cursor.execute(command)
    except:
        print('error in get_all_masseuse_names ')
    
    names = [] #= mysqlManager.cursor.fetchall()
    for masseuse in mysqlManager.cursor:
        names.append(masseuse[0])

    return names
