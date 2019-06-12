#!/usr/bin/python2.7
# coding=utf-8
import xlrd
import xlwt
import json
import os.path
import datetime
import os
from glob import glob
import shutil
import urllib
from pip._vendor.six import u
import codecs


def getColNames(sheet):
    rowSize = sheet.row_len(0)
    colValues = sheet.row_values(0, 0, rowSize)
    columnNames = []

    for value in colValues:
        if value is u'':
            pass
        else:
            # unicode(value, "utf8")
            columnNames.append (value)

    return columnNames


def getWorkBookData(workbook):
    # type: (object) -> object
    sheets = workbook.sheets ()
    print type (sheets)
    counter = 0
    # workbookdata = {}
    workbookList = []
    for sheet in sheets:
        idx = 0
        sheetName = sheet.name
        #worksheet = workbook.sheet_by_index(idx)
        columnNames = getColNames(sheet)

        # organize workbooList
        sheetInfo = {}
        aColsData = []
        for columnName in columnNames:
            aColsDict = {}
            aColsDict['sName'] = columnName
            aColsDict['sTechName'] = ""
            aColsData.append(aColsDict)

        sheetInfo["sSheetName"] = sheetName
        sheetInfo["aCols"] = aColsData
        #sheetInfo = sorted(sheetInfo.keys(), reverse=True)
        workbookList.append(sheetInfo)
        idx = idx + 1
    return workbookList


def main():
    filename = raw_input("Enter the path to the filename -> ")
    print type (filename)
    filename = unicode(filename, "utf8")
    if os.path.isfile(filename):
        workbook = xlrd.open_workbook(filename)
        workbookdata = getWorkBookData(workbook)
        file_name = os.path.splitext(filename)[0]
        with codecs.open(file_name+'.json', 'w', 'utf-8') as w:
            w.write(json.dumps(workbookdata, ensure_ascii=False, sort_keys=True, indent=2,  separators=(',', ": ")))
        w.close()
        print "%s was created" % file_name
    else:
        print "Sorry, that was not a valid filename"

main ()
