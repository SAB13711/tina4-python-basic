# Setting up new tina4_python project

## Landing Page and Base Template

### Guide for setting up main landing page and base template

> [Official Tina4 Twig/Jinja Guide](https://www.tina4.com/getting-started/python/-Basics/a-static-website-with-twig.html)  
> [Basic Twig for templates](https://twig.symfony.com/doc/3.x/templates.html)   
> [Basic Jinja for templates](https://jinja.palletsprojects.com/en/stable/templates/)   
> [Official Twig Documentation](https://twig.symfony.com/doc/)   
> [Official Jinja Documentation](https://jinja.palletsprojects.com/en/stable/)

- create a new file under `src/templates`, called `base.twig`, with the following contents:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{{ title }}</title>
    </head>
<body>
{% block content %}
{% endblock %}
</body>
</html>
```

- create a new file under `src/templates`, called `navigation.twig`, with the following contents:

```html
<nav>
    <a href="/">Home Page</a>
    <a href="/about-us">About Us</a>
</nav>
```

- create a new file under `src/templates`, called `index.twig`, with the following contents:

```html
{% set title="Home Page" %}
{%  extends "base.twig" %}
{% block content %}
<h1> {{ title }}</h1>
{%  include "navigation.twig" %}
<h2>Wonderful Content</h2>
<p>
    Here is some content about the page
</p>
{% endblock %}
```

- create a new file under `src/templates`, called `about-us.twig`, with the following contents:

```html
{% set title="About Us" %}
{%  extends "base.twig" %}
{% block content %}
<h1> {{ title }}</h1>
{%  include "navigation.twig" %}
<h2>Wonderful Content</h2>
<p>
    Here is some content about the page
</p>
{% endblock %}
```

- when you have these files created, refresh the webserver and you should see a landing page
- the base template is so you can import custom content that is then inherited by all templates extending `base.twig`
- example of `base.twig` with a custom script import for `tina4helper.js`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <script src="/js/tina4helper.js"></script>
    <title>{{ title }}</title>
</head>
<body>
{% block content %}
{% endblock %}
</body>
</html>
```

- the above script import will allow you to send api requests using Tina4, from the templates inheriting from `base.twig`
- how to create other pages inheriting from `base.twig`:

```html
{% extends "base.twig" %}
{% set container_class ="main-content-container" %}
{% block content %}
    --- ALL THE CONTENT OF THE PAGE GOES HERE ---
    <h2>This is a heading</h2>
    <p>This is a paragraph</p>
{% endblock %}
```
