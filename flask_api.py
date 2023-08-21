from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Establish a connection to PostgreSQL
def create_db_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        database="testdb",
        user="postgres",
        password="welcome1"
    )

# Define API route
@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_data(customer_id):
    db_connection = create_db_connection()
    cursor = db_connection.cursor()

    query = f"SELECT * FROM customer_data WHERE customer_id = {customer_id};"
    cursor.execute(query)
    customer_data = cursor.fetchone()
    
    db_connection.close()

    if customer_data:
        # Convert the tuple result to a dictionary for JSON response
        customer_dict = {
            "customer_id": customer_data[0],
            "first_name": customer_data[1],
            "last_name": customer_data[2],
            "email": customer_data[3],
            "phone_number": customer_data[4],
            "city": customer_data[5],
            "state": customer_data[6],
            "zip_code": customer_data[7]
        }
        return jsonify(customer_dict)
    else:
        return jsonify({"message": "Customer not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

