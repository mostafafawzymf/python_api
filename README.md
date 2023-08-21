# python_api

Python script to extract customer and load the transformed data into a PostgreSQL database and create an API

the code workflow as follworing :-
1-read the CSV files
2-trancform the csv files into a dataframe in pandas python
3-load_data_to_postgres

Installation on Linux
To set up the project on a Linux system, follow these steps:

Clone the repository:

Open a terminal and navigate to the directory where you want to clone the repository.


git clone[ https://github.com/your-username/customer-data-etl.git](https://github.com/mostafafawzymf/python_api/tree/main)
cd customer-data-etl
Install Required Packages:

Make sure you have Python 3.x installed. If not, you can install it using your package manager. For example, on Ubuntu:


sudo apt update
sudo apt install python3
Next, install the required Python packages:


pip3 install pandas psycopg2 Flask
Database Setup:

Install PostgreSQL if you don't have it already:



sudo apt install postgresql postgresql-contrib
Start and enable the PostgreSQL service:



sudo systemctl start postgresql
sudo systemctl enable postgresql
Create a PostgreSQL database named customer_data_db and a user:


sudo -u postgres createdb customer_data_db
sudo -u postgres createuser --interactive
Set a password for the user when prompted.


