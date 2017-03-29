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


__all__ = ["Map"]


class Map(dict, MarshallableObject):
    # this is an example. it could as well be unimplemented here.
    @staticmethod
    def factory( **kwds ):
        return Map( **kwds )

    def getValue( self, key ):
        return self[key]
    
    def setValue( self, key, value ):
        self[key] = value

from factory import Factory
Factory.set_factory( "Map", Map.factory, __name__ )
