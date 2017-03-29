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

import hashlib


__all__ = ["is_ip_address", "is_primitive_type", "is_simple_sequence",
           "is_simple_map", "md5sum_file"]


def is_ip_address( ip ):
    "Check if argument is an IP address (dotted quad)."
    quad = ip.split( "." )
    if len( quad ) != 4:
        return False
    for q in quad:
        try:
            i = int( q )
        except ValueError:
            return False
        if i < 0 or i > 255:
            return False
    return True


def is_primitive_type( value ):
    return isinstance( value, ( bool, int, long, float, str, unicode ) )


def is_simple_sequence( array ):
    result = True
    for element in array:
        if not is_primitive_type( element ):
            result = False
            break
    return result


def is_simple_map( map ):
    result = True
    for element in map.values():
        if not is_primitive_type( element ):
            result = False
            break
    return result


def md5sum_file( fobj ):
    "Returns an md5 hash for a file object"
    m = hashlib.md5()
    while True:
        d = fobj.read(8096)
        if not d:
            break
        m.update(d)
    return m.hexdigest()
