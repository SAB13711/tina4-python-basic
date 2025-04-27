# Setting up new tina4_python project

## Basic Forms and Templates

### Guide for setting up basic forms and submitting them

> [Official Tina4 forms guide](https://www.tina4.com/getting-started/python/-Basics/b-posting-a-simple-form.html)   
> [Official Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)   

- forms are used to get user input and submit the data to the back-end
- create a new file, in `src/templates/forms`, called `login-form-page.twig`
- paste the below code:

```html
{% extends "base.twig" %}
{% set container_class ="main-content-container" %}
{% block content %}
  <div class="login-container">
      <h2>Login</h2>
      <form method="POST" action="/login-user">
          <div class="form-group">
              <label for="username">Username:</label>
              <input type="text" id="username" name="username" required autofocus>
          </div>
          <div class="form-group">
              <label for="password">Password:</label>
              <input type="password" id="password" name="password" required>
          </div>
          <div class="form-group">
              <button type="submit">Login</button>
          </div>
      </form>
  </div>
{% endblock %}
```

- the above code is a basic page, with a login form
- note the `<form>`:
  - contains the actual form fields and interactive elements
  - can set it's `method` to `POST`
  - can set it's `action` field to the endpoint it directs to

### Notes

- you can essentially just render this page wherever you need it
- alternatively you can extract the content and render it dynamically on other pages:
  - you can use api requests that send back rendered forms
  - you can use `{% include 'template.twig' %}` to directly use it in another template

### Setting up an endpoint to go to a page

- we can create a route/endpoint, called `user-login`, in our `main.py` file in `routes`:

```python
from tina4_python.Template import Template
from tina4_python.Router import get, post, put, delete

@get("/user-login")
async def get_user_login(request, response):
  return response(Template.render_twig_template("/forms/pages/login-form-page.twig"))
```

- in the above we are using tina4's ability to render twig/jinja templates
- you can also pass variables through to the template:

```python
user_data = {"name": "Luke Man", "age": 37, "date_joined": "2022-05-15" }
Template.render_twig_template("/user-details.twig", {"user_data": user_data})
```

- which you can then use in the template like this:

```html
<h1>Name: {{ user_data.name }}</h1>
<p>Age: {{ user_data.age }}</p>
<p>Member since: {{ user_data.date_joined }}</p>
```

### Security

- sometimes you need data to be secured and endpoints too
- form tokens are used to secure the endpoints in Tina4
- you can only access a secured endpoint if a form token was sent
- there are four ways you can get a formToken in Tina4:

1. Calling a JINJA filter "formToken"

> `RANDOM` is used to refresh the form token each time

```html
{% extends "base.twig" %}
{% set container_class ="main-content-container" %}
{% block content %}
  <div class="login-container">
      <h2>Login</h2>
      <form method="POST" action="/login-user">
          <div class="form-group">
              <label for="username">Username:</label>
              <input type="text" id="username" name="username" required autofocus>
          </div>
          <div class="form-group">
              <label for="password">Password:</label>
              <input type="password" id="password" name="password" required>
          </div>
          <div class="form-group">
              <button type="submit">Login</button>
          </div>
          {{  ("Login"~RANDOM()) | formToken }}
      </form>
  </div>
{% endblock %}
```

2. Calling a JINJA global "formToken()"

```html
{% extends "base.twig" %}
{% set container_class ="main-content-container" %}
{% block content %}
  <div class="login-container">
      <h2>Login</h2>
      <form method="POST" action="/login-user">
          <div class="form-group">
              <label for="username">Username:</label>
              <input type="text" id="username" name="username" required autofocus>
          </div>
          <div class="form-group">
              <label for="password">Password:</label>
              <input type="password" id="password" name="password" required>
          </div>
          <div class="form-group">
              <button type="submit">Login</button>
          </div>
          {%  set token = formToken({"page":"Login"}) %}
          <input type="hidden" name="formToken" value="{{ token }}">
      </form>
  </div>
{% endblock %}
```

3. Getting the FreshToken value from an already authenticated header.

4. Generating a form token in the back-end and passing it to the front-end:

```python
from tina4_python.Template import Template
from tina4_python.Router import get, post, put, delete

@get("/user-login")
async def get_user_login(request, response):
    form_token = Template.get_form_token()
    return response(Template.render_twig_template("/forms/pages/login-form-page.twig", {"form_token": form_token}))
```

### Best Practice:

- all the above is for when submitting forms directly, ie, have `method="POST" action="submit_url"`
- the better way to do this, is through manually submitting data with javascript
  - allows for validation checks before sending data
  - allows for better handling of redirects
- example of doing it with javascript and an api call:

```html
{% extends "base.twig" %}
{% set container_class ="main-content-container" %}
{% block content %}
<div class="login-container">
  <h2>Login</h2>
  <form id="login-form" method="POST" action="/" onsubmit="return false;">
    <div class="form-group">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required autofocus>
    </div>
    <div class="form-group">
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>
    </div>
    <div class="form-group">
      <button type="submit">Login</button>
    </div>
    {%  set formToken = formToken({"page":"Login"}) %}
  </form>
</div>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", function (event) {
      event.preventDefault(); // stop normal form submit

      let username = document.getElementById('username').value;
      let password = document.getElementById('password').value;
      if (username.trim() === "") {
        alert("Please enter a username.");
        return;
      }
      if (password.trim() === "") {
        alert("Please enter a password.");
        return;
      }
      // send login request
      sendRequest("/api/user-login?formToken={{ formToken }}&email=" + username + "&password=" + password, null, "POST", function (data) {
        console.log("inside callback for /api/user-login");
        // the call back is what happens when the response is returned
        if (data["success"]) {
          // login successful
        } else {
          // login unsuccessful
        }
      });
    });
  });
</script>
{% endblock %}
```

- there is now the ability to implement more checks and logic, both for when sending requests and when receiving returned data
- for the `sendRequest` function to be used, you need access to the tina4 helper file. Alter `base.twig` to look like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="/js/tina4helper.js"></script>
    <title>{{ title }}</title>
</head>
<body>
{% block content %}
{% endblock %}
</body>
</html>
```

- this allows for tina4 helper methods to be available to all pages inheriting from `base.twig` 

### Example of an api endpoint for the above:

```python
from tina4_python.Router import get, post, put, delete
from src.app import user_service

@post("/api/user-login")
async def post_user_login(request, response):
  data = request.params
  email = data.get("email")
  password = data.get("password")
  login_response = user_service.check_user_credentials(email, password)
  return response(login_response, login_response["code"])
```
