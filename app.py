from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='D:\\GITHUB PROJECTS\\Railway-Registration\\templates')

# Create user table if not exists
def create_table():
    conn = sqlite3.connect('railway_registration.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name varchar(25) NOT NULL,
                        middle_name varchar(25),
                        last_name varchar(25) NOT NULL,
                        gender TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        mobile INTEGER NOT NULL,
                        city varchar(25) NOT NULL,
                        state varchar(25) NOT NULL,
                        pincode INTEGER NOT NULL,
                        train_name varchar(25) DEFAULT 'nan',
                        train_no INTEGER DEFAULT 0,
                        arrival_time TIME DEFAULT '00:00:00',
                        destination varchar(25) DEFAULT 'nan')''')
    conn.commit()
    conn.close()

# Home Page - Options to Book/View/Cancel
@app.route('/')
def index():
    return render_template('index.html')

# Train Booking Page - Choose a Train
@app.route('/book')
def book_ticket():
    return render_template('train_select.html')

# Handle train selection and go to user form
@app.route('/confirm_booking', methods=['POST'])
def confirm_booking():
    train_no = request.form['train_no']
    train_name = request.form['train_name']
    arrival_time = request.form['arrival_time']
    destination = request.form.get('destination', 'Unknown')
    return render_template('user.html', train_no=train_no, train_name=train_name, arrival_time=arrival_time, destination=destination)

# Insert User Form Data
@app.route('/insert', methods=['POST'])
def insert_data():
    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    age = request.form['age']
    mobile = request.form['mobile']
    city = request.form['city']
    state = request.form['state']
    pincode = request.form['pincode']
    train_name = request.form['train_name']
    train_no = request.form['train_no']
    arrival_time = request.form['arrival_time']
    destination = request.form['destination']

    conn = sqlite3.connect('railway_registration.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO user (first_name, middle_name, last_name, gender, age, mobile, city, state, pincode, train_name, train_no, arrival_time, destination)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (first_name, middle_name, last_name, gender, age, mobile, city, state, pincode, train_name, train_no, arrival_time, destination))
    conn.commit()
    conn.close()

    return render_template('confirmation.html',
                       first_name=first_name,
                       middle_name=middle_name,
                       last_name=last_name,
                       gender=gender,
                       age=age,
                       mobile=mobile,
                       city=city,
                       state=state,
                       pincode=pincode,
                       train_name=train_name,
                       train_no=train_no,
                       arrival_time=arrival_time,
                       destination=destination)


# View Booked Tickets
@app.route('/view')
def view_data():
    conn = sqlite3.connect('railway_registration.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    conn.close()
    return render_template('view.html', users=users)

# Cancel Ticket by ID
@app.route('/cancel')
def cancel_ticket():
    return render_template('delete.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    user_id = request.form['id']
    conn = sqlite3.connect('railway_registration.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    
    # Pass confirmation message to the template
    return render_template('deleteConfirmation.html', user_id=user_id)


@app.route('/find_trains', methods=['POST'])
def find_trains():
    source = request.form['source']
    destination = request.form['destination']
    travel_date = request.form['travel_date']

    # Dummy train list for now, replace with actual DB/API query
    available_trains = [
        {'train_no': '12345', 'train_name': 'Express One', 'arrival_time': '09:00', 'destination': destination},
        {'train_no': '67890', 'train_name': 'Express Two', 'arrival_time': '14:30', 'destination': destination}
    ]

    return render_template('select_train.html', trains=available_trains, travel_date=travel_date, source=source)


if __name__ == '__main__':
    create_table()
    app.run(debug=True)
