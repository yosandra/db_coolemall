#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the version 3 of the GNU Lesser General Public License
#   as published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Copyright (c) NEC Deutschland GmbH, NEC HPC Europe

import logging
import re
import socket
import threading
import socketserver

__all__ = ["DIRECT_RPC_DEFAULT_PORT"]

#Constants
DIRECT_RPC_PORT_DEFAULT = 9450
# precompiled regexp pattern
NAMED_ARGS_RE = re.compile('([^ =]+) *= *("[^"]*"|[^ ]*)')
SIMPLE_ARGS_RE = re.compile('("[^"]*"|\'[^\']*\'|[^ ]+|[^ =])')


def parse_command_line( line ):
    """
    Parse a command line and return command, args and kwds.
    """
    kwds = {}
    nline = ""
    indx = 0
    for m in NAMED_ARGS_RE.finditer(line):
        start = m.start()
        end = m.end()
        if start > indx:
            nline = nline + line[indx:start]
            indx = end + 1
        k = m.group(1)
        v = m.group(2)
        if v[:1]=='"':
            kwds[k]= v[1:-1]
        elif v[:1]=="'":
            kwds[k]= v[1:-1]
        else:
            kwds[k]= v
    nline = nline + line[indx:]

    args = []
    for v in SIMPLE_ARGS_RE.findall(nline):
        if v[:1]=='"':
            args.append( v[1:-1] )
        elif v[:1]=="'":
            args.append( v[1:-1] )
        else:
            args.append( v )

    return args[0], args[1:], kwds


class TCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # --- file like interface ---
        # self.rfile is a file-like object created by the handler;
        self.command = self.rfile.readline().strip()
        logging.info( "DirectRPC received from %s: %s" % (self.client_address[0], self.command) )
        cmd, args, kwds = parse_command_line( self.command )
        logging.info( "DirectRPC cmd=%s args=%s kwds=%s" % (cmd, repr(args), repr(kwds)) )

        # execute RPC
        funcs = DirectRPCServer.functions
        if funcs.has_key( cmd ):
            func = funcs[cmd]
            try:
                logging.debug( "DirectRPC calling function: %s" % cmd)
                result = func( *args, **kwds )
                logging.debug( "DirectRPC result=%s" % repr( result ) )
            except Exception, e:
                logging.error( "DirectRPC calling function '%s' failed" % cmd)
                logging.error( e )
                # TODO: send back an exception [EF]
                self.wfile.write( repr( Exception ) )
            else:
                self.wfile.write( repr( result ) )
        else:
            logging.error( "DirectRPC: command '%s' not found." % cmd )
            # TODO: send back an exception [EF]
            self.wfile.write( repr( Exception ) )


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class DirectRPCServer():
    functions = {}
    port = 0

    def __init__( self, port=DIRECT_RPC_PORT_DEFAULT ):
        logging.info( "Direct RPC Server starting..." )
        if DirectRPCServer.port != 0:
            logging.error( "Direct RPC Server is already running on port %d, cannot start another instance!" % DirectRPCServer.port )
            raise BaseException
        
        self.server = ThreadedTCPServer( ("0.0.0.0", port), TCPRequestHandler )
        self.ip, self.port = self.server.server_address
        DirectRPCServer.port = self.port

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        self.server_thread = threading.Thread( target=self.server.serve_forever, name="DirectRPC" )
        # Exit the server thread when the main thread terminates
        self.server_thread.setDaemon(True)
        self.server_thread.start()
        logging.info( "Direct RPC Server loop running on port: %d" % self.port )
        # self.server.shutdown()

    @staticmethod
    def client( message, ip="localhost" ):
        # this doesn't actually belong here, but it's handy to have it... [EF]
        message = message + "\n"
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        assert DirectRPCServer.port > 0, "DirectRPCServer port is unset!"
        sock.connect( (ip, DirectRPCServer.port) )
        sock.send( message )
        response = ""
        # caveat: data must fit into memory!
        while True:
            data = sock.recv( 1024 )
            if not data:
                break
            response = response + data
        sock.close()
        logging.debug( "DirectRPC client received response: %s" % response )

        from types.factory import Factory
        for imp in Factory.import_all():
            try:
                exec imp
            except Exception, e:
                logging.error( "DirectRPC exec import failed: %s" % imp)
                logging.error( e )

        try:
            output = eval( response )
        except Exception, e:
            logging.error( "Exception when evaluating response to direct rpc" )
            logging.error( e )
            return None
        return output

    @staticmethod
    def register_rpc( name, function ):
        if DirectRPCServer.functions.has_key( name ):
            print "WARNING: Reregistering of DirectRPC Call '%s' attempted!" % name
            return
        DirectRPCServer.functions[name] = function


def list_functions( verbose=False ):
    funcs = DirectRPCServer.functions.keys()
    funcs.sort()
    if verbose:
        out = []
        for f in funcs:
            function = DirectRPCServer.functions[f]
            out.append( (f, dir( function )) )
        return out
    else:
        return funcs

DirectRPCServer.register_rpc( "list_functions", list_functions )
