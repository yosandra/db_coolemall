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
# Derived from metric.py
# Copyright (c) NEC Deutschland GmbH, NEC HPC Europe
# Copyright (c) ZIH, Technische Universitaet Dresden

from key_value_object import KeyValueObject


__all__ = [ "Command" ]


class Command(KeyValueObject):
    def __init__( self, command=None, target=None, **kwds ):
        KeyValueObject.__init__( self, command=command, target=target, **kwds )
        for key in ( "command", "target"):
            assert hasattr( self, key ), "'%s' required in Command" % key

    @staticmethod
    def factory( **kwds ):
        return Command( command="dummy", target="dummy", **kwds )





from factory import Factory
Factory.set_factory( "Command", Command.factory, __name__ )
