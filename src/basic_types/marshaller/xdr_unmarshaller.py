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

import xdrlib

from unmarshaller import Unmarshaller


class XDRUnmarshaller(Unmarshaller):
    def __init__( self, buff ):
        self._unpacker = xdrlib.Unpacker( buff )
        self.__buflen = len( buff )

    def get_position( self ):
        "Return -1 if at end-of-file"
        __pos = self._unpacker.get_position()
        if __pos >= self.__buflen:
            return -1
        return __pos

    def readBoolean( self, decl ):
        return self._unpacker.unpack_bool()

    def readFloat( self, decl ):
        return self._unpacker.unpack_float()

    def readDouble( self, decl ):
        return self._unpacker.unpack_double()

    def readInt32( self, decl ):
        return self._unpacker.unpack_int()

    def readInt64( self, decl ):
        return self._unpacker.unpack_hyper()
    
    def readMap( self, decl, value ):
        size = self._unpacker.unpack_int();
        for __i in xrange( size ):
            value.unmarshal( self )
    
    def readSequence( self, decl, value ): 
        size = self._unpacker.unpack_int();
        for __i in xrange( size ):
            value.unmarshal( self )
            
    def readString( self, decl ):
        return self._unpacker.unpack_fstring( self._unpacker.unpack_uint()  )

    def readStruct( self, decl, value ):
        value.unmarshal( self ) 

    def readUint32( self, decl ):
        return self._unpacker.unpack_uint()

    def readUint64( self, decl ):
        return self._unpacker.unpack_uhyper()
