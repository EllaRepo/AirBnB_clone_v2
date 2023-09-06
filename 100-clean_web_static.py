#!/usr/bin/python3
""" This module defines a function that that deletes out-of-date archives
"""
from fabric.api import *


env.hosts = ['35.174.207.25', '54.144.140.227']
env.user = "ubuntu"


def do_clean(number=0):
    """ Function that deletes out-of-date archives
    """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
