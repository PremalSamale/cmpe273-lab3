from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ConnectedServer(DatagramProtocol):

    def datagramReceived(self, datagram, address):
        print("Datagram %s received" % (repr(datagram)))
        self.transport.write(b'Server: Hello World',address)

reactor.listenUDP(5000, ConnectedServer())
reactor.run()
