from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Sarfaraz Ahmed"  # Apna naam likho
    username = os.getlogin()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 'top' command ka output lene ke liye
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    # HTML format me display karna
    return f"""
    <h2>Name: {name}</h2>
    <h3>Username: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>TOP output:\n{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
