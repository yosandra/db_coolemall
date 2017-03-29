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

import sys

from marshaller import Marshaller


class PrettyPrinter(Marshaller):   
    def __init__( self, print_to_file=None ):
        if print_to_file is not None:
            self.__print_to_file = print_to_file
        else:
            self.__print_to_file = sys.stdout

    def writeBoolean( self, key, value ): self.writeString( key, str( value ) )         
    def writeDouble( self, key, value ): self.writeString( key, str( value ) )
    def writeInt64( self, key, value ): self.writeString( key, str( value ) )
    
    def _writeKey( self, key ):
        print >>self.__print_to_file, key + " =",
        
    def writeMap( self, key, value ):
        self._writeKey( key )
        print >>self.__print_to_file, "{ "
        if value is not None:
            value.marshal( self )
        print >>self.__print_to_file, " }"
    
    def writeSequence( self, key, value ):
        self._writeKey( key )
        print >>self.__print_to_file, "[ "
        if value is not None:
            value.marshal( self )
        print >>self.__print_to_file, " ]"        
                
    def writeString( self, key, value ):
        self._writeKey( key )
        print >>self.__print_to_file, value 
        
    def writeStruct( self, key, value ):
        self.writeMap( key, value )
