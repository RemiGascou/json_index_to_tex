# -*- coding: utf-8 -*-

path = 'D:\\Projets GIT\\#Python Projects - GIT\\json_index_to_tex\\'

jsoninfile = "data/ccna_terms.json"
texoutfile = "exported/ccna_terms.tex"
a = JSON2Tex()
a.load(path + jsoninfile)
a.sortData()
a.exportToJSON(path + jsoninfile)
a.exportToTex(path + texoutfile)
