""" Module 5 project: Working with SQL
"""
# Standard library imports
import csv
import logging
from pathlib import Path
import json
import pandas as pd
import xlrd
import sqlite3

# External library imports (requires virtual environment)

# Local module imports

# Set up logging and configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method

# Define the database file in the current root project directory
db_file = Path("blog_user_project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        user_data_path = Path("data", "users_data.csv")
        posts_data_path = Path("data", "posts_data.csv")
        users_df = pd.read_csv(user_data_path)
        posts_df = pd.read_csv(posts_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            users_df.to_sql("users", conn, if_exists="replace", index=False)
            posts_df.to_sql("posts", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def execute_sql_from_file(db_filepath, sql_file):
    """Execute SQL script from a file."""
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        print(f"Error executing {sql_file}: {e}")


def main():
    logging.info("Program started")
    create_database()
    create_tables()
    insert_data_from_csv()
    # Add calls to execute_sql_from_file here for each SQL file
    execute_sql_from_file(db_file, Path("sql", "delete_records.sql"))
    execute_sql_from_file(db_file, Path("sql", "insert_records.sql"))
    execute_sql_from_file(db_file, Path("sql", "query_aggregation.sql"))
    execute_sql_from_file(db_file, Path("sql", "query_filter.sql"))
    execute_sql_from_file(db_file, Path("sql", "query_group_by.sql"))
    execute_sql_from_file(db_file, Path("sql", "query_join.sql"))
    execute_sql_from_file(db_file, Path("sql", "query_sorting.sql"))
    execute_sql_from_file(db_file, Path("sql", "update_records.sql"))

logging.info("Program ended")

if __name__ == "__main__":
    main()