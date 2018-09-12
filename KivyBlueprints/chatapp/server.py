from twisted.internet import protocol, reactor

transports = set()


class Chat(protocol.Protocol):
    def dataReceived(self, data):
        transports.add(self.transport)

        if ':'.encode() not in data:
            return

        user, msg = data.split(':'.encode(), 1)

        for t in transports:
            if t is not self.transport:
                t.write(('{0} says: {1}'.format(user, msg)).encode())


class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat()


reactor.listenTCP(9096, ChatFactory())
reactor.run()