### datafun-05-sql by Jason Ballard February 5 2024

# Project Overview

DataFun-05-SQL is designed to provide hands-on experience with SQL, focusing on SQLite for managing and querying databases. This project emphasizes the fundamentals of SQL alongside best practices in project setup and management. It's an ideal starting point for those looking to enhance their data manipulation and analysis skills with SQL.

## Getting Started
✅ Create a GitHub project repository with a default README.md.

✅ Clone new project repo down to local machine. 

✅ Open the new project folder in VS Code.

✅ Add  to the .gitignore with .vsode/ and .venv/ 

✅ Create and activate a local virtual environment in .venv.

✅ Install dependencies into your .venv (pandas and pyarrow) and freeze into the requirements.txt. 

✅ Record the commands used in README.md. 

✅ Git add and commit with a useful message (e.g. "initial commit") and push to GitHub.

✅ Create first project files (usually in VS Code). 

Remember to save work, git add / commit / push to GitHub.

## Objective

### 1. Environment setup
The environment set up is beginning to become second nature. 

Ensure that the github versioning is setup and operational. The following code was used to set up git:
```bash
git clone https://github.com/JBtallgrass/datafun-05-sql.git
git remote -v
```
### 2. Project start

Set up up the virtual environment is important so that any development within a project doesn't interfere with the machine environment. The following code was used to develop the virtual environment for the project: 
```bash
python -m venv .venv
# activate .venv
source .venv/scripts/activate
```
``` bash
install dependencies
python -m pip install pandas pyarrow
# requirements.txt freeze
python -m pip freeze > requirements.txt
```

### 3. Import Dependencies
The followng dependencies were imported for use in the project:
```bash
# import dependencies
import csv
import logging
from pathlib import Path
import json
import pandas as pd
import pyarrow
import sqlite3
```
### 4. Logging



### 5. Database creation and Schema design
# Blog Database Schema

This document describes the database schema for a simple blog system.

## Tables

### Users

- `user_id`: INT, Primary Key, auto-increment
- `username`: VARCHAR(255), unique
- `email`: VARCHAR(255), unique
- `created_at`: TIMESTAMP, default CURRENT_TIMESTAMP

### Posts

- `post_id`: INT, Primary Key, auto-increment
- `user_id`: INT, Foreign Key (References `Users.user_id`)
- `title`: VARCHAR(255)
- `content`: TEXT
- `published_at`: TIMESTAMP, default CURRENT_TIMESTAMP

## Relationships

- Each `Post` is associated with one `User` through `user_id`.



### 6. SQL operations



### 7. Integration (python and SQL)



### 8. Main function



### 9. Conditional script execution


## Project development images

