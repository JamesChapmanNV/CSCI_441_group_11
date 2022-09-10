import mysqlManager


def insert_appointment(start_time,room,status,masseuseId,customerId): 
    try:
        data = (str(start_time),str(room),status,str(masseuseId),str(customerId))
        insertCommand = ("INSERT IGNORE INTO appointments(start_time,room,status,masseuseId,customerId) "
                        "VALUES (%s, %s, %s, %s, %s)")
        mysqlManager.cursor.execute(insertCommand, data)
        mysqlManager.connection.commit()  
    except:
        print('error in insert_appointment')

def delete_appointment(appointmentId): 
    try:
        command = ("DELETE FROM appointments where appointmentId = %s" % appointmentId)
        mysqlManager.cursor.execute(command)
        mysqlManager.connection.commit()  
    except:
        print('error in delete_appointment')

def update_appointment(appointmentId,status,masseuseId,customerId): 
    try:
        data = (status,str(masseuseId),str(customerId),str(appointmentId),)
        command = ("Update appointments set status = %s, "
            "masseuseId = %s, customerId = %s, where (appointmentId = %s)")

        mysqlManager.cursor.execute(command, data)
        mysqlManager.connection.commit()  
    except:
        print('error in update_appointment')

def get_appointments(date): 
    try:
        data = (str(date), )
        command = ("Select appointmentId, start_time, room, status, masseuseId, customerId "
                "from appointments where ( DATE(start_time) = %s )")
        mysqlManager.cursor.execute(command, data)
        mysqlManager.connection.commit()  
    except:
        print('error in get_appointments Select')
    
    appointments = []
    try:
        for appointmentId, start_time, room, status, masseuseId, customerId in mysqlManager.cursor:
            # Creates an array within appointments array
            # one for each appointment/timeslot
            appointments.append([appointmentId, start_time, room, status, masseuseId, customerId])
    except:
        print('error in get_appointments append')
       
    return appointments
