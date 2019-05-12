from flask import Flask, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()

# mysql configuration
app.config['MYSQL_DATABASE_USER'] = 'e4YsvvDdqe'
app.config['MYSQL_DATABASE_PASSWORD'] = '6nH3Dk1LiE'
app.config['MYSQL_DATABASE_DB'] = 'e4YsvvDdqe'
app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'

mysql.init_app(app)

@app.route('/coba')
def coba():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()

    return render_template('coba.html', result=result)
    # dataList = []
    # if data is not None:
    #     for item in data:
    #         dataTempObj = {
    #             'customer_id'   : item[0],
    #             'name'          : item[1],
    #             'address'       : item[2]
    #         }
    #         dataList.append(dataTempObj)
    #     return dataList
    # else:
    #     return 'data kosong'

    # return render_template('coba.html')

if __name__ == '__main__':
    app.run()