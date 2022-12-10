from src import mysqlManager


def insert_customer(customerId,name,address,email,phone): 
    try:
        data = (str(customerId),name,address,email,str(phone))
        insertCommand = ("INSERT IGNORE INTO customers(customerId,name,address,email,phone) "
                        "VALUES (%s, %s, %s, %s, %s)")
        
        mysqlManager.cursor.execute(insertCommand, data)
        mysqlManager.connection.commit()  
    except:
        print('error in insert_customer')

def delete_customer(customerId): 
    try:
        command = ("DELETE FROM customers where customerId = %s" % customerId)            
        mysqlManager.cursor.execute(command)
        mysqlManager.connection.commit()  
    except:
        print('error in delete_customer')
        
def get_customer_ID(name):
    try:
        data = (str(name),)
        command = ("Select customerId from customers "
                   "where name = %s ")
        mysqlManager.cursor.execute(command, data)

        cid = mysqlManager.cursor.fetchone()

    except:
        print('error in get_customer_ID ')

    if (cid[0]):
        return cid[0]
    return ''


def get_customer_name(customerId): 
    try:
        data = (str(customerId), )
        command = ("Select name from customers "
                "where customerId = %s ")
        mysqlManager.cursor.execute(command, data)
    except:
        print('error in get_customer Select')
    
    name = mysqlManager.cursor.fetchone()
    #returns an tuple ('name',)
    #Access name string at index 0
    return name[0]


def get_all_customer_names():
    try:
        command = ("SELECT distinct name FROM customers")
        mysqlManager.cursor.execute(command)
    except:
        print('error in get_all_customer_names ')

    names = []  # = mysqlManager.cursor.fetchall()
    for customers in mysqlManager.cursor:
        names.append(customers[0])

    return names

def get_customers():
    try:
        command = ("Select customerId, name, address, email, phone "
                   "from customers ")
        mysqlManager.cursor.execute(command)

    except:
        print('error in get_customers Select')

    customers = []
    try:
        for customerId, name, address, email, phone in mysqlManager.cursor:
            # Creates an array within appointments array
            # one for each appointment/timeslot
            customers.append([customerId, name, address, email, phone])
    except:
        print('error in get_customers append')

    return customers
