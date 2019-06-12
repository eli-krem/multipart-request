import socket
import random
import mimetypes

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8888
url = '/test/upload.php'
s.connect((host, port))
filename = "F5_Networks_logo.svg.png"
f = open(filename, 'rb')
data = f.read()

mimetype = mimetypes.MimeTypes().guess_type(filename)[0]
rand = random.randint(10000000000000,20000000000000)
boundary = 'aaaa' + str(rand)

request_body_start = '--' + boundary + '\r\nContent-Disposition: form-data; name="filename"; filename=' + filename + '\r\nContent-Type: ' + mimetype + '\r\n\r\n'

request_body_end = '\r\n' + '--' + boundary + '--\r\n\r\n'

headers = {"host": host + ':' + str(port), "Connection": "keep-alive", "Content-Length": len(request_body_start + str(data) + request_body_end), "Content-Type": "multipart/form-data; boundary="}

request_header = 'POST ' + url + ' HTTP/1.1\r\nHost: ' + headers["host"] + '\r\nConnection: ' + headers["Connection"] + '\r\nContent-Length: ' + str(headers["Content-Length"]) + '\r\nContent-Type: '+ headers["Content-Type"] + boundary + '\r\n\r\n'


s.send(request_header.encode('utf-8')) #send headers
s.send(request_body_start.encode('utf-8')) #send multipart 
s.send(data) #send data
s.send(request_body_end.encode('utf-8')) #send end multipart

s.close()