#-*- coding: utf-8 -*-
import pydivert

def sniff():
    while(1):
        w = pydivert.WinDivert("tcp.DstPort == 80 and tcp.PayloadLength > 0")

        w.open()  # packets will be captured from now on

        packet = w.recv()  # read a single packet
        print(packet)
        w.send(packet)  # re-inject the packet into the network stack

        w.close()  # stop capturing packets