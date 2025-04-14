from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from llm_helper import ask_llm
from lldb_driver import LLDBDriver
import sys

app = Flask(__name__)
socketio = SocketIO(app)
lldb_driver = None
lldb_log = ""

def initialise_lldb_context():
    global lldb_log
    lldb_driver.run_command("breakpoint set --name main")
    lldb_driver.run_command("run")
    lldb_driver.run_command("frame info")
    lldb_driver.run_command("source list")
    socketio.sleep(2.0)
    context = lldb_driver.get_output()
    lldb_log += context + "\n"
    return context

def get_lldb_context():
    global lldb_log
    cmds = [
        "frame select 0",
        "frame info",
        "source list",
        "vo"
    ]
    context = ""
    for cmd in cmds:
        lldb_driver.run_command(cmd)
        socketio.sleep(0.2)
        output = lldb_driver.get_output()
        if output.strip():  # skip empty output
            context += f"$ {cmd}\n{output}\n"

    lldb_log += context + "\n"
    return context

@app.route('/')
def index():
    print('rendering /')
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    context = initialise_lldb_context()
    emit('context_update', {'context': context})

@socketio.on('user_message')
def handle_message(data):
    msg = data['message']
    if msg.startswith('!lldb '):
        command = msg[len('!lldb '):]
        lldb_driver.run_command(command)
        socketio.sleep(2.0)
        output = lldb_driver.get_output()
        emit('bot_message', {'message': output})
        emit('context_update', {'context': output})
    else:
        context = get_lldb_context()
        reply = ask_llm(f"LLDB log: {lldb_log}\nLLDB Context:\n{context}\n\nUser asked: {msg}")
        emit('bot_message', {'message': reply})

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: vibe_debugging.py <executable>")
        sys.exit(1)
    lldb_driver = LLDBDriver(sys.argv[1])
    socketio.run(app, debug=True)
