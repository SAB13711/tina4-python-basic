# Setting up new tina4_python project

## Initializing Project and File Structure

### Guide for initial setup of project and file structure using Poetry and Tina4

> [Download and Install Python](https://www.python.org/downloads/)  
> [Official Tina4 installation guide](https://www.tina4.com/getting-started/python/index.html)

- create empty folder with project name
- open folder in console, or open console and `cd` into folder
- run command: `pip install poetry`
- run command: `poetry init`
    - this will prompt you for project details, default are good except for:
        - python version should be: `<4.0,>=3.12`
        - input `no` for the two dynamic questions
- run command: `poetry add tina4_python`
- create a new file in the folder, call it `app.py`
    - in the file, put one line: `import tina4_python`
- in console, run command: `poetry run python app.py`
- at this point:
    - you should have a running webserver at `http://127.0.0.1:7145` - this will show error page
    - the file structure should be created
- move to the console, and press `CTRL + c` to stop the server
- to run the server again, run `poetry run python app.py` in the console

### Project Structure

```
Project Folder Layout:
    - secrets (ignore for now)
    - migrations (create if needed)
    - src
        - app : classes go here - things like 'user_service' or 'product_service' that have functions related to their topic
        - orm : database ORM classes go here - can be generated with Tina4, see database guide
        - public : any public files to be served - treated as /
            - css
            - images
            - js
            - swagger
        - routes : routing logic goes here - routes and endpoints
        - scss: scss files go here and are compiled to public/css - styling files
        - templates : jinja2/twig templates go here - all the pages and their parts
            - errors : error pages for 404 & 403 go here and can be customized
```
