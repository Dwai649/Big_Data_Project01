import happybase

connection = happybase.Connection('localhost')


def open_connection():
    connection.open()

def close_connection():
    connection.close()


def get_table(name):
    open_connection()
    table = connection.table(name)
    close_connection()
    return table

def batch_insert_data(filename, tablename):
    print("starting batch insert of "+filename)
    file = open(filename, 'r')
    table = get_table(tablename)
    open_connection()
    i = 0
    with table.batch(batch_size=50000) as a:
        for line in file:
            if i!=0 or i!=1:
                w = line.strip().split(",")
                a.put(w[1]+w[2] ,{'cf1:VendorID': str(w[0]), 'cf1:tpep_pickup_datetime': str(w[1]), 'cf1:tpep_dropoff_datetime': str(w[2]), 
                                                                       'cf1:passenger_count': str(w[3]), 'cf1:trip_distance': str(w[4]), 'cf1:RatecodeID': str(w[5]), 'cf1:store_and_fwd_flag': str(w[6]), 'cf1:PULocationID': str(w[7]), 'cf1:DOLocationID': str(w[8]), 
                                                                        'cf1:payment_type': str(w[9]),'cf1:fare_amount': str(w[10]), 'cf1:extra': str(w[11]), 'cf1:mta_tax': str(w[12]), 'cf1:tip_amount': str(w[13]), 'cf1:tolls_amount': str(w[14]), 'cf1:improvement_surcharge': str(w[15]), 'cf1:total_amount': str(w[16]) })
            
            i+=1

    file.close()
    print("batch insert done")
    close_connection()    
