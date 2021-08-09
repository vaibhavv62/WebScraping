import ScrapData as sd
import sqlite3
con = sqlite3.connect('flipkart_laptops.db')
cur = con.cursor()

create_table_query = "CREATE TABLE laptops (\
	name TEXT NOT NULL,\
	price TEXT NOT NULL,\
	rating TEXT NOT NULL,\
	discount TEXT NOT NULL,\
	processor TEXT NOT NULL,\
    ram TEXT NOT NULL,\
    os TEXT NOT NULL,\
    rom TEXT NOT NULL,\
    screen TEXT NOT NULL,\
    extras TEXT NOT NULL,\
    warranty TEXT\
        );"

# cur.execute(create_table_query) #UnComment & Execute Once to Create Table
# print('Table Created')

parsed_data = sd.scrap_data()
no_of_records = len(parsed_data[0])
counter = 0
for laptop in range(no_of_records):
    name = parsed_data[0][counter]
    price = parsed_data[1][counter]
    rating = parsed_data[2][counter]
    discount = parsed_data[3][counter]
    processor = parsed_data[4][counter]['processor']
    ram = parsed_data[4][counter]['ram']
    os = parsed_data[4][counter]['os']
    rom = parsed_data[4][counter]['rom']
    screen = parsed_data[4][counter]['screen']
    extras = parsed_data[4][counter]['extras']
    warranty = parsed_data[4][counter]['warranty']
    # print(name,price,rating,discount,processor,ram,os,rom,screen,extras,warranty)
    insert_query = f"INSERT INTO laptops VALUES\
            ('{name}','{price}','{rating}','{discount}','{processor}','{ram}','{os}','{rom}','{screen}','{extras}','{warranty}');"
    cur.execute(insert_query)
    con.commit()
    print('Record Inserted')

con.close()
