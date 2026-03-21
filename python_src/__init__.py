__version__ = '1.0.5'

def version():
    return __version__

import sys
from .database import get_tables, manifolds_path, original_manifolds_path

try:
    import snappy
    table_dict = snappy.database.add_tables_from_package('veering_16', False)
    for name, table in table_dict.items():
        setattr(snappy, name, table)
        if name not in snappy.database_objects:
            snappy.database_objects.append(name)
except ImportError:
    raise RuntimeError('Error happened when loading veering 16 tet census data to SnapPy')
