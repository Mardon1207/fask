from flask import Flask
api=Flask(__name__)
@api.route("/")
def hello():
    return "Hello World"
@api.route("/home")
def home():
    return "Welcome to home"
@api.route("/about")
def about():
    return "Welcome to about"
@api.route("/contact")
def contact():
    return "Welcome to contact"
@api.route("/products")
def products():
    return "Welcome to products"
if __name__=="__main__":
    api.run()