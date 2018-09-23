from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("224.3.29.71")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        self.transport.write(b'Client:Hello World', (('224.3.29.71'), 10000))

    def datagramReceived(self, datagram, address):
        print('Datagram %s received from %s' % (repr(datagram), repr(address)))


reactor.listenMulticast(10000, MulticastClient(), listenMultiple=True)
reactor.run()