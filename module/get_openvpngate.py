from requests import get 
import csv
import base64
import os
import time

def download():
    try:
        print("Download VPN Starting")
        url = 'http://www.vpngate.net/api/iphone/'
        file_name = '/tmp/vpndata.csv'
        with open(file_name, "wb+") as file:
            response = get(url)
            file.write(response.content)
        print("Download Complete")
    except:
        print("Download Errer")
        log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
        log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'Download_VPN ERRER' + '\n')


