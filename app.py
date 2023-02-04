from flask import Flask, request
import redis
import mysql.connector
from prometheus_flask_exporter import PrometheusMetrics



app = Flask(__name__)

metrics = PrometheusMetrics(app)
# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

# Connect to Redis database
redis_db = redis.Redis(host="redis", port=6379)

# Connect to MySQL database
mysql_db = mysql.connector.connect(
    host="db",
    user="test",
    password="test",
    database="test"
)

@app.route("/")
def index():
    # Increment the number of visits in Redis
    visits = redis_db.incr("visits")

    # Retrieve the latest messages from MySQL
    cursor = mysql_db.cursor()
    cursor.execute("SELECT message FROM messages ORDER BY id DESC LIMIT 10")
    messages = cursor.fetchall()

    return f"""
        <html>
            <body>
                <h1>Vous êtes le visiteur n°  {visits}.</h1>
                <p> Dernier messages :</p>
                <ul>
                    {
                        "".join([f"<li>{message}</li>" for message in messages])
                    }
                </ul>
                <form method="post">
                    <input type="text" name="message" />
                    <input type="submit" value="Send" />
                </form>
            </body>
        </html>
    """

@app.route("/", methods=["POST"])
def add_message():
    # Retrieve the message from the form
    message = request.form["message"]

    # Store the message in the database
    cursor = mysql_db.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    mysql_db.commit()

    return "Message sent!"

@app.route("/test", methods=["GET"])
def test():
    if request.method == "GET":
        return "response: Welcome to Falsk application"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
