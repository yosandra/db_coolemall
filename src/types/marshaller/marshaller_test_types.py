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

try:
    from timacs.types import Map, Sequence, Struct
except ImportError:
    raise
    Map = dict
    Sequence = list
    Struct = object


class BooleanStruct(Struct):
    def __init__( self, data=False ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeBoolean( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readBoolean( "data" )
            

class DoubleStruct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeDouble( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readDouble( "data" )


class EmptyStruct(Struct):
    pass


class FloatStruct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeFloat( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readFloat( "data" )


class Int8Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeInt8( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readInt8( "data" )


class Int16Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeInt16( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readInt16( "data" )
            

class Int32Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeInt32( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readInt32( "data" )
            

class Int64Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeInt64( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readInt64( "data" )
            

class StringStruct(Struct):
    def __init__( self, data="" ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeString( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readString( "data" )
            

class Uint8Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeUint8( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readUint8( "data" )
            

class Uint16Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeUint16( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readUint16( "data" )
            

class Uint32Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeUint32( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readUint32( "data" )
            

class Uint64Struct(Struct):
    def __init__( self, data=0 ):
        self.data = data

    def marshal( self, marshaller ):
        marshaller.writeUint64( "data", self.data )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readUint64( "data" )
            


class StringSetStruct(Struct):
    def __init__( self, *args ):
        self.data = Sequence()
        self.data.extend( args )

    def marshal( self, marshaller ):
        marshaller.writeSequence( "data", self.data )
        #for i in xrange( len( self ) ):
        #    marshaller.writeString( str( i ), self[i] )

    def unmarshal( self, unmarshaller ):
        self.data = unmarshaller.readSequence( "data", self.data )
        #for i in xrange( len( self ) ):
        #    self[i] = unmarshaller.readString( str( i ) )                     


class StringStructSet(Sequence):
    def marshal( self, marshaller ):
        for i in xrange( len( self ) ):
            marshaller.writeStruct( str( i ), self[i] )

    def unmarshal( self, marshaller ):
        for i in xrange( len( self ) ):
            self[i] = StringStruct(); unmarshaller.readStruct( str( i ), self[i] )                     


class StringMap(Map):
    def marshal( self, marshaller ):
        for key, value in self.iteritems():
            marshaller.writeString( key, value )

    def unmarshal( self, unmarshaller ):
        key = unmarshaller.readString( None )
        value = unmarshaller.readString( key )
        self[key] = value


class StringStructMap(Map):
    def marshal( self, marshaller ):
        for key, value in self.iteritems():
            marshaller.writeStruct( key, value )

    def unmarshal( self, unmarshaller ):
        key = unmarshaller.readString( None )
        value = StringStruct(); unmarshaller.readStruct( key, value )
        self[key] = value
            
