# Copyright 2003-2009 Minor Gordon, with original implementations and ideas contributed by Felix Hupfeld.
# This source comes from the Yield project. It is licensed under the GPLv2 (see COPYING for terms and conditions).

from unittest import TestCase, TestSuite

from timacs.types.marshaller.marshaller_test_types import *


__all__ = ["MarshallerTestCase", "MarshallerTestSuite"]


class MarshallerTestCase(TestCase):
    def __init__( self, obj ):
        TestCase.__init__( self )
        self.obj = obj

    def createMarshaller( self ): raise NotImplementedError
    def createUnmarshaller( self, marshaller ): return None 

    def runTest( self ):
        marshaller = self.createMarshaller()
        marshalled_obj = self.obj.marshal( marshaller )
        unmarshaller = self.createUnmarshaller( marshaller )        
        if unmarshaller is not None:
            unmarshalled_obj = type( self.obj )()
            unmarshalled_obj.unmarshal( unmarshaller )
            if unmarshalled_obj != self.obj and repr( unmarshalled_obj ) != repr( self.obj ):
                print self.__class__.__name__ + ": got", repr(unmarshalled_obj), " and expected", repr(self.obj)
                self.fail()

    def shortDescription( self ):
        return self.__class__.__name__ + "(" + self.obj.__class__.__name__ + ")"


class MarshallerTestSuite(TestSuite):
    def __init__( self, marshaller_test_case_type ):
        TestSuite.__init__( self )
        self.addTest( marshaller_test_case_type( BooleanStruct( True ) ) )
        self.addTest( marshaller_test_case_type( BooleanStruct( False ) ) )
        self.addTest( marshaller_test_case_type( EmptyStruct() ) )    
        self.addTest( marshaller_test_case_type( FloatStruct( -1.0 ) ) )
        self.addTest( marshaller_test_case_type( FloatStruct( 0.0 ) ) )
        self.addTest( marshaller_test_case_type( FloatStruct( 1.0 ) ) )
        self.addTest( marshaller_test_case_type( DoubleStruct( -1.0 ) ) )
        self.addTest( marshaller_test_case_type( DoubleStruct( 0.0 ) ) )
        self.addTest( marshaller_test_case_type( DoubleStruct( 1.0 ) ) )
        self.addTest( marshaller_test_case_type( Int32Struct( -1 ) ) )
        self.addTest( marshaller_test_case_type( Int32Struct( 0 ) ) )
        self.addTest( marshaller_test_case_type( Int32Struct( 1 ) ) )
        self.addTest( marshaller_test_case_type( Int64Struct( -1 ) ) )
        self.addTest( marshaller_test_case_type( Int64Struct( 0 ) ) )
        self.addTest( marshaller_test_case_type( Int64Struct( 1 ) ) )
        self.addTest( marshaller_test_case_type( StringStruct( "" ) ) )
        self.addTest( marshaller_test_case_type( StringStruct( "test" ) ) )
        self.addTest( marshaller_test_case_type( StringSetStruct( "a", "b" ) ) )
        
