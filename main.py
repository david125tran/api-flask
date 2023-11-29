# In terminal type this to install flask-restful:   pip install flask-restful

#--------------------------- Imports ---------------------------#
from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

#--------------------------- HTTP Status Codes ---------------------------#
# 200: Request is successful
# 201: Request created successfully
# 400: Request cannot be processed
# 404: The record was not found

#--------------------------- Quotes ---------------------------#
random_quotes = [
    {
        # Quote id start at 1 and not 0.  id of 0 is reserved for returning a random quote.

        "id": 1,
        "author": "Seneca",
        "quote": "He who boasts of his ancestry is praising the deeds of another."
    },
    {
        "id": 2,
        "author": "Charles M. Schulz",
        "quote": "That's the secret to life... replace one worry with another..."
    },
    {
        "id": 3,
        "author": "Francois de La Rochefoucauld",
        "quote": "The pleasure of love is in loving."
    }
]

class Quote(Resource):
    #--------------------------- GET ---------------------------#
    def get(self, id=0):
        if id == 0:   # If an id was not specified, the GET method returns a random quote
            return random.choice(random_quotes), 200
        else:   # If an id was specified, the GET method returns a specific quote
            for quote in random_quotes:
                if quote["id"] == id:
                    return quote, 200
        return "Quote not found", 404   # If an id was specified and not found, the GET method returns a 400 error code

    #--------------------------- POST ---------------------------#

    def post(self, id):   # POST adds to a resource
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
    
        for quote in random_quotes: # If an id was specified and the id already exists, the POST method returns a 400 error code
            if id == quote["id"]:
                return f"Quote with id {id} already exists", 400
    
        quote = {
            "id": int(id),
            "author": params["author"],
            "quote": params["quote"]
        }
    
        random_quotes.append(quote) # If an id was specified and the id doesn't exist yet, the POST method creates the request successfully
        return quote, 201

    #--------------------------- PUT ---------------------------#
    def put(self, id):   # PUT replaces a resource or adds to a resource
        parser = reqparse.RequestParser
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
    
        for quote in random_quotes:   # If the id already exists, the quote is replaced
            if id == quote["id"]:
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200
    
        quote = {   # If the id does not exist yet, the quote is added
            "id": id,
            "author": params["author"],
            "quote": params["quote"]
        }
    
        random_quotes.append(quote)
        return quote, 201

    #--------------------------- DELETE ---------------------------#
    def delete(self, id):
        global random_quotes
        random_quotes = [quote for quote in random_quotes if quote["id"] != id]
        return f"Quote with id {id} is deleted.", 200



app = Flask(__name__)
api = Api(app)

#--------------------------- Add the resource to our API ---------------------------#
api.add_resource(Quote, "/", "/<int:id>", "/random-quotes", "/random-quotes/", "/random-quotes/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)

#--------------------------- Example of getting a quote with id of 3 ---------------------------#
#--------------------------- Run this code below in a different Python IDE window ---------------------------#
# import requests
# quote_id = 3 # You can change this id to whatever quote id you want
# url = f"http://localhost:5000/random-quotes/{quote_id}"
# response = requests.get(url=url)
# response.raise_for_status()
# data = response.json()
# print(data)
# print(url)
