# Copyright 2003-2009 Minor Gordon, with original implementations and ideas contributed by Felix Hupfeld.
# This source comes from the Yield project. It is licensed under the GPLv2 (see COPYING for terms and conditions).

import unittest, shutil

from fs_marshaller import FSMarshaller
from fs_unmarshaller import FSUnmarshaller
from marshaller_test import MarshallerTestCase, MarshallerTestSuite 


class FSMarshallerTestCase(MarshallerTestCase):
    def createMarshaller( self ):
        return FSMarshaller( "fs_marshaller_test" )

    def createUnmarshaller( self, marshaller ):
        return FSUnmarshaller( "fs_marshaller_test" )

    def tearDown( self ):
        shutil.rmtree( "fs_marshaller_test" )       


suite = MarshallerTestSuite( FSMarshallerTestCase )


if __name__ == "__main__":
    unittest.TextTestRunner().run( suite )
