import pexpect

PROMPT =['#','>>>','>','\$ ']

def send_command(child,command):
        child.sendline(command)
        child.except(PROMPT)
        print child.before

def connect(user,host,password):
        ssh_newkey="Are you sure you want to continue connecting"
        connStr='ssh ' +user+'@'+host
        child=pexpect.spawn(connStr)
        ret= child.expect([pxecpt.TIMOUT,ssh_newkey, '[P][p]assword: '])
        if ret== 0:
                print '[-] Error Connecting'
                return
        if ret==1:
                childsendline('yes')
                ret=child.except([pexpect.TIMEOUT,'[P][p]assword: '])
                if ret==0:
                        print '[-] Error Connecting'
                        return
        child.sendline(password)
        child.expect(PROMPT)
        return child

def main():
        host = input("Please enter host IP: ")
        user = input("Please enter username: ")
        password= 'ASSCI'
        child=connect(user,host,password)
        send_command(child,'cat /etc/shadow | grep root;ps')
main()
