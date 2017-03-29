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

class Unmarshaller(object):
    def get_position( self ): raise NotImplementedError
    def readBoolean( self, decl ): raise NotImplementedError
    def readFloat( self, decl ): return self.readDouble( decl )
    def readDouble( self, decl ): raise NotImplementedError
    def readInt8( self, decl ): return self.readInt16( decl )
    def readInt16( self, decl ): return self.readInt32( decl )
    def readInt32( self, decl ): return self.readInt64( decl )
    def readInt64( self, decl ): raise NotImplementedError
    def readMap( self, decl ): raise NotImplementedError
    def readSequence( self, decl ): raise NotImplementedError
    def readString( self, decl ): raise NotImplementedError
    def readStruct( self, decl ): raise NotImplementedError
    def readUint8( self, decl ): return self.readInt8( decl )
    def readUint16( self, decl ): return self.readInt16( decl )
    def readUint32( self, decl ): return self.readInt32( decl )
    def readUint64( self, decl ): return self.readInt64( decl )    
    def readKeysOrNone(self): raise NotImplementedError
    def readNextObj(self): raise NotImplementedError
    def readObj(self, key): raise NotImplementedError