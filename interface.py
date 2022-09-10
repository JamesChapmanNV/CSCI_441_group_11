import mysqlManager
import customerManager
import masseuseManager
import appointmentManager
import availabilityManager

"""  mysqlManager.create_tables(mysqlManager.cursor)
"""

# Gather info from user to create a new customer
customerManager.insert_customer(customerId,name,address,email,phone)

# Gather info from user to create a new masseuse
masseuseManager.insert_masseuse(masseuseId,name,address,email,phone)

# Gather info from user About a masseuse
# Note: 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday.
# Go through each week day (int, 2 – 6), 
# ask for start time (int, 0 – 23), end time (int, 0 – 23), or skip day of the week
# end time > start time
availabilityManager.insert_availability(masseuseId,dow,start,end)

# Populate appointments let's say 8 weeks out
# 8 start times should be created for each day (9a to 5p)
# each start time should have 3 rooms
# this creates empty appointments with status OPEN
# insert_appointment(start_time,room,status,masseuseId,customerId)
appointmentManager.insert_appointment(start_time,room,"OPEN",NULL,NULL)

# Use to book or cancel appointment
# update_appointment(appointmentId,status,masseuseId,customerId)
appointmentManager.update_appointment(appointmentId,"BOOKED",masseuseId,customerId)
    # Cancel APPT
appointmentManager.update_appointment(appointmentId,"OPEN",NULL,NULL)

# ! This might logically be the start (when you open the program)
# ask customer which day they want to book/cancel
# Returns all appointments for that day (each hour, each room)
appointmentManager.get_appointments(date)

# returns array of masseuseId that are available for each appointment
availabilityManager.get_availability(start_time)
# if(empty)
#   start_time does not have any available masseuses

# to display names use
customerManager.get_customer_name(customerId)
masseuseManager.get_masseuse_name(masseuseId)


