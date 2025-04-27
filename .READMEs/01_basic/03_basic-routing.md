# Setting up new tina4_python project

## Basic Routing and Endpoints

### Guide for setting up basic routing and endpoints

> [Official Tina4 routing guide](https://www.tina4.com/getting-started/python/-Basics/b-first-api-routes.html)

- in `src/routs`, create a new file called `main.py` and another called `api.py`
- explanations:
  - `main.py` is for all main endpoints, such as those that are used to access your website
    - example: 
      - website url: `https://www.my-website.com`
      - route string: `/hello/world`
      - end result: `https://www.my-website.com/hello/world`
  - `api.py` is for all the endpoints that are mostly used within the website itself
    - this can be api calls/requests between front- and back-end logic
    - usually prefaced with `/api` before the rest, for example:
      - `https://www.my-website.com/api/hello/world`
- in `main.py`, put the following code:

```python
from tina4_python.Router import get, post

@get("/hello/world")
async def get_hello_world(request, response):
    return response("Hello World!")

@post("/hello/world")
async def post_hello_world(request, response):
    return response("Hello World!")
```

- you will notice if you go to `http://127.0.0.1:7145/hello/world`, it will show a 404 error page
- all files that contain routes, such as `main.py` and `api.py`, must be registered to work
- in the `src` directory, open the file called `__init__.py`
- this file is used for initializing
- paste the following code:

```python
from .routes import main
from .routes import api
```

- this will import and activate all routes in the files
  - test this by stopping and restarting the server, then going to `http://127.0.0.1:7145/hello/world`

### Response Object

- notice the code for the endpoints from earlier return `response(something_here)`
- this is to make sure that the values are returned in a routing friendly manner, easily readable by other code.
- to return any value, including dictionaries and lists, you can simply put it in the `()` 
  - examples:

```python
@get("/dictionary-response")
async def get_dictionary(request, response):
  return response({"msg": "this is a dictionary!", "code": 200, "error": "none"})

@get("/list-response")
async def get_list(request, response):
  return response(["this", "is", "a", "list", "of", "words"])

@get("/combo-response")
async def get_combo(request, response):
  word_list = ["this", "is", "a", "list", "of", "words"]
  return response({"msg": "this is a dictionary, with a list inside!", "code": 200, "word_list": word_list})
```

### Redirecting

- to redirect, simply user `response.redirect(new_url)`
- example:

```python
@post("/login")
async def get_login_page(request, response):
    # check the database for a user and password
    if Users.validate_login(request):
        return response.redirect("/dashboard")
    else:
        return response.redirect("/login")
```

### Security

- any route can be secured, simply by placing `@secure` below the route declaration
- example:

```python
from tina4_python.Swagger import secure

@post("/hello/world")
@secure()
async def post_hello_world(request, response):
  return response("Hello World! Secure post route")
```

- make one of your routes secure and see the `403` error

