import pexpect
import sys

sshcmd = sys.argv[1]
password = sys.argv[2]
exp = pexpect.spawn(sshcmd)
index =exp.expect(['(yes/no)', 'password:', pexpect.EOF, pexpect.TIMEOUT], timeout=20)
if index == 0 :
    exp.sendline('yes')
    exp.expect('password:')
    exp.sendline(password)
elif index == 1:
    exp.sendline(password)
elif index == 2 :
    pass
else:
    print('can not exectute %s, dest is not achived' % sshcmd)
exp.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=5)
