import os

class Popen:
    def __init__(self, cmd, stdin=None, stdout=None, stderr=None):
        if stdin is None:
            stdin, self.stdin = os.pipe()
            self.stdin = open(self.stdin, 'wb')
        if stdout is None:
            self.stdout, stdout = os.pipe()
            self.stdout = open(self.stdout, 'rb')
        if stderr is None:
            self.stderr, stderr = os.pipe()
            self.stderr = open(self.stderr, 'rb')
            
        self.child = os.fork()
        if self.child:
            return
        os.close(0)
        os.close(1)
        os.close(2)
        os.dup(stdin)
        os.dup(stdout)
        os.dup(stderr)
        os.execvp(cmd[0], cmd)
    def wait(self):
        r = os.waitpid(self.child, 0)
        return r[1]
        
        
