import mysql.connector

def koneksi():
    db = mysql.connector.connect(
    host = "remotemysql.com",
    user = "e4YsvvDdqe",
    passwd = "6nH3Dk1LiE",
    database = "e4YsvvDdqe"
    )

    datamysql = db.cursor()

    return datamysql, db