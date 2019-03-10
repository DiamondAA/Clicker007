import requests
import json
import time
import os

def jsonfrom():
    try:
        ip = requests.get('http://icanhazip.com')
        iphub = requests.get('https://iphub.info/api/ip/{0}'.format((ip.text).replace('\n', '')))
        jsoniphub = json.loads(iphub.text)
        return(jsoniphub)
    except:
        log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
        log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'ipcheck_jsonfrom ERRER' + '\n')

def countryName():
    try:
        return(str(jsonfrom()['countryName']))
    except:
        log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
        log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'ipcheck_countryName ERRER' + '\n')


def ipType():
    try:
        return(str(jsonfrom()['block']))
    except:
        log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
        log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'ipcheck_ipType ERRER' + '\n')


