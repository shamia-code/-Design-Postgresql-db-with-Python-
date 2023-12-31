import psycopg2 
from config import config 

def update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id """
    sql ="""UPDATE vendors
            SET vendor_name= %s 
            WHERE vendor_id = %s"""
    
    conn= None
    updated_rows=0

    try:
        #read the database configuration
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute(sql, (vendor_name, vendor_id))
        #Get the number of the updated rows 
        updated_rows = cur.rowcount
        conn.commit()
        #close communication with the PostgreSQL database 
        cur.close()

    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
    return updated_rows

if __name__ =="__main__":
    #Update vendor id 1
    update_vendor(1,"3M Corp")

