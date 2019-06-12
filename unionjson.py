#!/usr/bin/python2.7
# coding=utf-8
import json
import os.path
import os
import codecs
import itertools
from collections import defaultdict

def unionData(data01, data02):
    data = []
    firstSheetNames = []
    for itemOne in data01:
        firstSheetNames.append(itemOne['sSheetName'])

    secondSheetNames = []
    for itemTwo in data02:
        secondSheetNames.append(itemTwo['sSheetName'])


    for first in data01:
        sheetInfo = {}
        firstSheetName = first['sSheetName']
        if firstSheetName not in secondSheetNames:
            for item in first['aCols']:
                item['sType'] = "player"
            data.append(first)
        else:
            for second in data02:
                if firstSheetName == second['sSheetName']:
                    firstsName = []
                    firstACols = first['aCols']
                    for firstACol in firstACols:
                        firstsName.append(firstACol['sName'])

                    secondsName = []
                    secondACols = second['aCols']
                    for secondACol in secondACols:
                        secondsName.append(secondACol['sName'])

                    aColsData = []
                    for firstName in firstsName:
                        if firstName not in secondsName:
                            aColsTypeDict = {}
                            aColsTypeDict['sName'] = firstName
                            aColsTypeDict['sTechName'] = ""
                            aColsTypeDict['sType'] = "player"
                            aColsData.append(aColsTypeDict)
                        else:
                            aColsDict = {}
                            aColsDict['sName'] = firstName
                            aColsDict['sTechName'] = ""
                            aColsData.append(aColsDict)


                    sheetInfo['sSheetName'] = firstSheetName
                    sheetInfo['aCols'] = aColsData

                    data.append(sheetInfo)
                    break

    for second in data02:
        secondSheetName = second['sSheetName']
        if secondSheetName not in firstSheetNames:
            for item in second['aCols']:
                item['sType'] = "staff"
            data.append(second)
        else:
            for first in data01:
                if secondSheetName == first['sSheetName']:
                    firstsName = []
                    firstACols = first['aCols']
                    for firstACol in firstACols:
                        firstsName.append(firstACol['sName'])

                    secondsName = []
                    secondACols = second['aCols']
                    for secondACol in secondACols:
                        secondsName.append(secondACol['sName'])


                    for secondName in secondsName:
                        if secondName not in firstsName:
                            aColsDict = {}
                            aColsDict['sName'] = secondName
                            aColsDict['sTechName'] = ""
                            aColsDict['sType'] = "staff"
                            for diffData in data:
                                if secondSheetName == diffData['sSheetName']:
                                    cols = diffData['aCols']
                                    cols.append(aColsDict)
                                    break
                    break

    return data


def main():
    filename01 = raw_input("Enter the path to the filename -> ")
    filename01 = unicode(filename01, "utf8")
    filename02 = raw_input("Enter the path to the filename -> ")
    filename02 = unicode(filename02, "utf8")
    if os.path.isfile(filename01) and os.path.isfile(filename02):
        # read file json data
        jsonData01 = {}
        jsonData02 = {}

        filename01open = open(filename01, "r")
        if filename01open.mode == 'r':
            contents01 = filename01open.read()
            jsonData01 = json.loads(contents01)
        filename02open = open(filename02, "r")
        if filename02open.mode == 'r':
            contents02 = filename02open.read()
            jsonData02 = json.loads(contents02)
        file_name = os.path.splitext(filename01)[0] + 'compine' + os.path.splitext(filename02)[0]

        # union json data
        uniondata = unionData(jsonData01, jsonData02)

        with codecs.open(file_name+'.json', 'w', 'utf-8') as w:
            w.write(json.dumps(uniondata, ensure_ascii=False, sort_keys=True, indent=2,  separators=(',', ": ")))
        w.close()
        print "%s was created" % file_name
    else:
        print "Sorry, that were not a valid filename"

main()