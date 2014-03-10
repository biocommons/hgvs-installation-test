=====================
hgvs integration test
=====================

This package is purely an integration test to ensure that the hgvs_ Python
package installs and executes basic functions correctly. It provides no
new code on its own.

It runs the following doctests via doctests::

  >>> import hgvs.parser
  >>> hp = hgvs.parser.Parser()
  >>> hgvs_g = 'NC_000007.13:g.36561662C>T'
  >>> var_g = hp.parse_hgvs_variant(hgvs_g)
  >>> var_g
  SequenceVariant(ac=NC_000007.13, type=g, posedit=36561662C>T)

  >>> import bdi.sources.uta1, hgvs.hgvsmapper
  >>> bdi = bdi.sources.uta1.connect()
  >>> hm = hgvs.hgvsmapper.HGVSMapper( bdi, cache_transcripts=True )
  >>> var_c = hm.hgvsg_to_hgvsc( var_g, 'NM_001637.3' )
  >>> var_c
  SequenceVariant(ac=NM_001637.3, type=c, posedit=1582G>A)


.. _hgvs: http://bitbucket.org/invitae/hgvs/
