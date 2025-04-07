import os
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Initialize the flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET")


# ------------------------ BEGIN FUNCTIONS ------------------------ #
# Function to retrieve DB connection
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),     
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    return conn

# Get all items from the "items" table of the db
def get_all_categories():
    # Create a new database connection for each request
    conn = get_db_connection()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    # Query the db
    query = "SELECT Distinct table_name FROM HomePage"
    cursor.execute(query)
    # Get result and close
    result = cursor.fetchall() # Gets result from query
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return result

def get_cpu():
    # Create a new database connection for each request
    conn = get_db_connection()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    # Query the db
    query = "SELECT * FROM CPU"
    '''
    default query = above
    l2hquery = filtered
    h2low = filtered
    if default values are met:
        cursor.execture(default_query)
    else if form is set to l2h
        cursor.executre(filtered)
    '''

    '''
    if something query = SELECT....
    else if something other = SELECT other...

    cursor.execute(query)
    '''

    data = request.form
    priceASC = data["priceASC"]
    priceDESC = data["priceDESC"]
    if priceASC == "on":
        query = "SELECT * FROM CPU ORDER BY price ASC"
    elif priceDESC == "on":
        query = "SELECT * FROM CPU ORDER BY price DESC"
    else:
        query = "SELECT * FROM CPU"

    cursor.execute(query)
    # Get result and close
    result = cursor.fetchall() # Gets result from query
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return result

def get_filtered_data():
    # Using a form to get the filter parameters
    data = request.form
    price = data["price"]
    brand = data["brand"]
    table_name = data["name"]
    # Might want to do an if here to add more filters
    conn = get_db_connection() # Now that we have the filter parameters we can create a db connection
    cursor = conn.cursor()

    query = "SELECT * FROM " + table_name + " WHERE " + table_name + "brand = " + brand + " AND " + table_name + "price = " + price + ";"

    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# ------------------------ END FUNCTIONS ------------------------ #


# ------------------------ BEGIN ROUTES ------------------------ #
# EXAMPLE OF GET REQUEST
@app.route("/", methods=["GET"])
def home():
    categories= get_all_categories() # Call defined function to get all items
    return render_template("index.html", items=categories) # Return the page to be rendered

@app.route("/CPU", methods=["GET"])
def browse_cpu():
    cpu_data = get_cpu() # Call defined function to get all items
    # filtered_results = get_filtered_data() # I'm don't think this will work since we need data from the rendered page before the page is rendered. 
    return render_template("browse_cpu.html", data=cpu_data)

# EXAMPLE OF POST REQUEST
@app.route("/new-item", methods=["POST"])
def add_item():
    try:
        # Get items from the form
        data = request.form
        item_name = data["name"] # This is defined in the input element of the HTML form on index.html
        item_quantity = data["quantity"] # This is defined in the input element of the HTML form on index.html

        # TODO: Insert this data into the database
        
        # Send message to page. There is code in index.html that checks for these messages
        flash("Item added successfully", "success")
        # Redirect to home. This works because the home route is named home in this file
        return redirect(url_for("home"))

    # If an error occurs, this code block will be called
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error") # Send the error message to the web page
        return redirect(url_for("home")) # Redirect to home
# ------------------------ END ROUTES ------------------------ #


# listen on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) # TODO: Students PLEASE remove debug=True when you deploy this for production!!!!!