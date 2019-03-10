import os
import random
import requests
import time
import subprocess
from multiprocessing import Process

from module.ipcheck import ipType

def check_vpn(vpnname):
    logvpn = os.listdir('./vpn/log')
    logbadevpn = os.listdir('./vpn/log_Bade_IP')
    for log in logvpn:
        if vpnname == log:
            return 'logconnect'
    for log in logbadevpn:
        if vpnname == log:
            return 'logconnect'

def openvpnstart(vpnname):
    try:
        os.system('sudo ip link delete tun0')
        os.system('sudo service openvpn restart')
        os.system('sudo killall openvpn')
        IPuser = requests.get('http://icanhazip.com')
        print('connecting ' + vpnname)
        x = subprocess.Popen(['openvpn','--auth-nocache','--config','{0}/vpn/vpn_gate/{1}'.format(os.getcwd(),vpnname)], shell=False ,stdout=subprocess.PIPE)
        time.sleep(30)
        IPcheckVPN = requests.get('http://icanhazip.com')
        if IPuser.text == IPcheckVPN.text:
            x.kill
            os.system('pkill -f openvpn')
            os.system('sudo killall openvpn')
            return 'VPN NO Connect'
        elif ipType() == '0':
            #print('Good IP')
            a = open("./vpn/log/{0}".format(vpnname), "wb")
            a.write(bytes(IPcheckVPN.text.replace('\n',''), 'utf-8'))
            a.close
            return 'convpn'
        else:
            #print('Bade IP')
            a = open("./vpn/log_Bade_IP/{0}".format(vpnname), "wb")
            a.close
            return 'Bade IP'
    except:
        return 'errer openvpnstart'

def vpnconnectIP(vpnname):
    #os.system('taskkill /f /im openvpn-gui.exe')
    #os.system('taskkill /f /im openvpn.exe')
    try:
        check = check_vpn(vpnname)
        if check == 'logconnect':
            return 'logconnect'
        else:
            return openvpnstart(vpnname)
    except:
        log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
        log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'VPNvpnconect ERRER' + '\n')
