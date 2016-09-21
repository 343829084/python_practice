import asyncio

@asyncio.coroutine
def wget(addr):
    print("wget web:",addr)
    connect = asyncio.open_connection(addr, 80)
    reader, writer = yield from connect
    request = 'GET / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n' % addr
    writer.write(request.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (addr, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()