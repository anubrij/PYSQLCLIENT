from pyodbc import *

"""Enum to show the current state of connection"""
class ConnectionState:
    Close = 0
    Open = 1

class SqlConnection(object):
    """docstring for SqlConnection."""
    __attr__ = None
    def __init__(self, connectionString):
        self.connectionString = connectionString
        self.State = ConnectionState.Close
        self.connectionAttributes = self.__splitconnectionstr__(self.connectionString)
        __attr__ = self.connectionAttributes

    def __splitconnectionstr__(self, str):
        parts = str.split(';')
        return dict([(s.split("=")[0].upper() , s.split("=")[1] ) for s in parts])

    def Open(self):
        self.__con__ = connect('DRIVER={Sql Server};SERVER={0};DATABASE={1};UID={2};PWD={3}'.format(__attr__['DATA SOURCE'] , __attr__['INITIAL CATELOG'] ,  __attr__['USER ID'], __attr__['PASSWORD']))
