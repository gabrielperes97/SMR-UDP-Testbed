#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.util import pmonitor

import time

from sys import argv


class SddlTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        """
        delay
        gsm - GSM/CSD (min 150, max 550).
        hscsd - HSCSD (min 80, max 400).
        gprs - GPRS (min 35, max 200).
        edge - EDGE/EGPRS (min 80, max 400).
        umts - UMTS/3G (min 35, max 200).
        hsdpa - HSDPA (min 0, max 0).
        lte - LTE (min 0, max 0).
        evdo - EVDO (min 0, max 0).
        none - No latency, the default (min 0, max 0). 
        """
        """
        netspeed
        gsm - GSM/CSD (up: 14.4, down: 14.4).
        hscsd - HSCSD (up: 14.4, down: 57.6).
        gprs - GPRS (up: 28.8, down: 57.6).
        edge - EDGE/EGPRS (up: 473.6, down: 473.6).
        umts - UMTS/3G (up: 384.0, down: 384.0).
        hsdpa - HSDPA (up: 5760.0, down: 13,980.0).
        lte - LTE (up: 58,000, down: 173,000).
        evdo - EVDO (up: 75,000, down: 280,000).
        full - No limit, the default (up: 0.0, down: 0.0). 
        """

        self.g_config = {'bw': 384, 'delay': 117 }

        # Server's links are really fast.
        self.server_config = {'bw': 100, 'delay': '0.1ms'}
        
        #MobileHub
        mh = self.addHost('mh')
        #gateway
        gw = self.addHost('gw')

        #Torre da operadora
        vivo = self.addSwitch('sw1')
        #links
        self.addLink(mh, vivo, **self.g_config) #3g
        
        self.addLink(vivo, gw, **self.server_config) #uma rede toda por tras

topos = { 'sddltopo': ( lambda: SddlTopo() ) }

def run(tx, packlen, pinglen, logname, security):
    if (security):
        sec = "-s "
    else:
        sec = ""


    topo = SddlTopo()
    net = Mininet(topo=topo, link=TCLink)
    net.start()
    print("Starting...")
    net.hosts[0].cmd("java -jar SddlSecTests.jar -G "+ sec +" &")
    net.hosts[0].cmd("java -jar SddlSecTests.jar -S -tx " + tx + " -l " + packlen + " -pl "+ pinglen + " -o " + logname +" &")
    time.sleep(5)
    net.hosts[1].cmdPrint("java -jar SddlSecTests.jar -C "+ sec +"-h 10.0.0.1")
    #CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    if (len(argv) == 1):
        run("1", "1024", "50000", "log.csv", False)
    if argv[5] == "true":
        sec = True
    else:
        sec = False
    run(argv[1], argv[2], argv[3], argv[4], sec)

        

