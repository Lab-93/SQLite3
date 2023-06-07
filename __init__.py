#!/bin/python3
"""
The SQLite3_Statements class offers a library of pre-defined SQL statements,
indexed and stored as a human-readable dictionary.

The class object accepts a `database` string that should be a valid
filepath to an sqlite3.db file.  After initialization, member methods
can be called at-will in your code to provide a simple API for database
functionality.
"""


from sqlite3 import connect
#from Lab93Cryptogram import CryptographyMethodsAPI as cryptogram




class databaseConnection:
    """
    The SQLite3.databaseConnection object is an internal class used by the
    functionality suite used for abstracting away overhead involved with using
    the built-in sqlite3 library.

    Given a `database` string, which is a valid filepath pointing to a .db file,
    the member objects databaseConnection.connection and
    databaseConnection.cursor are accessibile from a freshly created thread.
    """

    def __init__( self,
                  database: str="./.sqlite3.db" ) -> None:
        try:
            self.connection = connect(
                database
            ); self.cursor = self.connection\
                                 .cursor()
        except Exception as error:
            return error


'''  Master dictionary of various sqlite3 statements. '''
self.statements = {
         
    "help": self.listStatements,


    'queryCompareColumns': {
        # Select a specific column from a row based on another column.
        'syntax': "SELECT {} FROM {} WHERE  {}='{}';",
        'help': """SELECT $COLUMN FROM $TABLE WHERE $COMPARATOR = $VALUE;
        
        Returns the value of a specific column if another column equals
        an exact value.

        ARGUMENTS:
            - database,
            - column,
            - table,
            - comparator,
            - value


        """
    },


    'createNewColumn': {
        # Add a new column to the database.
        'syntax': "ALTER TABLE {} ADD {} {};",
        'help': """ALTER TABLE $TABLE ADD $COLUMN $TYPE;

        Adds a new $COLUMN of $TYPE to $TABLE.

        ARGUMENTS:
            - database,
            - table,
            - column,
            - column_type


        """
    },


    'createNewTable': {
        # Create a new new table within the database.
        'syntax': "CREATE TABLE IF NOT EXISTS {}({} {} PRIMARY KEY);",
        'help': """CREATE TABLE IF NOT EXISTS $TABLE( $COLUMN $TYPE PRIMARY KEY);

        Create a new table named $TABLE, with an initial compulsory column $COLUMN
        of type $TYPE, which is also a primary key.

        ARGUMENTS:
            - database,
            - table,
            - column,
            - column_type


        """
    },

    '''
    'queryTableData': {
        # Collect everything from a given table.
        'syntax': "SELECT * FROM {};",
        'help': """SELECT * FROM $TABLE;
        
        Pulls everything from a table in a form that can be accessed
        like an array.

        ARGUMENTS:
            - database,
            - table


        """
    },
    '''

    'queryTableExistence': {
        # Check if a specific table exists within the database.
        'syntax': "SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{}';",
        'help': """SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name=$TABLE;
        
        Returns either 0 or 1, where 1 means that a $TABLE exists and 0 means
        it does not.

        ARGUMENTS:
            - database,
            - table


        """
    },


    # Check a given table for a specific column.
    'queryColumnExistence': {
        'syntax': "SELECT COUNT(*) FROM pragma_table_info('{}') WHERE name='{}';",
        'help': """SELECT COUNT(*) FROM pragma_table_info('$COLUMN' WHERE name='$TABLE';)

        Returns either one or zero, where one means that a $COLUMN exists within $TABLE.

        ARGUMENTS:
            - database,
            - table,
            -column


        """
    },


    # Enumerate a list of tables within the master record.
    'queryTableList': {
        'syntax': "SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;",
        'help': """SELECT name FROM sqlite_schema WHERE type='table ORDER BY name;"

        Curates a list of tables known to a specific $TABLE, alphabatized by name.

        ARGUMENTS:
            - database


        """
    },

    '''
    # Curate a list of headers for a given table.
    'queryHeaderList': {
        'syntax': "SELECT name FROM sqlite_master WHERE type='table';",
        'help': """SELECT name FROM sqlite_master WHERE type='table';

        Curates a list of columns from a given $TABLE.

        ARGUMENTS:
            - database,
            - table


        """
    },
    '''


    # Add a new row to a specific table.
    'createNewUniqueRow': {
        'syntax': "INSERT OR IGNORE INTO {}({}) VALUES({});",
        'help': """INSERT OR IGNORE INTO $TABLE($COLUMNS) VALUES($VALUES);

        Creates a new row in the database, meant to be unique to every other row
        in the database.  In this case, $COLUMNS can be multiple comma separated 
        names, and $VALUES their positionally related data values.

        ARGUMENTS:
            - database,
            - table,
            - columns,
            - values


        """
    },

}

