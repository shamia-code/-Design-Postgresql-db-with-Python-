# In psycopg , the connection( ) class is responsble for handling transactions and it initiates a transaction every time a SQL statement  is issued to the PostgreSQL database
#The connection class has two methods for terminating a transaction ie
#commit() for mitting changes   and rollback() for canceling the changes 

#below function shows how to add anew part and assign  the vendors who supply that part at the same time 
#First we insert a new row in the part table and get the part_id
#Then we insert a new row into the vendor_parts table


import psycopg2
#from config import config

def add_part(part_name, vendor_list):
    #statement for inserting a new row into the parts table 
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"
    #statement for inserting a new row into the vendor_parts table 

    assign_vendor = "INSERT INTO vendor_parts(vendor_id,part_id) VALUES (%s,%s)"

    conn=None
    try:
        #params=config ()
        #params="dbname=suppliers user=postgres password=shamia"
        conn= psycopg2.connect("dbname=suppliers user=postgres password=shamia")
        cur=conn.cursor()
        #insert a new part 
        cur.execute(insert_part, (part_name,))
        #get the part id
        part_id=cur.fetchone()[0]
        #assign parts provided by vendors
        for vendor_id in vendor_list:
            cur.execute(assign_vendor,(vendor_id, part_id))
        #commit changes 
        conn.commit()
    except ( Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    add_part('SIM TRAY',(1,2))
    add_part('Speaker',(3,4))
    add_part('AMplifier',(5,6))
