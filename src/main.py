# -*- coding: utf-8 -*-

import json
from lib import *

a = JtTParser()
a.load("data/index_of_terms.json")
a.sortData()
a.exportToTex("exported/index_of_terms.tex")

if __name__ == '__main__':
    pass
