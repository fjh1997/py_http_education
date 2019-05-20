import socket
import sys
import gzip
import ssl


message_get = '''GET / HTTP/1.1
Host: www.yvsou.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7

'''

def readrequest(s):
    buffer = ''.encode()
    data = 1
    n=0
    try:
        while data:
            data = s.recv(4096)
            buffer += data

    except Exception as e:
        print (e)
            
    finally:
        return buffer

#Send GET request
try:
    # Create a socket
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port 9999 on localhost
    sock = context.wrap_socket(s, server_hostname='www.yvsou.com')
    server_address = ('www.yvsou.com', 443)
    print ('Connecting to www.yvsou.com on port 443')
    sock.connect(server_address)

    print ('sending %s' % message_get)
    sock.sendall(message_get.encode())
    # Receive data
    data = readrequest(sock)
    [head,body]=data.split(b'\r\n\r\n')
    print (head)
    print (gzip.decompress(body))
    


except Exception as e:
    print (e)

finally:
    # Closing the connection
    sock.close()




