
from flask import Flask, render_template
import socket


app = Flask(__name__)

@app.route('/')
def greenlight():
    HOST = '50.155.99.140'    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall("all_off")
    data = s.recv(1024)
    s.close()
    print repr(data)
    return render_template('index.html')

@app.route('/<light_name>')
def turn_on_light(light_name):
    all_off_helper()
    if light_name == 'green':
        HOST = '50.155.99.140'    # The remote host
        PORT = 50007              # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall("green_on")
        data = s.recv(1024)
        s.close()
        print repr(data)
    elif light_name == 'yellow':
        HOST = '50.155.99.140'    # The remote host
        PORT = 50007              # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall("yellow_on")
        data = s.recv(1024)
        s.close()
        print repr(data)
    elif light_name == 'red':
        HOST = '50.155.99.140'    # The remote host
        PORT = 50007              # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall("red_on")
        data = s.recv(1024)
        s.close()
        print repr(data)
    return render_template(str(light_name) + '.html')
           
@app.route('/off')
def turn_all_off():
    all_off_helper()
    return render_template('off.html')

def all_off_helper():
    HOST = '50.155.99.140'    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall("all_off")
    data = s.recv(1024)
    s.close()
    print repr(data)

if __name__ == '__main__':
    app.run(debug=True)