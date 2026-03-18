from __future__ import print_function
import sys, sqlite3, re, os, random
import snappy_manifolds
# import ast

# This module uses sqlite3 databases with multiple tables.
# The path to the database file is specified at the module level.
from .sqlite_files import __path__ as manifolds_paths

manifolds_path = manifolds_paths[0]
database_path = os.path.join(manifolds_path, 'veering_16.sqlite')

split_filling_info = re.compile(r'(.*?)((?:\([0-9 .+-]+,[0-9 .+-]+\))*$)')

original_manifolds_path = snappy_manifolds.manifolds_path
original_database_path = os.path.join(original_manifolds_path, 'manifolds.sqlite')

def get_tables(ManifoldTable):
    """
    Functions such as this one are meant to be called in the
    __init__.py module in snappy proper.  To avoid circular imports,
    it takes as argument the class ManifoldTable from database.py in
    snappy. From there, it builds all of the Manifold tables, for example
    here from the sqlite 11_tet.sqlite in manifolds_src and manifolds.sqlite
    from snappy_manifolds, and returns the merged table as an element in a list.
    """

    class VeeringCensus(ManifoldTable):
        """ 
        Iterator for all veering triangulations with up to 16 tetrahedra.
        """
        
        _regex = re.compile(r'([msvt])([0-9]+)$|o([0-9]+)_([0-9]+)$')
        
        def __init__(self, **kwargs):
            ManifoldTable.__init__(self, table = 'veering_16_view',
                                   db_path = original_database_path, **kwargs)

            view_name = 'veering_16_view'

            conn = self._connection
            cursor = conn.cursor()
            
            # Dictionary specifying tables to append
            # Keys: paths of databases -> Values: tables contained by given databases
            # All tables specified will be appended to the view <view_name>
            sql_dict = {
                database_path : ['veering_16']
            }

            table_dict = dict() 
            # records the aliases of databases containing a given table
            alias_dict = dict() 
            # records the alias of a given database file (1-to-1)


            for i, sql_path in enumerate(sql_dict.keys(), start = 1):
                alias = f'db{i}'
                alias_dict.update({sql_path : alias})

                for table_name in sql_dict[sql_path]:
                    if table_name not in table_dict.keys():
                        table_dict.update({table_name : [alias]})
                    else:
                        table_dict.update({table_name : table_dict[table_name] + [alias]})

                cursor.execute('ATTACH DATABASE ? AS ?', (sql_path, alias))

            select_statements = [f'SELECT * FROM {self._table}']
            for table_name in table_dict.keys():
                for alias in table_dict[table_name]:
                    select_statements.append(f"SELECT * FROM {alias}.{table_name}")
            union_query = ' UNION ALL '.join(select_statements)

            create_view_sql = f"CREATE TEMPORARY VIEW {view_name} AS {union_query}"
            cursor.execute(create_view_sql)
            cursor.close()

            self._table = view_name
            self._select = f'select name, triangulation from {view_name} '

            self._get_length()
            self._get_max_volume()

    return [VeeringCensus()]


def connect_to_db(db_path):
    """
    Open the given sqlite database, ideally in read-only mode.
    """
    if sys.version_info >= (3,4):
        uri = 'file:' + db_path + '?mode=ro'
        return sqlite3.connect(uri, uri=True)
    elif sys.platform.startswith('win'):
        try:
            import apsw
            return apsw.Connection(db_path, flags=apsw.SQLITE_OPEN_READONLY)
        except ImportError:
            return sqlite3.connect(db_path)
    else:
        return sqlite3.connect(db_path)
