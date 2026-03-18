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

        # ISSUE: current names might overlap with decorated isosigs.
        _regex = re.compile(r'([a-zA-Z]_[012]+)$')
        _select = 'select name, triangulation from %s '

        def __init__(self, **kwargs):
            return ManifoldTable.__init__(self,
                                         table='veering_16_view',
                                         db_path=database_path,
                                         **kwargs)
        def _finalize(self, M, row):
            M.set_name(row[0])

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
