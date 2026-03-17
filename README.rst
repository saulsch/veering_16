The database for transverse veering triangulations with up to 16 tetrahedra
============================

..  HEADS-UP: The data in this repository has been merged into `snappy_manifolds <https://github.com/3-manifolds/snappy_manifolds>`_ version 1.4,
..  which automatically comes with SnapPy 3.3. Hence there is no need to install this module for anyone with SnapPy>=3.3. 

This repository stores the manifold database of a complete census of
all transverse veering triangulations with at most sixteen tetrahedra.
This data is also available from the webpage:

  Andreas Giannopoulos, Saul Schleimer and Henry Segerman. 
  A census of veering structures. 
  `https://math.okstate.edu/people/segerman/veering.html <https://math.okstate.edu/people/segerman/veering.html>`_, 2019.

The repository includes the source code for the Python module
:code:`veering_16` which packages them up for use in SnapPy.

To install the module in SageMath::

  sage -pip install git+https://github.com/saulsch/veering_16/

To use this module with SnapPy, one can do::

  sage: from veering_16 import snappy

The extended census can then be accessed via SnapPy's :code:`Manifold` class. 
For example::

  sage: M = snappy.Manifold('cPcbbbiht_12')
  sage: M.identify()
  '[fix]'

The iterator for all manifolds in this module is :code:`snappy.VeeringCensus`. For example::
  
  sage: for M in snappy.VeeringCensus[1:3]: print(M, M.volume()) 
  FIX

  sage: for M in snappy.VeeringCensus(num_cusps=2)[2:5]: print(M, M.volume(), M.num_cusps())
  FIX
  
The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other
users. The triangulations themselves are stored in the "isosig" format
of Burton, as described in the appendix to his
`paper <http://arxiv.org/abs/1110.6080>`_ with an added "decoration"
suffix that describes the angle structures.
