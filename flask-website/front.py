from flask import Flask, render_template, request
from elasticsearch import helpers, Elasticsearch

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html', result = "")

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':

		#connect to ES
		es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

		#Grab text that was submitted in the website
		search = request.form["thing"]

		#Run any Elasticsearch query, here we use the profiles index
		#we created in the jupyter notebook profile_example.ipynb
		matches = es.search(index='profiles', \
			body={"size":10,"query":{"match":{"essay0":search}}})

		#Filter the result into the values you want to display
		best_match = matches['hits']['hits'][0]["_source"]

		result = "you are compatible with a " + best_match["age"] \
		+ " year old " + best_match["job"] + " from "\
		+ best_match["location"]

	#Return the filtered result for the website to display
  	return render_template('index.html', result= result)

if __name__ == '__main__':
   app.run(debug = True, port=5000)