import sqlite3
from bottle import PasteServer
from bottle import route, run, debug, template, request, static_file, error, redirect
# only needed when you run Bottle on mod_wsgi
from bottle import default_app

'''
Define the default route to redirect to '/todo' 
'''
@route('/')
def index():
    redirect('/todo') # Set home page

'''
Define the route to display the list of todo items
'''
@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')  # Connect to the SQLite database named 'todo.db'
    c = conn.cursor()  # Create a cursor for executing SQL commands
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")  # Execute an SQL query to select tasks with status '1'
    result = c.fetchall()  # Fetch all the results from the query
    c.close()  # Close the database connection

    output = template('make_table', rows=result)  # Use a template to create an HTML table with the results
    return output
'''
Define the route for adding a new todo item
'''
@route('/new', method='GET')
def new_item():
    if request.GET.save:  # Check if the 'save' parameter is present in the GET request
        new = request.GET.task.strip()  # Get the 'task' parameter from the GET request and strip any leading/trailing whitespace

        conn = sqlite3.connect('todo.db')  # Connect to the SQLite database named 'todo.db'
        c = conn.cursor()  # Create a cursor for executing SQL commands

        c.execute("INSERT INTO todo (task, status) VALUES (?, ?)", (new, 1))  # Insert a new task with status '1' into the database
        new_id = c.lastrowid  # Get the ID of the newly inserted task

        conn.commit()  # Commit the changes to the database
        c.close()  # Close the database connection
        redirect('/todo')  # Redirect to the '/todo' route
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

    else:
        return template('new_task.tpl')  # Display a form for adding a new task

'''
Define the route for editing an existing todo item
'''
@route('/edit/<no:int>', method='GET')
def edit_item(no):
    if request.GET.save:  # Check if the 'save' parameter is present in the GET request
        edit = request.GET.task.strip()  # Get the 'task' parameter from the GET request and strip any leading/trailing whitespace
        status = request.GET.status.strip()  # Get the 'status' parameter from the GET request and strip any leading/trailing whitespace

        if status == 'open':  # Check if the status is 'open'
            status = 1  # Set the status to 1
        else:
            status = 0  # Otherwise, set the status to 0

        conn = sqlite3.connect('todo.db')  # Connect to the SQLite database named 'todo.db'
        c = conn.cursor()  # Create a cursor for executing SQL commands
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))  # Update the task and status of the specified ID
        conn.commit()  # Commit the changes to the database
        redirect('/todo')  # Redirect to the '/todo' route
        return '<p>The item number %s was successfully updated</p>' % no

    else:
        conn = sqlite3.connect('todo.db')  # Connect to the SQLite database named 'todo.db'
        c = conn.cursor()  # Create a cursor for executing SQL commands
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))  # Retrieve the task for the specified ID
        cur_data = c.fetchone()  # Fetch the result

        return template('edit_task', old=cur_data, no=no)  # Display a form for editing the task

'''
Define the route for deleting a todo item
'''
@route('/delete/<no:int>', method='GET')
def delete_item(no):
    conn = sqlite3.connect('todo.db')  # Connect to the SQLite database named 'todo.db'
    c = conn.cursor()  # Create a cursor for executing SQL commands
    c.execute("DELETE FROM todo WHERE id = ?", (no,))  # Delete the task with the specified ID
    conn.commit()  # Commit the changes to the database
    redirect('/todo')  # Redirect to the '/todo' route
    return '<p>The item number %s was successfully deleted</p>' % no

'''
Define a route to show a specific todo item
'''
@route('/item<item:re:[0-9]+>')
def show_item(item):
    conn = sqlite3.connect('todo.db')  # Connect to the SQLite database named 'todo.db'
    c = conn.cursor()  # Create a cursor for executing SQL commands
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))  # Retrieve the task for the specified ID
    result = c.fetchall()  # Fetch the result
    c.close()  # Close the database connection
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' % result[0]

'''
Define a route to show a specific todo item in JSON format
'''
@route('/json<json:re:[0-9]+>')
def show_json(json):
    conn = sqlite3.connect('todo.db') # Connect to the SQLite database named 'todo.db'
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,)) # Retrieve the task for the specified I
    result = c.fetchall() # Fetch the result
    c.close() # Close the database connection

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}

'''
Define custom error handlers
'''
@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

'''
Define a route to serve a help page
'''
@route('/help')
def help():
    return static_file('help.html', root='.')


debug(True) # Enable debugging


run(reloader=True) # Run the Bottle web application
