# -*- coding: utf-8 -*-

import json
import sys

class JtTParser(object):
    """docstring for JtTParser."""
    def __init__(self, pathtofilename=""):
        super(JtTParser, self).__init__()
        self.pathtofilename = pathtofilename
        self.data           = []

    def sortData(self, order="ASC"):
        if order in ["ASC", "DESC"]:
            self.data.sort(key=lambda k: k.get('name', 'term_blank'), reverse=(order=="DESC"))
        else :
            raise TypeError("Order value must be \"ASC\" or \"DESC\". Got order="+order)

    def printData(self):
        for element in self.data:
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
        data = json.loads(jsondata)
        self.data = data["terms"]

    def exportToTex(self, texfilename="index.tex"):
        if texfilename != "":
            if not texfilename.endswith(".tex"):
                texfilename += ".tex"
            datatex = """"""
            for element in self.data:
                datatex += "\\textbf{" + element['name'] + "}\n"
                datatex += "\\label{" + element['ref'] + "}\n"
                datatex += element['descr']
                datatex += "\n\n"
            f = open(texfilename, 'w')
            f.write(datatex)
            f.close()
        else :
            raise FileNotFoundError("No texfilename given.")


usage = """\n"""
usage += "  Usage : python3 jttparser.py infile.json outfile.tex\n"


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 3:
        jsoninfile = args[1]
        texoutfile = args[2]
        a = JtTParser()
        a.load(jsoninfile)
        a.sortData()
        a.exportToTex(texoutfile)
    else :
        print(usage)
