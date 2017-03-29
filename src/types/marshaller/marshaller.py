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

from timacs.types import Map, Sequence, Struct


class Marshaller(object):
    def write( self, key, value ):
        if isinstance( value, basestring ):
            self.writeString( key, value )
        elif isinstance( value, float ):
            self.writeDouble( key, value )
        elif isinstance( value, int ):
            self.writeInt32( key, value )
        elif isinstance( value, long ):
            self.writeInt64( key, value )
        elif isinstance( value, dict ):
            self.writeMap( key, value )           
        elif isinstance( value, list ):
            self.writeSequence( key, value )
        #elif isinstance( value, Struct ):
        #    self.writeStruct( key, value )
        else:
            raise NotImplementedError, key + " : " + str( type( value ) ) 
    
    def writeBoolean( self, key, value ): raise NotImplementedError
    def writeFloat( self, key, value ): self.writeDouble( key, value )
    def writeDouble( self, key, value ): raise NotImplementedError
    def writeInt8( self, key, value ): self.writeInt16( key, value )
    def writeInt16( self, key, value ): self.writeInt32( key, value )
    def writeInt32( self, key, value ): self.writeInt64( key, value )
    def writeInt64( self, key, value ): raise NotImplementedError
    def writeMap( self, key, value ): raise NotImplementedError
    def writeSimpleMap( self, key, value ): raise NotImplementedError
    def writeSequence( self, key, value ): raise NotImplementedError
    def writeSimpleSequence( self, key, value ): raise NotImplementedError
    def writeString( self, key, value ): raise NotImplementedError
    def writeStruct( self, key, value ): raise NotImplementedError
    def writeUint8( self, key, value ): self.writeInt8( key, value )
    def writeUint16( self, key, value ): self.writeInt16( key, value )
    def writeUint32( self, key, value ): self.writeInt32( key, value )
    def writeUint64( self, key, value ): self.writeInt64( key, value )
