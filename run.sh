#!/bin/bash

JSONDIR=data
EXPORTDIR=exported
FILENAME=ccna_terms

python3 json2Tex.py ${JSONDIR}/${FILENAME}.json ${EXPORTDIR}/${FILENAME}.tex
