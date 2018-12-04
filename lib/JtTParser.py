# -*- coding: utf-8 -*-

import json

class JtTParser(object):
    """docstring for JtTParser."""
    def __init__(self, pathtofilename=""):
        super(JtTParser, self).__init__()
        self.pathtofilename = pathtofilename
        self.data = {}

    def sortData(self, order="ASC"):
        if order in ["ASC", "DESC"]:
            lines = self.data["terms"]
            lines.sort(key=lambda k: k.get('name', 'term_blank'), reverse=(order=="DESC"))
            print(lines)
        else :
            raise TypeError("Order value must be \"ASC\" or \"DESC\". Got order="+order)

    def load(self, pathtofilename=""):
        if pathtofilename == "":
            if self.pathtofilename != "":
                pathtofilename = self.pathtofilename
            else :
                raise FileNotFoundError("No pathtofilename given.")
        f = open(pathtofilename, 'r')
        jsondata = ''.join(f.readlines())
        f.close()
        self.data = json.loads(jsondata)

    def exportToTex(self, texfilename="index.tex"):
        if texfilename != "":
            pass
        else :
            raise FileNotFoundError("No texfilename given.")
