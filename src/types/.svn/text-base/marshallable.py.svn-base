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


__all__ = ["MarshallableObject"]


class MarshallableObject():
    def __repr__( self ):
        keys = self.keys()
        keys.sort()
        params = ", ".join( "%s=%s" % (key, repr(self.getValue(key))) for key in self.keys() )
        return "%s(%s)" % (self.__class__.__name__, params)

    def __str__( self ):        
        from cStringIO import StringIO
        from marshaller.pretty_printer import PrettyPrinter
        out_string_io = StringIO()        
        self.marshal( PrettyPrinter( out_string_io ) )
        return out_string_io.getvalue()

    def __marshal( self, marshaller, key, obj ):
        if type(obj).__name__ == 'bool':
            marshaller.writeBoolean( key, obj )
        elif type(obj).__name__ == 'int':
            marshaller.writeInt32( key, obj )
        elif type(obj).__name__ == 'long':
            marshaller.writeInt64( key, obj )
        elif type(obj).__name__ == 'float':
            marshaller.writeDouble( key, obj )
        elif type(obj).__name__ == 'str':
            marshaller.writeString( key, obj )
        elif type(obj).__name__ == 'unicode':
            marshaller.writeString( key, str(obj) )
        elif isinstance ( obj, list ):
            if is_simple_sequence( obj ):
                marshaller.writeSimpleSequence( key, obj )
            else:
                marshaller.writeSequence( key, obj )
        elif isinstance ( obj, dict ):
            if is_simple_map( obj ):
                marshaller.writeSimpleMap( key, obj )
            else:
                marshaller.writeMap( key, obj )
        else:
            # it's some other sort of object, try marshalling as a map
            try:
                #print "marshalling object of type", type(obj), "class", obj.__class__.__name__
                marshaller.writeMap( key, obj )
            except:
                raise NotImplementedError, key + ":" + str( type(obj) )
        
    def marshal( self, marshaller ):
        #self.__marshal( marshaller, "__class__", self.__class__.__name__.split(".")[-1] )
        keys = self.keys()
        keys.sort()
        for key in keys:
            if key.startswith("__"):
                continue
            value = self.getValue(key)
            if value is not None:
                if is_primitive_type( value ) or len( value ) > 0:
                    #print "map marshaling key:", key, "value:", type(value)
                    self.__marshal( marshaller, key, value )

    def unmarshal( self, unmarshaller ):
        self.clear()
        keys = unmarshaller.readKeysOrNone()
        assert keys != None, 'no keys found in Metric'
        for key in keys:
            object_type = unmarshaller.readObjType( key )
            if object_type == "simple":
                self.setValue( key, unmarshaller.readObj( key ) )
            else:
                from factory import Factory

                object = Factory.build( object_type )
                if isinstance( object, list ):
                    unmarshaller.readSequence( key, object )
                else:
                    unmarshaller.readMap( key, object )
                self.setValue( key, object )
