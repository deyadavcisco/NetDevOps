#!/usr/bin/env python2

import paramiko # used to create SSH sessions
import time # used to insert pauses in the script

# a list of the hosts we wish to access
hosts = ["198.18.1.31", "198.18.1.32", "198.18.1.33", "198.18.1.34"]

# NXOS login details
username = "cisco"
password = "cisco"

# Create a new Paramiko SSH connection object
conn = paramiko.SSHClient()
# Automatically add SSH hosts keys
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# For each host we wish to connect to
for host in hosts:
        print "--------------------",host,"--------------------"
        # create a shell session for multiple commands
        conn.connect(host, 22, username, password, look_for_keys=False, allow_agent=False)
        remote_shell = conn.invoke_shell()
        time.sleep(2)
        # receive remote host shell output
        output = remote_shell.recv(65535)
        # display the output
        print output

        # send the command "configure terminal"
        remote_shell.send("configure terminal\n")
        time.sleep(1)
        output = remote_shell.recv(65535)
        print output

        # Enable feature NXAPI
        remote_shell.send("feature nxapi\n")
        time.sleep(5)
        output = remote_shell.recv(65535)
        print output

        # Enable NXAPI HTTP port 80
        remote_shell.send("nxapi http port 80\n")
        time.sleep(1)
        output = remote_shell.recv(65535)
        print output

        # exit the configuration mode
        remote_shell.send("end\n")
        time.sleep(1)
        output = remote_shell.recv(65535)
        print output
        time.sleep(1)

        # close the SSH session to this host we can re-use the object for the
        # next host
        conn.close()
