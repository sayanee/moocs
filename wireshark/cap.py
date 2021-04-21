import pyshark
capture = pyshark.LiveCapture(interface='lo0')
for packet in capture.sniff_continuously(packet_count=50):
    myfile = open('pyshark1.txt','w')
    myfile.write(str(packet))
    try:
        print('Source = ' + packet['ip'].src)
        print('Destination = ' + packet['ip'].dst)
    except:
        pass
print ('The end')
exit()
