import urllib.request
from bs4 import BeautifulSoup
import ssl


handler = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_594720.html').read()
soup = BeautifulSoup(handler, 'html.parser')

# Ignore SSL certificate errors
ctx = ssl.create_default_context() 
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

tags = soup('span')
count = 0
for tag in tags:
    count = count + int(tag.contents[0])

print(count)

#OUTPUT
#2561



#SSL is a standard security technology for establishing an encrypted link between a server and a client—typically a web server (website) and a browser
#browser and the server need what is called an SSL Certificate to be able to establish a secure connection.
#context (CTX) structure is needed for each application that is running SSL
#the process that creates an SSL session is the only process that can issue the SSL API functions for that SSL session

#create_default_context() returns a new context with secure default settings.
#   |->support for server name indication (SNI) and hostname matching.

#SSLContext.verify_mode
#   |->Whether to try to verify other peers’ certificates and how to behave if verification fails. 
#   |->This attribute must be one of CERT_NONE, CERT_OPTIONAL or CERT_REQUIRED.
#   |->Enabling hostname checking automatically sets verify_mode from CERT_NONE to CERT_REQUIRED

#SSLContext.check_hostname
#   |->Whether to match the peer cert’s hostname with match_hostname() in SSLSocket.do_handshake().
#   |->check_hostname must be enabled as well to verify the authenticity of a cert