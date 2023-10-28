import psycopg2

#Calling the connect() function and specifying the PostgreSQL database parameter.
conn=psycopg2.connect("dbname=suppliers user=postgres password=shamia")


# OR you can do this 
conn=psycopg2.connect(
    host="localhost",                   #This is the database server address

    database="suppliers",               
    user="postgres",                    #The username used to authenticate
    password="shamia"
)

# To make more convenient, you can use a configuration file to store all connection paramateters
#by using the database.ini file 

#With the database.ini, you can change the POSTGRESQL connection parameters when you move the code to he production environment without modifying the code .

#The config() funtion reads the database.ini file and returns connection parameters 
