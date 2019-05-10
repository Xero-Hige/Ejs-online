
import subprocess
from subprocess import PIPE

class RunCode:

    def __init__(self,filename):
        self.filename = './/' + filename
    
    def run(self):
        proc = subprocess.Popen(['python3', self.filename, '-v'],stdout=PIPE, stderr=PIPE)
        try:
            outs, errs = proc.communicate(timeout=4)
            errs = errs.decode('UTF-8')
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            errs = 'TimeoutExpires exception'
        return errs
