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
    
    brand: str = request.args.get("brands")
    price_sort = request.args.get("price_sort")
    mainQuery = "SELECT * FROM CPU"
    brandFilter = "SELECT CPUBrand FROM CPU"
    
    print(f"This is what is in brand: {brand}") # Delete this

    # mainQuery for sorting
    if brand not in ('-- Brands --', ''):
        mainQuery += f" WHERE CPUBrand = '{brand}'"
    if price_sort in ('ASC', 'DESC'):
        mainQuery += f" ORDER BY CPUPrice {price_sort}"

    cursor.execute(mainQuery)
    
    # Get result and close
    mainResult = cursor.fetchall() # Gets result from query
    cursor.execute(brandFilter) # Gets brands from CPU query
    brandResult = cursor.fetchall()
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return [mainResult, brandResult]

def get_pwr():
    # Create a new database connection for each request
    conn = get_db_connection()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    
    brand: str = request.args.get("brands")
    price_sort = request.args.get("price_sort")
    mainQuery = "SELECT * FROM PowerSupply"
    brandFilter = "SELECT PWRBrand FROM PowerSupply"

    # mainQuery for sorting
    if brand not in ('-- Brands --', '', None):
       mainQuery += f" WHERE PWRBrand = '{brand}'"
    if price_sort in ('ASC', 'DESC'):
        mainQuery += f" ORDER BY PWRPrice {price_sort}"

    cursor.execute(mainQuery)
    
    # Get result and close
    mainResult = cursor.fetchall() # Gets result from query
    cursor.execute(brandFilter) # Gets brands from CPU query
    brandResult = cursor.fetchall()
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return [mainResult, brandResult]

def get_mem():
    # Create a new database connection for each request
    conn = get_db_connection()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    
    brand: str = request.args.get("brands")
    price_sort = request.args.get("price_sort")
    mainQuery = "SELECT * FROM Memory"
    brandFilter = "SELECT RAMBrand FROM Memory"

    # mainQuery for sorting
    if brand not in ('-- Brands --', '', None):
       mainQuery += f" WHERE RAMBrand = '{brand}'"
    if price_sort in ('ASC', 'DESC'):
        mainQuery += f" ORDER BY RAMPrice {price_sort}"

    cursor.execute(mainQuery)
    
    # Get result and close
    mainResult = cursor.fetchall() # Gets result from query
    cursor.execute(brandFilter) # Gets brands from CPU query
    brandResult = cursor.fetchall()
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return [mainResult, brandResult]

def get_gpu():
    # Create a new database connection for each request
    conn = get_db_connection()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    
    brand: str = request.args.get("brands")
    price_sort = request.args.get("price_sort")
    mainQuery = "SELECT * FROM GPU"
    brandFilter = "SELECT GPUBrand FROM GPU"

    # mainQuery for sorting
    if brand not in ('-- Brands --', '', None):
       mainQuery += f" WHERE GPUBrand = '{brand}'"
    if price_sort in ('ASC', 'DESC'):
        mainQuery += f" ORDER BY GPUPrice {price_sort}"

    cursor.execute(mainQuery)
    
    # Get result and close
    mainResult = cursor.fetchall() # Gets result from query
    cursor.execute(brandFilter) # Gets brands from CPU query
    brandResult = cursor.fetchall()
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return [mainResult, brandResult]

def get_storage():
    # Create a new database connection for each request
    conn = get_db_connection()  # Create a new database connection
    cursor = conn.cursor() # Creates a cursor for the connection, you need this to do queries
    
    brand: str = request.args.get("brands")
    price_sort = request.args.get("price_sort")
    mainQuery = "SELECT * FROM Storage"
    brandFilter = "SELECT StorBrand FROM Storage"

    # mainQuery for sorting
    if brand not in ('-- Brands --', '', None):
       mainQuery += f" WHERE StorBrand = '{brand}'"
    if price_sort in ('ASC', 'DESC'):
        mainQuery += f" ORDER BY StorPrice {price_sort}"

    cursor.execute(mainQuery)
    
    # Get result and close
    mainResult = cursor.fetchall() # Gets result from query
    cursor.execute(brandFilter) # Gets brands from CPU query
    brandResult = cursor.fetchall()
    conn.close() # Close the db connection (NOTE: You should do this after each query, otherwise your database may become locked)
    return [mainResult, brandResult]

def get_filtered_data():
    # Using a form to get the filter parameters
    data = request.form
    priceASC = data["priceASC"]
    priceDESC = data["priceDESC"]
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
    cpu_data: list = get_cpu() # Call defined function to get all items
    # filtered_results = get_filtered_data() # I'm don't think this will work since we need data from the rendered page before the page is rendered. 
    return render_template("browse_cpu.html", data=cpu_data[0], filter=cpu_data[1])

@app.route("/GPU", methods=["GET"])
def browse_gpu():
    gpu_data: list = get_gpu() # Call defined function to get all items
    # filtered_results = get_filtered_data() # I'm don't think this will work since we need data from the rendered page before the page is rendered. 
    return render_template("browse_gpu.html", data=gpu_data[0], filter=gpu_data[1])

@app.route("/PowerSupply", methods=["GET"])
def browse_pwr():
    pwr_data: list = get_pwr() # Call defined function to get all items
    # filtered_results = get_filtered_data() # I'm don't think this will work since we need data from the rendered page before the page is rendered. 
    return render_template("browse_pwr.html", data=pwr_data[0], filter=pwr_data[1])

@app.route("/Storage", methods=["GET"])
def browse_storage():
    storage_data: list = get_storage() # Call defined function to get all items
    # filtered_results = get_filtered_data() # I'm don't think this will work since we need data from the rendered page before the page is rendered. 
    return render_template("browse_storage.html", data=storage_data[0], filter=storage_data[1])

@app.route("/Motherboard", methods=["GET"])
def browse_mobo():
    mobo_data: list = get_mobo() # Call defined function to get all items
    # filtered_results = get_filtered_data() # I'm don't think this will work since we need data from the rendered page before the page is rendered. 
    return render_template("browse_mobo.html", data=mobo_data[0], filter=mobo_data[1])

@app.route("/Memory", methods=["GET"])
def browse_mem():
    mem_data: list = get_mem()
    return render_template("browse_memory.html", data=mem_data[0], filter=mem_data[1])

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