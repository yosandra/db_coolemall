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

from marshaller import Marshaller


class XDRMarshaller(Marshaller):
    def __init__( self ): self._packer = xdrlib.Packer()
    def get_buffer( self ): return self._packer.get_buffer()
    def writeBoolean( self, decl, value ): self._packer.pack_bool( value )
    def writeFloat( self, decl, value ): self._packer.pack_float( value )
    def writeDouble( self, decl, value ): self._packer.pack_double( value )
    def writeInt32( self, decl, value ): self._packer.pack_int( value )
    def writeInt64( self, decl, value ): self._packer.pack_hyper( value )
    def writeMap( self, decl, value ): self._packer.pack_int( len( value ) ); value.marshal( self )
    def writeSequence( self, decl, value ): self._packer.pack_int( len( value ) ); value.marshal( self )    
    def writeString( self, decl, value ): self._packer.pack_string( value )
    def writeStruct( self, decl, value ): value.marshal( self )    
    def writeUint32( self, decl, value ): self._packer.pack_uint( value )
    def writeUint64( self, decl, value ): self._packer.pack_uhyper( value )
