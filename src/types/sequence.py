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

from timacs.types.helpers import is_simple_sequence


class Sequence(list):
    def marshal( self, marshaller ):
        if is_simple_sequence( self ):
            marshaller.writeSimpleSequence( self )
        else:
            for i in xrange( len( self ) ):
                marshaller.write( "i_%d" % i, self[i] )

    def unmarshal( self, unmarshaller ):
        keys = unmarshaller.readKeysOrNone() 
        for key in keys:
            index = int( key.lstrip( "i_" ) )
            self.insert(index, unmarshaller.readObj( key ) )
        #raise NotImplementedError

    def __str__( self ):
        from cStringIO import StringIO
        from timacs.types.marshaller.pretty_printer import PrettyPrinter
        out_string_io = StringIO()
        self.marshal( PrettyPrinter( out_string_io ) )
        return out_string_io.getvalue()

    def __repr__( self ):
        # Note: Sequence is a Python list (repr is "[a, ...]")
        rep = "[" + ", ".join( repr( element ) for element in self ) + "]"
        # TODO: Sequence should have __init__ to reconstruct an object via eval()
        return rep
