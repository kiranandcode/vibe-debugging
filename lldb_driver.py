import subprocess
import threading

class LLDBDriver:
    def __init__(self, exe_path):
        self.proc = subprocess.Popen(
            ['lldb', exe_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        self.output_lines=[]
        self._start_reader_thread()

    def _start_reader_thread(self):
        def reader():
            for line in self.proc.stdout:
                self.output_lines.append(line)
        threading.Thread(target=reader, daemon=True).start()

    def run_command(self, command):
        self.proc.stdin.write(command + '\n')
        self.proc.stdin.flush()

    def get_output(self):
        out = ''.join(self.output_lines)
        self.output_lines.clear()
        return out
