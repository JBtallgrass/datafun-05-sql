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


def execute_sql_from_file(filename, connection):
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()
    connection.executescript(sql_script)

def main():
    conn = sqlite3.connect('blog.db')
    execute_sql_from_file('create_users_table.sql', conn)
    execute_sql_from_file('create_posts_table.sql', conn)
    execute_sql_from_file('insert_users.sql', conn)
    execute_sql_from_file('insert_posts.sql', conn)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()











logging.info("Program ended")  # add this at the end of the main method

if __name__ == "__main__":
    main()


# Objective

# Database creation and Schema design

# SQL operations

# Integration (python and SQL)

# Main function

# Conditional script execution