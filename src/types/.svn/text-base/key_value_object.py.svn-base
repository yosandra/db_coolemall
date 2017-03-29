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

from helpers import *
from struct import *
from sequence import *
from marshallable import *


__all__ = ["KeyValueObject"]


class KeyValueObject(MarshallableObject):
    '''
    Generic object that contains and can be initialized with key-value pairs.
    The values can be primitive types, lists or dicts. Values can not be
    self defined objects.
    Marshalling and unmarshalling is done with the knowledge gained from introspection.
    ''' 
    def __init__( self, **kwds ):
        for key, val in kwds.items():
            #print "KeyValueObject: %s -> %s" % (key, str(val))
            self.setValue( key, val )

    def __len__( self ):
        return len( self.__dict__.keys() )

    def clear(self):
        self.__dict__.clear()

    # this is an example. it could as well be unimplemented here.
    @staticmethod
    def factory( **kwds ):
        return KeyValueObject( **kwds )

    def getValue( self, key ):
        return self.__dict__[key]

    def keys(self):
        return self.__dict__.keys()
    
    def setValue( self, key, value ):
        self.__dict__[key] = value
