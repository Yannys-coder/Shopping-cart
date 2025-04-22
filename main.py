from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route("/details", methods=['POST', 'GET'])
def details():
    username = request.form['input']
    phone_number = request.form['phone']
    number_of_items= request.form['Total items']
    total_amount = request.form['Total amt.']
    current_date = request.form['date']
 

    mydb= mysql.connector.connect(
        host="remotemysql.com",
        user="uL7j9FaRVB",
        password="qQvo5rGf3i",
        database="uL7j9FaRVB")

    mycursor = mydb.cursor()
    mycursor= mydb.cursor()
    mycursor.execute('CREATE TABLE Customer_Details(Customer_name varchar(255), Phone_number varchar(10), Number_of_items int(11), Total_Amount int(11), date_of_purchase)'
    )

    mycursor.execute(
        'insert into Customer_details VALUES(%s,%s,%s,%s,%s,)'
        (username, phone_number, number_of_items, total_amount, current_date)
        )
    mydb.commit()
    return render_template('page.html')
@app.route("/winner", methods=['POST', 'GET'])
def winner():
    mydb = mysql.connector.connect(
         host="remotemysql.com",
        user="uL7j9FaRVB",
        password="qQvo5rGf3i",
        database="uL7j9FaRVB")
    mycursor = mydb.cursor()
    mycursor.execute(
        'SELECT * FROM Customer_Details WHERE date_of_purchase = current_date order by Total_Amount DESC'
    )
    account = mycursor.fetchone()
    print(account)
    if account:
        user_name = account[0]
        phone_number = account[1]
        return render_template('page.html', user_name = user_name, phone_number = phone_number)
    else:
        return render_template('page.html')
    
@app.route('/')
def index():
    return render_template('index.html')
app.run()


    