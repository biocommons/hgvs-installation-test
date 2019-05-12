
def test_parsing(parser):
    hgvs_g = "NC_000007.13:g.36561662C>T"
    var_g = parser.parse_hgvs_variant(hgvs_g)
    # no exception


# from hgvs.dataproviders.uta import connect
# hdp = connect()
#  
# from hgvs.assemblymapper import AssemblyMapper
# am = AssemblyMapper(hdp, assembly_name="GRCh37")
# var_c = am.g_to_c(var_g, "NM_001637.3")

