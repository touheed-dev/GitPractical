from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker! This Flask app is running."

@app.route("/db")
def db_test():
    try:
        connection = mysql.connector.connect(
            host="db",
            database="flaskdb",
            user="flaskuser",
            password="flaskpassword"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result and result[0] == 1:
            return "Flask + MySQL connection successful. SQL check: SELECT 1 returned 1."
        return "Flask app connected to MySQL, but query result was unexpected."

    except Exception as e:
        return f"Flask + MySQL connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
