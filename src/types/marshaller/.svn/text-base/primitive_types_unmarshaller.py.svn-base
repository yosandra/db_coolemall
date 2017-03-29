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

from copy import copy

from unmarshaller import Unmarshaller


class PrimitiveTypesUnmarshaller(Unmarshaller):
    def __init__( self, in_pt ):
        if isinstance( in_pt, list ):
            self.in_pt = copy( in_pt )
        elif isinstance( in_pt, dict ):            
            self.in_pt = in_pt
        else:
            raise TypeError, "input primitive type must be list or dict, not " + in_pt.__class__.__name__

    def readBoolean( self, key ):
        return bool( self.__readX( key ) )

    def readDouble( self, key ):
        return float( self.__readX( key ) )

    def readInt64( self, key ):
        value = self.__readX( key )
        if type( value ) == long and int( value ) == long( value ):
            return int( value )
        else:
            return value

    def readMap( self, key, value ):
        if value is not None:
            value.unmarshal( PrimitiveTypesUnmarshaller( self.__readX( key ) ) )
            
    def readObjType( self, key ):
        "PrimitiveTypeMarshaller only knows about simple objects"
        return "simple"
         
    def readSequence( self, key, value ):
        if value is not None:
            value.unmarshal( PrimitiveTypesUnmarshaller( self.__readX( key ) ) ) 

    def readString( self, key ):
        return self.__readX( key )
        
    def readStruct( self, key, value ):
        if value is not None:             
            value.unmarshal( PrimitiveTypesUnmarshaller( self.__readX( key ) ) ) 
    
    def __readX( self, key ):
        if isinstance( self.in_pt, list ):
            return self.in_pt.pop( 0 )
        else:
            return self.in_pt[key]        
        
    def readKeysOrNone(self):
        if isinstance( self.in_pt, list ):
            return None
        else:
            return self.in_pt.keys()    

    def readObj(self, key):
        if isinstance( self.in_pt, dict ):
            return self.in_pt[key]        
        else:
            raise TypeError, "key reads are for dict objects only"
        
        
    def readNextObj(self):
        if isinstance( self.in_pt, list):
            return self.in_pt.pop( 0 )
        else:
            raise TypeError, "sequential reads are for list objects only"
