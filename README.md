# api-flask

This is a file I used to learn Flask API. I make a list of random quotes to return.

Run this in a Python IDE such as PyCharm In terminal type this to install flask-restful: pip install flask-restful


******************Get random quote******************

1) http://localhost:5000/
2) http://localhost:5000/random-quotes/
3) http://localhost:5000/random-quotes

******************Get specific quote******************
1) localhost:5000/random-quotes/<int:id>
Replace <int:id> with integer 1 to 3 to return quotes 1, 2, or 3
