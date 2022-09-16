"""
NO FUNCTIONS SHOULD BE ADDED OR REMOVED FROM THIS MODULE. SIMPLY COMPLETE EACH FUNCTION AS DESCRIBED.
YOU SHOULD ALSO NOT REMOVE ANY OF THE COMMENTS OR CHANGE THE STRUCTURE IN ANY WAY OTHER THAN AS INSTRUCTED.

This module is responsible for setting up and querying the database.
"""
import sqlite3
import file
import tui


def execute(action, headings, records):

    """
    Task 22: Execute database action.

    The function should check the value of action (which is the database menu option specified by the user)
    and execute the relevant database function.
    For example,
        If action is 1 then the function should invoke the setup_database function.
        If action is 2 then the function should invoke the retrieve_customers_alphabetically function.

    In each case, with the exception of the setup_database function, the result of executing relevant database function
    should be displayed using the appropriate tui function.
    For example,
        The result of executing the retrieve_customers_alphabetically function should be displayed using the tui
        display_records function.

    If the action is invalid then the error message 'Invalid selection.' should be displayed using the tui error
    function.

    :param action: An integer indicating which action (database option) to perform.
    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: Does not return anything.
    """
    headings = (file.load_data()[0])
    records = (file.load_data()[1])

    if action == 1:
        print(setup_database(headings, records))
    elif action == 2:
        print(retrieve_customers_alphabetically())
    elif action == 3:
        print(retrieve_total_product_sales())
    elif action == 4:
        print(retrieve_top_product_categories())
    elif action == 5:
        print(retrieve_top_product_subcategories())
    else:
        print(tui.error("Invalid selection"))


def setup_database(headings, records):
    """
    Task 23: Create a database and populate it.

    The function should create a database named 'sales.db' stored in the 'data' folder with a single table
    named 'records'.
    The function should populate the database using the records passed as a parameter.

    For higher marks (advance task):
        - Normalise the database into 2 or more tables.
    """
    db = sqlite3.connect("data/sales.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE records (
        'Record ID' INTEGER,
        'Order ID' TEXT,
        'Order Date' TEXT,
        'Ship Date' TEXT,
        'Ship Mode' TEXT,
        'Customer ID' TEXT,
        'Customer Name' TEXT,
        'Segment' TEXT,
        'Country' TEXT,
        'City' TEXT,
        'State' TEXT,
        'Postal Code' TEXT,
        'Region' TEXT,
        'Product ID', TEXT,
        'Category' TEXT,
        'Sub-category' TEXT,
        'Product Name' TEXT,
        'Sales' REAL,
        'Quantity' INTEGER,
        'Discount' REAL,
        'Profit' REAL
    );""")



    record = """INSERT INTO records ('Record ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name',
    'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Sales',
    'Quantity', 'Discount', 'Profit') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    for i in records:
        cursor.execute(record, i)

    db.commit()








def retrieve_customers_alphabetically():
    """
    Task 24: Retrieve customers sorted alphabetically.

    The function should query the database to retrieve all customer names sorted alphabetically
    by first name and then last name.
    The function should return the results.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return A list or tuple containing the records retrieved from the database.
    """
    db = sqlite3.connect("data/sales.db")
    cursor = db.cursor()
    cursor.execute("SELECT \"customer name\" FROM records")
    all_records = cursor.fetchall()
    customer_name = []
    for i in sorted(all_records):
        customer_name.append(i)
    return customer_name






def retrieve_total_product_sales():
    """
    Task 25: Retrieve the total product sales.

    The function should query the database to retrieve the total sales for each product.
    The function should sort the results by the product name in alphabetical and ascending order.
    The function should return the results.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A list or tuple containing the records retrieved from the database.
    """
    db = sqlite3.connect("data/sales.db")
    cursor = db.cursor()

    cursor.execute("SELECT \"product name\", SUM(sales) FROM records GROUP BY \"product name\"")
    all_records = cursor.fetchall()

    product_name = []
    for i in sorted(all_records):
        product_name.append(i)

    return product_name


def retrieve_top_product_categories():
    """

    Task 26: Retrieve the top 3 product categories.

    The function should query the database to retrieve the top 3 product categories.
    The top 3 product categories are the categories of products that result in the highest profits.
    The results should include the name of the category and the amount of profit.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A list or tuple containing the records retrieved from the database.
    """
    db = sqlite3.connect("data/sales.db")
    cursor = db.cursor()

    cursor.execute("SELECT category, SUM(profit) FROM records GROUP BY category ORDER BY category DESC LIMIT 3;")
    all_records = cursor.fetchall()
    
    return all_records

print(retrieve_total_product_sales())










def retrieve_top_product_subcategories():
    """
    Task 27: Retrieve the top 3 product sub-categories.

    The function should query the database to retrieve the top 3 product sub-categories for specific dates.
    The dates will be specified by the user.
    The top 3 product sub-categories are those that have the highest sales on the specified dates.
    The results should include the name of each sub-category and the amount of sales for each sub-category.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A dictionary where the keys are the dates and the values are the top 3 product sub-categories (with
    the name and the sales for each sub-category) for that date.
    """
    print(Order_date)
    input("Enter a Order_date")
    db = sqlite3.connect("data/sales.db")
    cursor = db.cursor()
    

