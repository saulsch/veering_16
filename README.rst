Database of transverse veering triangulations up to 16 tetrahedra
=================================================================

..  NOTE: Hopeful we can merge this into `snappy_manifolds <https://github.com/3-manifolds/snappy_manifolds>`_ version 1.4 and delete all of this garbage.
   
This repository contains the manifold database of all transverse veering triangulations with at most sixteen tetrahedra. The data is also available here:

  Andreas Giannopoulos, Saul Schleimer and Henry Segerman.
  A census of veering structures. 
  `https://math.okstate.edu/people/segerman/veering.html <https://math.okstate.edu/people/segerman/veering.html>`_, 2019.

To install this package, do::

  python -m pip install --upgrade veering_16

or, if you are using SageMath::

  sage -pip install --upgrade veering_16

The above command should be able to automatically install the 1.4 version of :code:`snappy_manifolds`, if it is not readily installed.

To use this module with SnapPy, you need to have SnapPy version 3.3.2 or later installed. You can check your SnapPy version with::

  >>> import snappy
  >>> snappy.__version__
  '3.3.2'

If you have an older version of SnapPy, you can upgrade it with::

  python -m pip install --upgrade snappy

or, if you are using SageMath::

  sage -pip install --upgrade snappy

With the above setup, simply importing :code:`snappy` will automatically import :code:`snappy_11_tets` and make the extended census available in SnapPy. The extended census can then be accessed via SnapPy's :code:`Manifold` class. 

The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other users.  The triangulations themselves are stored in the "isosig" format of Burton, as described in the appendix to `this paper
<http://arxiv.org/abs/1110.6080>`_ with an added "decoration" suffix
that describes the taut angle structure.
