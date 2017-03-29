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
# $Id$

__all__ = ["NumRecord"]


class NumRecord(object):
    """
    Numeric record object definition. A record contains:
        - the measurement time in nanoseconds
        - the measured value (a integer, long or float)
    """
    def __init__( self, time_ns=0, value=0 ):
        self.time_ns = time_ns
        self.value = value

    def __repr__(self):
        # There seems to be no way to get the outer class name (RRD), thus it is hard coded.
        return "%s(%s, %s)" % ( self.__class__.__name__, repr( self.time_ns ), repr( self.value ) )

    def marshal( self, marshaller ):
        marshaller.writeUint64( "time_ns", long(self.time_ns) )
        marshaller.writeDouble( "value", self.value )

    def unmarshal( self, unmarshaller ):
        self.time_ns = unmarshaller.readUint64( "time_ns" )
        self.value = unmarshaller.readDouble( "value" )


from timacs.types.factory import Factory
Factory.set_factory( "NumRecord", NumRecord, __name__ )
