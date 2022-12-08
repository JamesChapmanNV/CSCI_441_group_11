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

def get_masseuses():
    try:
        command = ("Select masseuseId, name, address, email, phone "
                   "from masseuses ")
        mysqlManager.cursor.execute(command)

    except:
        print('error in get_masseuses Select')

    masseuses = []
    try:
        for masseuseId, name, address, email, phone in mysqlManager.cursor:
            # Creates an array within appointments array
            # one for each appointment/timeslot
            masseuses.append([masseuseId, name, address, email, phone])
    except:
        print('error in get_masseuses append')

    return masseuses

def get_masseuse_ID(name):
    try:
        data = (str(name),)
        command = ("Select masseuseId from masseuses "
                   "where name = %s ")
        mysqlManager.cursor.execute(command, data)

        mid = mysqlManager.cursor.fetchone()

    except:
        print('error in get_masseuse_ID ')

    if (mid[0]):
        return mid[0]
    return ''

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
