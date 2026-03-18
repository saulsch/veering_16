Database of transverse veering triangulations up to 16 tetrahedra
=================================================================

..  NOTE: The data in this repository has been merged into `snappy_manifolds <https://github.com/3-manifolds/snappy_manifolds>`_ version 1.4,
..  which automatically comes with SnapPy 3.3. Hence there is no need to install this module for anyone with SnapPy>=3.3. 
.. Once merged into :code:`snappy_manifolds` in version x.y, and now comes with SnapPy version a.b automatically, see `SnapPy's News page <https://snappy.computop.org/news.html>`_ for details.

This repository contains the manifold database of all transverse
veering triangulations with at most sixteen tetrahedra.
The data is also available here:

  Andreas Giannopoulos, Saul Schleimer and Henry Segerman.
  A census of veering structures. 
  `https://math.okstate.edu/people/segerman/veering.html <https://math.okstate.edu/people/segerman/veering.html>`_, 2019.

To install the module in SageMath::

  sage -pip install git+https://github.com/saulsch/veering_16/

To use this module with SnapPy, one can do::

  sage: from veering_16 import snappy

..  python -m pip install --upgrade veering_16
..  sage -pip install --upgrade veering_16

The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other
users. The triangulations themselves are stored in the "isosig" format
of Burton, as described in the appendix to `this paper
<http://arxiv.org/abs/1110.6080>`_ with an added "decoration"
that describes the angle structure.
