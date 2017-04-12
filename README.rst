=====================
hgvs integration test
=====================

.. image:: https://travis-ci.org/reece/hgvs-installation-test.svg?branch=master
    :target: https://travis-ci.org/reece/hgvs-installation-test

This package is purely an integration test to ensure that the hgvs_ Python
package installs and executes basic functions correctly. It provides no
new code on its own.

It runs the following doctests via doctests::

  >>> import hgvs.parser
  >>> hp = hgvs.parser.Parser()
  >>> hgvs_g = "NC_000007.13:g.36561662C>T"
  >>> var_g = hp.parse_hgvs_variant(hgvs_g)
  >>> var_g
  SequenceVariant(ac=NC_000007.13, type=g, posedit=36561662C>T)

  >>> from hgvs.assemblymapper import AssemblyMapper
  >>> from hgvs.dataproviders.uta import connect
  >>> hdp = connect()
  >>> am = AssemblyMapper(hdp, assembly_name="GRCh37")
  >>> var_c = am.g_to_c(var_g, "NM_001637.3")
  >>> var_c
  SequenceVariant(ac=NM_001637.3, type=c, posedit=1582G>A)


.. _hgvs: http://github.com/biocommons/hgvs/
