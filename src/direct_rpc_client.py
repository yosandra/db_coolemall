import socket
from types import *


# Constants
# TODO: this is the same number as in DirectRPCServer
SERVER_PORT = 9450

    
def directRPCClient( message, ip="localhost", port=SERVER_PORT ):
    # this doesn't actually belong here, but it's handy to have it... [EF]
    message = message + "\n"
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    sock.connect( (ip, port) )
    sock.send( message )
    response = ""
    # caveat: data must fit into memory!
    while True:
        data = sock.recv( 1024 )
        if not data:
            break
        response = response + data
    sock.close()
    #print("Received: %s" % response)

    from types.factory import Factory
    for imp in Factory.import_all():
        try:
            exec imp
        except Exception, e:
            print "exec failed", imp, e

    try:
        output = eval( response )
    except Exception, e:
        print "Exception when evaluating response to direct rpc:", e
        return None
    return output

if __name__ == "__main__":
    import sys
    if len( sys.argv ) > 2:
        ip = sys.argv[1]
        port = SERVER_PORT
        if ":" in ip:
            ip, port = ip.split(":")
        message = " ".join( sys.argv[2:] )
        print directRPCClient( message, ip=ip, port=int( port ) )

