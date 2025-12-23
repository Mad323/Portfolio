from socket import *
import optparse
from threading import *

def connScan(tgtHost,tgtPort):
        try:
                sock=socket.(socket.AF_INET,SOCK_STREAM)
                sock.connect((tgtHost,tgtPort))
                print '%d/tcp Open' % tgtPort
        except:
                print ' %d/tcp Closed' % tgtPort
        finally:
                 sock.close()


def portScan(tgtHost,tgtPorts):
        try:
                tgtIP=gethostbyname(tgtHost)
        except:
                print 'Unkown host %s ' %tgtHost
        try:
                tgtName=gethostbyname(tgtIP)
                print 'Scan Results for: ' + tgtName[0]
        except:
                print 'Scan Results for: ' + tgtIP
        setdefaulttimeout(1)
        for tgtPort in tgtPorts:
                t=Thread(target=connScan, args=(tgtHost,int(tgtPort)))
                t.start()

def main():

        parser = optparse.OptionParser('Usage of program: ' + '-H <target> -p <target ports>')
        parser.add_option('-H',dest='tgtHost', type 'string',help='specify target host')
        parser.add_option('-p',dest='tgtPort', type 'string',help='specify target ports by comma')
        (options, args) =parser.parse_args()
        tgtHost=option.tgtHost
        tgtPorts=str(option.tgtPort).split(',')
        if (tgHost ==None) | (tgtPorts[0]==None):
                print parser.usage
                exit(0)
        portScan(tgtHost,tgtPorts)
if _name_=='_main_':

        main()
