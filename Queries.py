import sqlite3
connec = sqlite3.connect("trainsdb.db")
cursor = connec.cursor()

def findTrainsPassenger(fname, lname):
    query = """
        SELECT Train.Train_Number, Train.Train_Name, train.source, train.destination, Booked.Ticket_Type, Booked.Status
        FROM Train
        JOIN Booked ON Train.Train_Number = Booked.Train_Number
        JOIN Passenger ON Booked.Passanger_ssn = Passenger.SSN
        WHERE Passenger.first_name = ? AND Passenger.last_name = ?
        AND Booked.Status = 'Booked';
    """
    cursor.execute(query, (fname, lname))
    results = cursor.fetchall()
    return results        
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# findTrainsPassenger(fname, lname)



def passengers_from_date(tdate):
    query = """
        SELECT Passenger.first_name, Passenger.last_name
        FROM Passenger
        JOIN Booked ON Passenger.SSN = Booked.Passanger_ssn
        JOIN train ON Booked.Train_Number = train.Train_Number
        join status on status.train_name = train.Train_name
        WHERE Status.Date = ? AND Booked.Status = 'Booked';
    """
    cursor.execute(query, (tdate,))
    results = cursor.fetchall()

    for row in results:
        print(row)
    
# date = input("Enter date: (DD-MM-YYYY): ")
# passengers_from_date(date)



def passengers_age(start_age, end_age):
    query = """
        SELECT train.train_number, train.train_name, train.source, train.destination, passenger.first_name, passenger.last_name, passenger.address, booked.ticket_type, booked.status
        FROM Passenger
        JOIN Booked ON Booked.passanger_ssn = Passenger.ssn
        Join train ON Booked.train_number = train.train_number
        WHERE strftime('%Y', 'now') - strftime('%Y', dob) BETWEEN ? AND ?;
    """
    cursor.execute(query, (start_age,end_age))
    
    results = cursor.fetchall()

    for row in results:
        print(row)

# sage  = input("Start age: ")
# eage = input("End age: ")
# passengers_age(int(sage), int(eage))



# def count_passengers():
#     query = """
#     """
#     cursor.execute(query)
#     results = cursor.fetchall()

#     for row in results:
#         print(row)

    
    
def passengers_from_train(tname):
    query = """
    Select passenger.first_name, passenger.last_name
    from passenger
    join Booked on Passenger.ssn = Booked.passanger_ssn
    JOIN train on Booked.train_number = train.train_number
    where Booked.status = 'Booked' and train.train_name = ?;
    """
    cursor.execute(query, (tname,))
    results = cursor.fetchall()

    for row in results:
        print(row)
        
# tname = input("Train name: ")
# passengers_from_train(tname)

def delete_record(passenger_ssn, train_number, ttype, status):
    query = """
        delete from Booked
        where Booked.passanger_ssn = ? and Booked.train_number = ? and Booked.status = ?
    """
    
    cursor.execute(query, (passenger_ssn, train_number, status))
    if (status == 'Booked'):
        query = """
        Select passanger_ssn 
        from Booked
        where Booked.train_number = ? and Booked.status = 'WaitL' and Booked.ticket_type = ?
        """
        
        cursor.execute(query,(train_number, ttype))
        res = cursor.fetchone()[0]
        
        query = """
        Update Booked
        set status = 'Booked'
        where Booked.train_number = ? and Booked.passanger_ssn = ?
        """
        
        cursor.execute(query,(train_number, res))
        connec.commit()
        
# ssn = input("input ssn: ")
# tnum = input("input ssn: ")
# ttype = input("input ssn: ")
# status = input("input ssn: ")

# delete_record(ssn, tnum, ttype, status)
    