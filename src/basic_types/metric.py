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

from key_value_object import KeyValueObject
from map import *
from struct import *
from sequence import *


__all__ = [ "Metric" ]


class Metric(KeyValueObject):
    def __init__( self, name=None, source=None, **kwds ):
        KeyValueObject.__init__( self, name=name, source=source, **kwds )
        for key in ( "name", "source", "time", "value" ):
            assert hasattr( self, key ), "'%s' required in Metric" % key

    @staticmethod
    def factory( **kwds ):
        return Metric( name="dummy", source="dummy", time=0, value=None, **kwds )


class MetricSet(Sequence):
    def marshal( self, marshaller ):
        for i in xrange( len( self ) ):
            marshaller.writeStruct( str( i ), self[i] )

    def unmarshal( self, unmarshaller ):
        for i in xrange( len( self ) ):
            self[i] = Metric(); unmarshaller.readStruct( str( i ), self[i] )


from factory import Factory
Factory.set_factory( "Metric", Metric.factory, __name__ )
