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


import os.path

from marshaller import Marshaller


class FSMarshaller(Marshaller):

    ## Creates directory path.
    # base_dir_path: directory path to be created
    def __init__( self, base_dir_path ):
        Marshaller.__init__( self )
        try:
            os.makedirs( base_dir_path )
        except:
            pass
        self._base_dir_path = base_dir_path

    ## Writes value in a file named key. If there is no value it removes the file.
    def _writeRepr( self, key, value ):
        file_path = os.path.join( self._base_dir_path, key )
        if len( value ) > 0: 
            open( file_path, "w+" ).write( value )
        else:
            try:
                os.unlink( file_path )
            except:
                pass

    ## Writes key - value pair to database.
    def writeObj( self, key, value ):
        self._writeRepr( key, repr( value ) )

    writeDouble =  writeInt64 = writeString = writeBoolean = writeObj

    def writeSequence( self, key, value ):
        if value is not None:
            value.marshal( FSMarshaller( os.path.join( self._base_dir_path, key ) ) )

    ## Descend one step
    def writeMap( self, key, value ):
        if value is not None:
            sub_element_marshaller = FSMarshaller( os.path.join( self._base_dir_path, key ) )
            value.marshal( sub_element_marshaller )
            sub_element_marshaller._writeRepr( "__class__", value.__class__.__name__.split()[-1] )

    writeStruct = writeMap
    writeSequence = writeMap
