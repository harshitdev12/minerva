from flask import Flask,render_template,request
from datetime import datetime
import requests

BACKEND_URL =  'http://10.34.101.183:2000'

app = Flask(__name__)

@app.route('/')

def home():
    day_of_week = datetime.today().strftime('%A %Y-%m-%D')
    current_time = datetime.now().strftime('%H-%M-%S')
  
    return render_template('index.html', day_of_week=day_of_week,  current_time= current_time)

@app.route('/submit', methods=['POST'])
def submit():


   form_data = dict(request.form)

   requests.post(BACKEND_URL + '/submit',json=form_data)
   return 'data submitted succesfully!'

def get_data():
    response = request.get(BACKEND_URL + '/view')
    return response.json()
   
if __name__=='__main__':

    app.run(debug=True, port=3000,host='0.0.0.0')
