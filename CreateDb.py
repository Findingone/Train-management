import sqlite3


data = {
    "train_data": [
        (1, "Orient Express" ,800,600, "Paris", "Istanbul"),
        (2, "Flying Scottsman",4000,3500, "Edinburgh", "London"),
        (3, "Golden Arrow",980,860, "Victoria", "Dover"),
        (4, "Golden Chariot",4300,3800, "Bangalore", "Goa"),
        (5, "Maharaja Express",5980,4510, "Delhi", "Mumbai")
    ],
    "booked_data": [
        (264816896,3,"Premium","Booked"),
        (240471168,2,"General","Booked"),
        (285200976,4,"Premium","Booked"),
        (285200976,2,"Premium","Booked"),
        (317434088,2,"Premium","Booked"),
        (310908858,2,"General","Booked"),
        (322273872,2,"General","Booked"),
        (256558303,3,"Premium","WaitL"),
        (302548590,2,"General","WaitL"),
        (284965676,3,"Premium","WaitL"),
        (277292710,3,"General","WaitL"),
        (331160133,3,"General","WaitL"),
        (331293204,3,"General","WaitL"),
        (290123298,3,"General","WaitL"),
        (286411536,4,"Premium","Booked"),
        (294860856,4,"Premium","Booked"),
        (317434088,4,"Premium","Booked"),
        (310908858,4,"Premium","Booked"),
        (322273872,4,"Premium","Booked"),
        (256558303,4,"Premium","Booked"),
        (302548590,4,"Premium","Booked"),
        (284965676,4,"General","Booked"),
        (277292710,4,"General","Booked"),
        (331160133,4,"General","Booked"),
        (331293204,4,"General","Booked")
    ],
    "train_status": [
        ("2022-02-19", "Orient Express",10,10,0,0),
        ("2022-02-20", "Flying Scottsman",8,5,2,5),
        ("2022-02-21", "Maharaja Express",7,6,3,4),
        ("2022-02-21", "Golden Chariot",6,3,4,7),
        ("2022-02-22","Golden Arrow",8,7,2,3),
        ("2022-03-10","Golden Arrow",8,5,2,5),
        ("2022-02-21", "Maharaja Express",7,6,3,4),
        ("2022-02-21", "Flying Scottsman",5,5,5,5)
    ],
    "passenger_list": [
        ("James","Butt","6649 N Blue Gum St,New Orleans,Orleans","504-845-1427",264816896, "1968-10-10"),
        ("Josephine","Darakjy","4 B Blue Ridge Blvd,Brighton,Livingston","810-374-9840",240471168, "1975-11-01"),
        ("Art","Venere","8 W Cerritos Ave #54	Bridgeport	Gloucester","856-264-4130",	285200976,	"1982-11-13"),
        ("Lenna","Paprocki","639 Main St	Anchorage	Anchorage",907-921-2010,	309323096,	"1978-09-08"),
        ("Donette","Foller","34 Center St	Hamilton	Butler",513-549-4561,	272610795,	"1990-11-06"),
        ("Simona","Morasca","3 Mcauley Dr	Ashland	Ashland",419-800-6759,	250951162,	"1994-08-15"),
        ("Mitsue","Tollner","7 Eads St	Chicago	Cook",773-924-8565,	272913578,	"1984-04-07"),
        ("Leota","Dilliard","7 W Jackson Blvd	San Jose	Santa Clara",408-813-1105,	268682534,	"1991-09-05"),
        ("Sage","Wieser","5 Boston Ave #88	Sioux Falls	Minnehaha",605-794-4895,	310908858,	"1982-02-25"),
        ("Kris","Marrier","228 Runamuck Pl #2808	Baltimore	Baltimore City",410-804-4694,	322273872,	"1956-04-04"),
        ("Minna","Amigon","2371 Jerrold Ave	Kulpsville	Montgomery",215-422-8694,	256558303,	"1995-09-09"),
        ("Abel","Maclead","37275 St  Rt 17m M	Middle Island	Suffolk",631-677-3675,	302548590,	"1960-05-11"),
        ("Kiley","Caldarera","25 E 75th St #69	Los Angeles	Los Angeles",310-254-3084,	284965676,	"1981-09-05"),
        ("Graciela","Ruta","98 Connecticut Ave Nw	Chagrin Falls	Geauga",440-579-7763,	277292710,	"1982-02-25"),
        ("Cammy","Albares","56 E Morehead St	Laredo	Webb",	956-841-7216,331160133,	"1956-04-04"),
        ("Mattie","Poquette","73 State Road 434 E	Phoenix	Maricopa",602-953-6360,	331293204,	"1995-09-09"),
        ("Meaghan","Garufi","69734 E Carrillo St	Mc Minnville	Warren",931-235-7959,	290123298,	"1960-02-11"),
        ("Gladys","Rim","322 New Horizon Blvd	Milwaukee	Milwaukee",414-377-2880,	286411536,	"1991-09-05"),
        ("Yuki","Whobrey","1 State Route 27	Taylor	Wayne",313-341-4470	,294860856,	"1985-02-25"),
        ("Fletcher","Flosi","394 Manchester Blvd	Rockford	Winnebago",815-426-5657	,317434088,	"1961-04-04")
    ]
}


def createDb():
    connec = sqlite3.connect("trainsdb.db")
    cursor = connec.cursor()
    cursor.execute("CREATE TABLE train(train_number, train_name, premium_fate, general_fare, source, destination)")
    cursor.execute("Create table booked(Passanger_ssn,train_number,ticket_type, Status)")
    cursor.execute("Create table status(date,train_name,'Premium_seats_ava', 'general_seats_ava', 'premium_seats_booked','general_seats_booked')")
    cursor.execute("Create table passenger(first_name,last_name,address,phone, ssn, dob)")
    
    sql_insert_trains = "INSERT INTO train (train_number, train_name, premium_fate, general_fare, source, destination) VALUES (?, ?, ?, ?, ?,?)"
    sql_insert_bookings = "INSERT INTO booked (Passanger_ssn,Train_Number,Ticket_Type,Status) values (?,?,?,?)"
    sql_insert_status = "insert into status(date,train_name,'Premium_seats_ava', 'general_seats_ava', 'premium_seats_booked','general_seats_booked') values (?,?,?,?,?,?)"
    sql_insert_passenger = "insert into passenger(first_name,last_name,address,phone, ssn, dob) values (?,?,?,?,?,?)"
    for train in data["train_data"]:
        cursor.execute(sql_insert_trains, train)
    for booking in data["booked_data"]:
        cursor.execute(sql_insert_bookings, booking)
    for status in data["train_status"]:
        cursor.execute(sql_insert_status, status)
    for passenger in data["passenger_list"]:
        cursor.execute(sql_insert_passenger, passenger)
        
    connec.commit()
    connec.close()

