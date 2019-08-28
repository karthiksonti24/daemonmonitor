#!/usr/bin/env python

import sys
import subprocess


class DaemonMonitor(object):

    def __init__(self, service):
        self.service = service

    def is_active(self):
        """Usage:Used to Check whether given service is running"""
        cmd = '/bin/systemctl status %s.service' % self.service
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        print proc
        stdout_list = proc.communicate()[0].split('\n')
        for line in stdout_list:
            if 'Active:' in line:
                if '(running)' in line:
                    return True
        return False

    def start(self):
        """Usage:Used to start a service"""
        cmd = '/bin/systemctl start %s.service' % self.service
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        print proc
        proc.communicate()

if __name__ == '__main__':                                                 
    monitor = DaemonMonitor(sys.argv[1])
    if not monitor.is_active():
        monitor.start()
