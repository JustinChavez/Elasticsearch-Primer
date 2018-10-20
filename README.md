# Elasticsearch Installation

1. Download Elasticsearch https://www.elastic.co/downloads/elasticsearch
2. Unzip anywhere
3. Open Terminal or the command line and navigate to the new file
4. Enter `./bin/elasticsearch` if you are on Linux or Mac, or enter `bin/elasticsearch.bat` if you are on Windows
5. Go to any internet browser and enter the address `http://localhost:9200/`
6. You should now see the details of your new cluster and can proceed to linking python

# Python and Jupyter notebook installation

1. Download Python 3 https://www.python.org/downloads/
2. Once downloaded, open your terminal or command line and enter the following to install pip and virtualenv
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install virtualenv 
```
3. Download this repository to your computer and navigate to its location using terminal or the command line
4. Run the following to open a new environment with all the dependencies installed
