from flask import Flask, request,render_template
import requests
import time
from datetime import datetime,timedelta
import random
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime,timedelta
import pytz


# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Add your credentials JSON file obtained from Google Developer Console
creds = ServiceAccountCredentials.from_json_keyfile_name('autofetch-1611435677959-a975f9d40d2c.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet by ID
sheet = client.open_by_key('1IB5hgHo5IrARwCMGM9d-fQN5trXE0OSiGa-g-bVq-Rw')

# Select the first worksheet
worksheet = sheet.get_worksheet(0)
print(worksheet)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new_index.html')

@app.route('/cilantro_promo', methods=['POST'])
def process_number():
    multiplied_number = int(request.form['age'])*60
    mother_name = request.form['name'].strip().replace(" ", "").lower()
    phone = request.form['phone']
    # Append the row
    row = [phone, mother_name ,"",datetime.now(pytz.utc).astimezone(pytz.timezone('Etc/GMT-2')).strftime("%Y-%m-%d %H:%M"),int(request.form['age'])]
    print(row)
    worksheet.append_row(row)
    return render_template('new_result.html', multiplied_number=multiplied_number,mother_name = mother_name.capitalize())
if __name__ == '__main__':
    app.run(debug=True)

