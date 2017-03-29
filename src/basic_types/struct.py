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

class Struct(object):
    def __repr__( self ):
        return str( self )
    
    def __str__( self ):        
        from cStringIO import StringIO        
        from basic_types.marshaller.pretty_printer import PrettyPrinter
        out_string_io = StringIO()        
        self.marshal( PrettyPrinter( out_string_io ) )
        return out_string_io.getvalue()

    def marshal( self, marshaller ):
        from inspect import ismethod
        self_dict = self.__dict__
        if self_dict is not None:
            self_dict_keys = self_dict.keys()
            self_dict_keys.sort()
            for key in self_dict_keys:
                value = self_dict[key]
                if not key.startswith( "_" ) and not ismethod( value ):
                    marshaller.write( value )
                                
    def unmarshal( self, unmarshaller ): 
        pass    
