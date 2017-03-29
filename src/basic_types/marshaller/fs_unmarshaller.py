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
#
# $Id: fs_unmarshaller.py 104 2011-09-06 16:09:19Z efocht $

import os.path, sys
import logging

from unmarshaller import Unmarshaller
from basic_types.factory import Factory


__all__ = ["FSUnmarshaller"]


class FSUnmarshaller(Unmarshaller):

    def __init__( self, base_dir_path, depth=sys.maxint ): 
        self._base_dir_path = base_dir_path
        self._depth = depth

    ## Read contents of base directory excluding RRD file.
    # @return: a sorted list containing all object keys (attributes)
    def readKeysOrNone( self ):
        keys = os.listdir( self._base_dir_path )
        keys = [key for key in keys if (not key.endswith( ".rrd" )
                                        and not key.endswith( ".rra" )
                                        and not key.endswith( ".rry" )
                                        and not key.endswith( ".log" )
                                        and not key.endswith( ".int" )
                                        and not key.startswith( "." ) 
                                        and not key.startswith( "__" ) ) ]
        keys.sort()
        return keys

    ## Ascend one level.
    def readMap( self, key, value ):
        if self._depth > 0:
            child_base_dir_path = os.path.join( self._base_dir_path, key )
            if os.path.exists( child_base_dir_path ):
                value.unmarshal( FSUnmarshaller( child_base_dir_path, self._depth - 1 ) )
                return value
            else:
                raise ValueError, "Path to serialized map not found: %s" % child_base_dir_path      

    readStruct = readMap
    readSequence = readMap

    ## Read object of unknown type and evaluate it (repr <--> eval).
    # @return: object of right type
    def readObj( self, key ):
        child_base_dir_path = os.path.join( self._base_dir_path, key )
        if os.path.exists( child_base_dir_path ):
            # TODO: improve error handling: no file, corrupt file, wrong content should be all addressed
            try:
                value_string = open( os.path.join( child_base_dir_path ) ).read()
            except IOError as e:
                raise ValueError, "readObj %s IOError: %s" % (child_base_dir_path, e)
            try:
                obj = eval( value_string )
                return obj
            except:
                error = "fs_unmarshaller.readObj(): ignoring value for key '%s'" % key
                logging.error( error )
                raise ValueError, error
        raise ValueError, "Path to serialized object not found: %s" % child_base_dir_path

    readBoolean = readDouble = readFloat = readInt32 = readInt64 = readString = readObj
    
    def readObjType( self, key ):
        child_base_dir_path = os.path.join( self._base_dir_path, key )
        if os.path.isfile( child_base_dir_path ):
            return "simple"
        elif os.path.isdir( child_base_dir_path ):
            class_file = os.path.join( child_base_dir_path, "__class__" )
            if os.path.exists( class_file ):
                return open( class_file ).read()
        else:
            raise TypeError, "Could not identify serialized object type for %s" % child_base_dir_path

    def readSubElementsAsMap( self ):
        """
        SubElements are things that were stored without a key! They are not recognized as keys in readKeyesOrNone().
        For a FS marshaller subelements are subdirectories with names starting with '__'.
        """
        result = []
        keys = os.listdir( self._base_dir_path )
        dirs = [key for key in keys if key.startswith( "__" ) ]
        for dir in dirs:
            child_path = os.path.join( self._base_dir_path, dir )
            if not os.path.isdir( child_path ):
                continue
            class_file = os.path.join( child_path, "__class__" )
            if not os.path.exists( class_file ):
                continue
            element_type = open( class_file ).read()

            if Factory.can_build( element_type ):
                val = Factory.build( element_type )
            else:
                print "FS unmarshaller: don't know how to build element type '%s'" % element_type
                continue
            val.unmarshal( FSUnmarshaller( child_path ) )
            result.append( val )
        return result
