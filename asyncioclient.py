import asyncio
import os

class EchoClient(asyncio.Protocol):
    """docstring for EchoClient"""
    def __init__(self, message, loop):
        super(EchoClient, self).__init__()
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print("Data sended {!r},{!r}".format(self.message, "test"))

    def data_received(self, data):
        print("Data received {!r}".format(data.decode()))

    def connection_lost(self, exc):
        print("the server close the connection")
        self.loop.stop()

loop = asyncio.get_event_loop()
message = "hello world!"
client = loop.create_connection(lambda: EchoClient(message, loop), '127.0.0.1', 8888)
loop.run_until_complete(client)
loop.run_forever()
loop.close()
