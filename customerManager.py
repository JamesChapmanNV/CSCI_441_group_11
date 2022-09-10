import mysqlManager


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

def get_customer_name(customerId): 
    try:
        data = (str(customerId), )
        command = ("Select name from customers "
                "where customerId = %s ")
        mysqlManager.cursor.execute(command, data)
    except:
        print('error in get_customer Select')
    
    name = mysqlManager.cursor
    return name