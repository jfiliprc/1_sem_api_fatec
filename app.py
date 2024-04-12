from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    soil_humidity = db.Column(db.Float, nullable=False)
    ambient_humidity = db.Column(db.Float, nullable=False)
    ambient_temperature = db.Column(db.Float, nullable=False)
    water_volume = db.Column(db.Float, nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/show-data")
def show_data():
    return render_template('show_data.html')

@app.route("/add-data")
def add_data():
    return render_template('add_data.html')

@app.route("/delete-data")
def delete_data():
    return render_template('delete_data.html')

@app.route("/statistics")
def statistics():
    return render_template('statistics.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
