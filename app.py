from flask import Flask, render_template, redirect
import pymongo
import mission_to_mars
from mission_to_mars import scrape



app = Flask(__name__)


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.MarsDB
collection = db.mars

@app.route('/')
def home():
	data = collection.find_one()
	return render_template('index.html', data=data)



@app.route('/scrape')
def scrape():
	data = scrape()
	collection.drop()
	collection.insert.one(data)
	return redirect('/', code=302)

	


if __name__ == "__main__":
	app.run(debug=True)
