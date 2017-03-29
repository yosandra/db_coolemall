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

from inspect import isclass, isfunction, ismethod


class Factory():
    """
    Factory for empty objects. Needed when deserializing objects.
    """
    __factories = {}
    @staticmethod
    def set_factory( obj_type, function, package ):
        assert obj_type is not None and function is not None, "wrong arguments"
        Factory.__factories[obj_type] = (function, package)
    
    @staticmethod
    def build( obj_type, *args, **kwds ):
        "It should be possible to build a fresh object when passing no arguments at all."
        assert Factory.__factories.has_key(obj_type), "%s factory method is not available" % obj_type
        f,pkg = Factory.__factories[obj_type]
        assert isclass( f ) or ismethod( f ) or isfunction( f ), "%s factory method is not a function (%s)" % (obj_type, str(type(f)))
        return f( *args, **kwds )

    @staticmethod
    def import_all():
        cmds = []
        for obj_type in Factory.__factories.keys():
            f, pkg = Factory.__factories[obj_type]
            if pkg is not None:
                cmds.append( "from %(pkg)s import %(obj_type)s" % locals() )
        return cmds
