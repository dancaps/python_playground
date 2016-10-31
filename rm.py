#! /usr/bin/python

from plumbum import *

#remote_hosts = ['10.0.0.52']

r_host = SshMachine('10.0.0.52')

print r_host, "is now connected"
#r_cd = r_host['cd ~']
#r_cd()

with r_host.cwd(r_host.cwd / "Desktop"):
    print r_host.cwd, "is the working directory"
    r_touch = r_host['touch Hello_World!']
    #r_touch()
    #r_ls = r_host['ls']
    #print r_ls

r_host.close
print r_host, " is now disconnected!"
print "Goodbye"

