# Copyright 2003-2009 Minor Gordon, with original implementations and ideas contributed by Felix Hupfeld.
# This source comes from the Yield project. It is licensed under the GPLv2 (see COPYING for terms and conditions).

import unittest

from marshaller_test import MarshallerTestCase, MarshallerTestSuite 
from primitive_types_marshaller import PrimitiveTypesMarshaller
from primitive_types_unmarshaller import PrimitiveTypesUnmarshaller


class PrimitiveTypesMarshallerTestCase(MarshallerTestCase):
    def createMarshaller( self ):
        return PrimitiveTypesMarshaller( dict() )

    def createUnmarshaller( self, marshaller ):
        return PrimitiveTypesUnmarshaller( marshaller._out_pt )


suite = MarshallerTestSuite( PrimitiveTypesMarshallerTestCase )


if __name__ == "__main__":
    unittest.TextTestRunner().run( suite )
