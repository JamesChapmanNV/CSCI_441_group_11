from src import mysqlManager
from datetime import datetime, timedelta, date


def insert_appointment(start_time, room, status, masseuseId, customerId):
    try:
        data = (str(start_time), str(room), status, str(masseuseId), str(customerId))
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


def update_appointment(appointmentId, status, masseuseId, customerId):
    try:
        data = (status, str(masseuseId), str(customerId), str(appointmentId),)
        command = ("Update appointments set status = %s, "
                   "masseuseId = %s, customerId = %s, where (appointmentId = %s)")

        mysqlManager.cursor.execute(command, data)
        mysqlManager.connection.commit()
    except:
        print('error in update_appointment')


def get_appointments(date):
    try:
        data = (str(date),)
        command = ("Select appointmentId, start_time, room, status, masseuseId, customerId "
                   "from appointments where ( DATE(start_time) = %s )")
        mysqlManager.cursor.execute(command, data)

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


def get_future_booked_appointments():
    now = datetime.now()
    curHour = (hour_rounder(now))
    try:
        data = (str(curHour),)
        command = ("Select appointmentId, start_time, room, status, masseuseId, customerId "
                   "from appointments where ( start_time >= %s ) ORDER BY start_time")
        mysqlManager.cursor.execute(command, data)
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


def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
            + timedelta(hours=t.minute // 30))