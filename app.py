from flask import Flask
import getpass
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Manjunath"
    username = getpass.getuser()

    # Get time in IST
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top command output
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    return f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
