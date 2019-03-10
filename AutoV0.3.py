import os
import random
import time
import requests
import shutil

from module.vpnconnect import vpnconnectIP
from module.get_openvpngate import row_vpndata
from module.seleniumpython import WebClicker

from module.useragentsRandom import useragentRandom
from module.useragentsRandom import desktopRandom
from module.useragentsRandom import mobileRandom
from module.useragentsRandom import otherRandom
from module.useragentsRandom import WindowsBrowsersRandom

from multiprocessing import Process

if __name__ == "__main__":
    os.system('sudo service openvpn stop')
    os.system('sudo ip link delete tun0')
    os.system('sudo killall openvpn')
    IPuser = requests.get('http://icanhazip.com').text.replace('\n','')
    while True:
            #try:
            os.system('sudo service openvpn start')
            listopenvpnDir = os.listdir(os.getcwd() + '/vpn/vpn_gate')
            listopenvpnName = []
            for listsa in listopenvpnDir:
                if listsa[0:2] == 'US':
                    listopenvpnName += [str(listsa)] * 30
                elif listsa[0:2] == 'UK':
                    listopenvpnName += [str(listsa)] * 30
                elif listsa[0:2] == 'UA':
                    listopenvpnName += [str(listsa)] * 30
                elif listsa[0:2] == 'CA':
                    listopenvpnName += [str(listsa)] * 30
                else:
                    listopenvpnName += [str(listsa)]
            listv = random.choice(listopenvpnName)
            dataconnect = vpnconnectIP(listv)
            if dataconnect == 'convpn':
                try:
                    md = os.listdir(r'/tmp')
                    for line in md:
                        try:
                            try:
                                os.remove("/tmp/{0}".format(line))
                            except:
                                shutil.rmtree("/tmp/{0}".format(line))
                        except:
                            pass
                except:
                    pass
                IPVPN = requests.get('http://icanhazip.com').text.replace('\n','')
                print('Good IP Connected ' + listv + ' IP ' + str(IPVPN))
                row_vpndata()
                print('screens size ' + str(screen[0]) + 'x' + str(screen[1]))
                Process(WebClicker(qq,screen))
                while IPuser == IPVPN:
                    time.sleep(5)
                    try:    
                        IPVPN = requests.get('http://icanhazip.com').text.replace('\n','')
                    except:
                        os.system('sudo ip link delete tun0')
                        IPVPN = requests.get('http://icanhazip.com').text.replace('\n','')
                os.system('pkill -f openvpn')
                os.system('pkill -f firefox')
                print('------------------------------------------------------')
            elif dataconnect == 'VPN NO Connect':
                log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
                log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'VPN NO Connect ' + str(listv) + '\n')
            elif dataconnect == 'lowe speed':
                log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
                log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'VPN lowe speed ' + str(listv) + '\n')
            elif dataconnect == 'Bade IP':
                IPVPN = requests.get('http://icanhazip.com').text.replace('\n','')
                print('Bade Connected ' + listv + ' IP ' + str(IPVPN))
                log = open(os.getcwd() + '/log/Errer_log/{0}.txt'.format(time.strftime("%d-%m-%Y")), 'a+')
                log.write(time.strftime("%d-%m-%Y %H:%M:%S") + ' ' + 'VPN Bade IP ' + str(listv) + ' IP ' + str(IPVPN) + '\n')
            elif dataconnect == 'VPN Not': 
                None
            elif dataconnect == 'errer openvpnstart':
                print('errer openvpnstart')
            else:
                None
            
      
