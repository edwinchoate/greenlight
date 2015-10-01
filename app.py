
from flask import Flask, render_template
import socket

app = Flask(__name__)
host = '50.155.99.140'    # The remote host
port = 50007              # The same port as used by the server

@app.route('/')
def greenlight():
    data = getData("get_status")
    print repr(data)
    if data == "0 0 1":
        return render_template('red.html')
    elif data == "0 1 0":
        return render_template('yellow.html')
    elif data == "1 0 0":
        return render_template('green.html')
    else:
        getData("all_off")
        return render_template('index.html')

@app.route('/<light_name>')
def lightOn(light_name):
    getData("all_off")
    if light_name == 'green':
        getData("green_on")
    elif light_name == 'yellow':
        getData("yellow_on")
    elif light_name == 'red':
        getData("red_on")
    return render_template(str(light_name) + '.html')
           
@app.route('/off')
def allOff():
    getData("all_off")
    return render_template('off.html')
    
def getData(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(message)
    data = s.recv(1024)
    s.close()
    print repr(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)


