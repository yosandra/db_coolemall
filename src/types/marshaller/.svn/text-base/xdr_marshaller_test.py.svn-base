# Copyright 2003-2009 Minor Gordon, with original implementations and ideas contributed by Felix Hupfeld.
# This source comes from the Yield project. It is licensed under the GPLv2 (see COPYING for terms and conditions).

import unittest

from marshaller_test import MarshallerTestCase, MarshallerTestSuite 
from xdr_marshaller import XDRMarshaller
from xdr_unmarshaller import XDRUnmarshaller


class XDRMarshallerTestCase(MarshallerTestCase):
    def createMarshaller( self ):
        return XDRMarshaller()

    def createUnmarshaller( self, marshaller ):
        return XDRUnmarshaller( marshaller.get_buffer() )


suite = MarshallerTestSuite( XDRMarshallerTestCase )


if __name__ == "__main__":
    unittest.TextTestRunner().run( suite )
