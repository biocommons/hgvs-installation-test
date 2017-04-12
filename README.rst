=====================
hgvs integration test
=====================

.. image:: https://travis-ci.org/reece/hgvs-installation-test.svg?branch=master
    :target: https://travis-ci.org/reece/hgvs-installation-test

This package is purely an integration test to ensure that the hgvs_
Python package and dependencies are installable from scratch and
executes basic functions correctly.

First, it installs `hgvs` using `pip`, then t runs the following
doctests via doctests::

  >>> from hgvs.parser import Parser
  >>> hp = Parser()
  >>> hgvs_g = "NC_000007.13:g.36561662C>T"
  >>> var_g = hp.parse_hgvs_variant(hgvs_g)
  >>> var_g
  SequenceVariant(ac=NC_000007.13, type=g, posedit=36561662C>T)

  >>> from hgvs.dataproviders.uta import connect
  >>> hdp = connect()

  >>> from hgvs.assemblymapper import AssemblyMapper
  >>> am = AssemblyMapper(hdp, assembly_name="GRCh37")
  >>> var_c = am.g_to_c(var_g, "NM_001637.3")
  >>> var_c
  SequenceVariant(ac=NM_001637.3, type=c, posedit=1582G>A)


.. _hgvs: http://github.com/biocommons/hgvs/
