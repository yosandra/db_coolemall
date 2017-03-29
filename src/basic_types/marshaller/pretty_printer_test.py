# Copyright 2003-2009 Minor Gordon, with original implementations and ideas contributed by Felix Hupfeld.
# This source comes from the Yield project. It is licensed under the GPLv2 (see COPYING for terms and conditions).

import unittest

from marshaller_test import MarshallerTestCase, MarshallerTestSuite 
from pretty_printer import PrettyPrinter


class PrettyPrinterTestCase(MarshallerTestCase):
    def createMarshaller( self ):
        return PrettyPrinter()


suite = MarshallerTestSuite( PrettyPrinterTestCase )


if __name__ == "__main__":
    unittest.TextTestRunner().run( suite )
