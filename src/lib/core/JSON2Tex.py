# -*- coding: utf-8 -*-

import json
import sys

class JSON2Tex(object):
    """docstring for JSON2Tex."""
    def __init__(self, pathtofilename=""):
        super(JSON2Tex, self).__init__()
        self.pathtofilename = pathtofilename
        self.data   = {}
        self.terms  = []

    def sortData(self, order="ASC"):
        if order in ["ASC", "DESC"]:
            self.terms.sort(key=lambda k: k.get('name', 'term_blank'), reverse=(order=="DESC"))
        else :
            raise TypeError("Order value must be \"ASC\" or \"DESC\". Got order="+order)

    def printData(self):
        for element in self.terms:
            print(element)

    def load(self, pathtofilename=""):
        if pathtofilename == "":
            if self.pathtofilename != "":
                pathtofilename = self.pathtofilename
            else :
                raise FileNotFoundError("No pathtofilename given.")
        f = open(pathtofilename, 'r')
        jsondata = ''.join(f.readlines())
        f.close()
        self.data   = json.loads(jsondata)
        self.terms  = self.data["terms"]

    def exportToTex(self, texfilename="index.tex"):
        if texfilename != "":
            if not texfilename.endswith(".tex"):
                texfilename += ".tex"
            datatex = """"""
            for element in self.terms:
                datatex += "\\subsectionnn{" + element['name'] + "}\n"
                datatex += "\\label{" + element['ref'] + "}\n\n"
                datatex += element['descr']
                datatex += "\n\n"
            f = open(texfilename, 'w')
            f.write(datatex)
            f.close()
        else :
            raise FileNotFoundError("No texfilename given.")

    def exportToJSON(self, jsonfilename="index.json"):
        if jsonfilename != "":
            if not jsonfilename.endswith(".json"):
                jsonfilename += ".json"
            f = open(jsonfilename, 'w')
            f.write(json.dumps(self.data, indent=4))
            f.close()
        else :
            raise FileNotFoundError("No jsonfilename given.")


# if __name__ == '__main__':
#     a = JSON2Tex()
#     a.load(jsoninfile)
#     a.sortData()
#     a.exportToJSON(jsoninfile)
#     a.exportToTex(texoutfile)
