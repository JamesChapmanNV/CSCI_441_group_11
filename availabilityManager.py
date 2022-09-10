import mysqlManager


def insert_availability(masseuseId,dow,start,end): 
    try:
        data = (str(masseuseId),str(dow),str(start),str(end))
        insertCommand = ("INSERT IGNORE INTO masseuseavailability(masseuseId,dow,start,end) "
                        "VALUES (%s, %s, %s, %s)")
        mysqlManager.cursor.execute(insertCommand, data)
        mysqlManager.connection.commit()  
    except:
        print('error in insert_availability')

def delete_availability(masseuseId): 
    try:
        command = ("DELETE FROM masseuseavailability where masseuseId = %s" % masseuseId)
        mysqlManager.cursor.execute(command)
        mysqlManager.connection.commit()  
    except:
        print('error in delete_availability')

def get_availability(start_time): 
    try:
        hour = start_time.strftime("%H")
        data = (str(start_time), str(hour), str(hour))
        command = ("Select masseuseId from masseuseavailability "
                "where ( dow = DAYOFWEEK(%s) and start <= %s "
                "and end > %s )")
        mysqlManager.cursor.execute(command, data)
        mysqlManager.connection.commit()  
    except:
        print('error in get_availability Select')
    
    available = []
    try:
        for masseuseId in mysqlManager.cursor:
            # Creates an array within appointments array
            # one for each appointment/timeslot
            available.append(masseuseId)
    except:
        print('error in get_availability append')
       
    return available