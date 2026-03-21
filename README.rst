Database of transverse veering triangulations up to 16 tetrahedra
=================================================================

..  NOTE: Hopeful we can merge this into `snappy_manifolds <https://github.com/3-manifolds/snappy_manifolds>`_ version 1.4 and delete all of this garbage.
   
This repository contains the manifold database of all transverse veering triangulations with at most sixteen tetrahedra. 
To install this package into python::

  python -m pip install --upgrade veering_16

or into SageMath::

  sage -pip install --upgrade veering_16

To use this module with SnapPy, you need to have SnapPy version 3.3.2 or later. 
You can check your SnapPy version as follows::

  >>> import snappy
  >>> snappy.__version__
  '3.3.2'

If you have an older version of SnapPy, you can upgrade it as follows::

  python -m pip install --upgrade snappy

or, in SageMath::

  sage -pip install --upgrade snappy

With the above setup, you can import :code:`snappy` and then import :code:`veering_16` to gain access to the veering census. 
For example, the :code:`.identify` method now reports that the figure-eight knot complement is the second manifold in the veering census::

  >>> import snappy
  >>> import veering_16
  >>> M = snappy.Manifold("m004")
  >>> M.identify()
  [m004(0,0), 4_1(0,0), K2_1(0,0), K4a1(0,0), otet02_00001(0,0), veer1(0,0)]

The figure-eight sibling is the first::

  >>> M = snappy.Manifold("veer0")
  >>> M.identify()
  [m003(0,0), otet02_00000(0,0), veer0(0,0)]

It is possible to slice the veering census in the `usual way <https://snappy.computop.org/censuses.html>`_.  
For example::

  >>> len(snappy.VeeringCensus())
  87047
  >>> len(snappy.VeeringCensus(num_cusps=1))
  59114

Each veering structure consists of a triangulation and an angle structure, as follows::

  >>> V = snappy.VeeringCensus()[12343]; V
  veer12343(0,0)(0,0)
  >>> V.triangulation_isosig(decorated = False)
  'oLAwLwzPQPccbbdfhijkklmnnnhhrhjajxxbbwxxa'
  >>> V.angles
  '12212201022221'

The triangulation is specified by Burton's "isosig" `format <http://arxiv.org/abs/1110.6080>`_.
The angle string describes the taut angle structure: 
an i in position k means that in tetrahedron k the edge (0,i+1) has dihedral angle pi.

The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other users.
The data is also available from the `census webpage <https://math.okstate.edu/people/segerman/veering.html>`_::

  Andreas Giannopoulos, Saul Schleimer, and Henry Segerman.
  A census of veering structures. 
  https://math.okstate.edu/people/segerman/veering.html, 2019.
