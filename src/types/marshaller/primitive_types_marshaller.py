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

from marshaller import Marshaller


class PrimitiveTypesMarshaller(Marshaller):   
    def __init__( self, out_pt ):
        Marshaller.__init__( self )
        self._out_pt = out_pt       

    def writeBoolean( self, key, value ):
        if isinstance( self._out_pt, dict ):
            self._out_pt[key] = value
        elif isinstance( self._out_pt, list ):
            self._out_pt.append( value )
        else:
            raise TypeError

    writeDouble = writeInt64 = writeString = writeBoolean
                
    def writeMap( self, key, value ):
        if value is not None: 
            out_pt = dict()
            value.marshal( PrimitiveTypesMarshaller( out_pt ) )
            if isinstance( self._out_pt, dict ):
                self._out_pt[key] = out_pt
            elif isinstance( self._out_pt, list ):
                self._out_pt.append( out_pt )
            else:
                raise TypeError
                
    def writeSequence( self, key, value ):
        if value is not None: 
            out_pt = list()
            value.marshal( PrimitiveTypesMarshaller( out_pt ) )
            if isinstance( self._out_pt, dict ):
                self._out_pt[key] = out_pt
            elif isinstance( self._out_pt, list ):
                self._out_pt.append( out_pt )
            else:
                raise TypeError
                    
    def writeStruct( self, key, value ): 
        self.writeMap( key, value )
