from musha.api import API
from musha.middleware import Middleware


app = API()

def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)

app.add_exception_handler(custom_exception_handler)


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"

@app.route("/contact")
def contact(request, response):
    response.text = "Welcome to CONTACT US page"
    
@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}!"

@app.route("/tell/{name}/{age:d}")
def tellage(request, response, name, age):
    response.text = f"Hello, {name}! Your age is {age}."

@app.route("/sum/{num_1:d}/{num_2:d}")
def sum(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"{num_1} + {num_2} = {total}"

@app.route("/books")
class BooksView:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"


# Testing Django based routes
def handler(req, resp):
    resp.text = "sample"

app.add_route("/sample", handler)


# Testing template route
@app.route("/template")
def template_handler(req, resp):
    resp.html = app.template("index.html", context={"name": "musha", "title": "Best Framework"})


@app.route("/json")
def json_handler(req, resp):
    resp.json = {"name": "data", "type": "JSON"}


@app.route("/text")
def text_handler(req, resp):
    resp.text = "This is a simple text"


# Exception handler
@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used.")


# Custom middleware
class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)

app.add_middleware(SimpleCustomMiddleware)