#------------------------------------------------------------------------------
# Copyright (c) 2012, 2013, 2014, 2015 Francesco Paraggio.
# 
# Author: Francesco Paraggio fparaggio@gmail.com
# 
# This file is part of Python-Windsim
# 
# Python-Windsim is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.
# 
# The usage of a range of years within a copyright statement contained within this distribution should be interpreted as being equivalent to a list of years including the first and last year specified and all consecutive years between them. For example, a copyright statement that reads 'Copyright (c) 2005, 2007- 2009, 2011-2012' should be interpreted as being identical to a statement that reads 'Copyright (c) 2005, 2007, 2008, 2009, 2011, 2012' and a copyright statement that reads "Copyright (c) 2005-2012' should be interpreted as being identical to a statement that reads 'Copyright (c) 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012'."
#------------------------------------------------------------------------------
import sys, os

filePath = r'D:\junk\Baton+\BatonDBGenerator\WorkingSet\src\6.DAT'




def getCompleteIndividual_WECS_Text(file):
    try:
        if (not os.path.exists(file)):
            return [0, file + ' does not exists']

        masterWECSList = []
        tmpWECSList = []

        fileHandle = open (file, 'r')

        WECS_Start = 'WECS number'
        startedPushingData = False
        foundFirstWECS = False
        for line in fileHandle:
            line = line.strip()

            if (WECS_Start in line):
                foundFirstWECS = True
                if (startedPushingData == False):
                    startedPushingData = True
                else:
                    masterWECSList.append(tmpWECSList)
                    tmpWECSList = []

            if(foundFirstWECS == True):
                tmpWECSList.append(line)

        masterWECSList.append(tmpWECSList)
        return [1, masterWECSList]
    except Exception, e :
        return [0, str(e)]




def getHighLevelItemsDict_From_Individual_WECS_Text(WECS_List):
    try:
        #This function will take input a list of line about the
        # a individual turbine.
        # i.e starting from WECS name to next WECS name including sectors.

        masterDict = {}

        listOfLegalItems = ['WECS number', 'WECS name', 'Manufacturer', 'Type', 'Nominal effect', 'Hub height', 'x (local)', 'y (local)', 'x (global)', 'y (global)']
        for line in WECS_List:
            line = line.strip()
            for legalItem in listOfLegalItems:
                if legalItem in line:
                    x = line.split(r':')
                    value = x[len(x)-1].strip()

                    masterDict[legalItem] = value
        return [1, masterDict]
    except Exception, e :
        return [0, str(e)]


def getIndividualSector_From_Individual_WECS_Text(WECS_List):
    try:
        #This function will return
        #    [1/ 0, list of list]
        #    each list will be a list of lines of a sector.

        masterWECSList = []
        tmpWECSList = []

        WECS_Start = 'sector:'
        startedPushingData = False
        foundFirstWECS = False
        for line in WECS_List:
            line = line.strip()
            #print 'Processing : ', line

            if (WECS_Start in line):
                foundFirstWECS = True
                if (startedPushingData == False):
                    startedPushingData = True
                else:
                    masterWECSList.append(tmpWECSList)
                    tmpWECSList = []

            if(foundFirstWECS == True):
                tmpWECSList.append(line)

        masterWECSList.append(tmpWECSList)
        return [1, masterWECSList]
    except Exception, e :
        return [0, str(e)]


def getDataStructureAboutIndividualSector(sectorList):
    try:
        #This function will return
        #    [1/ 0, list of list]
        #    each list will be a list of lines of a sector.

        header_sectorList = ['k', 'z-coord', 'UCRT']
        lineToBeIgnored = False

        sector = -99
        tmpDict = {}
        for line in sectorList:
            line = line.strip()

            if lineToBeIgnored == True:
                lineToBeIgnored = False
                continue

            if 'sector:' in line:
                tmpList = line.split()
                sector = tmpList[len(tmpList)-1]
                continue

            if ( (header_sectorList[0] in line) or (header_sectorList[1] in line) or (header_sectorList[2] in line) ):
                sectorKeys = line.split()
                lineToBeIgnored = True
                #print 'sectorKeys = ', sectorKeys
                for tmpKey in sectorKeys:
                    tmpDict[tmpKey] = []

                continue

            #code to split the value of sector
            tmpListOfValues = line.split()
            i = -1
            for value in tmpListOfValues:
                i = i + 1
                tmpDict[sectorKeys[i]].append(value)


        tmpDict['sector'] = sector
        return [1, tmpDict]
    except Exception, e :
        return [0, str(e)]



def printTurbineSummary(turbineDict):
    #This function will print the folloing for each turbine:
    #    WECS number
    #    WECS Name
    #    Number of Sectors
    #    Names of sectors

    for key in turbineDict:
        print 'Printing information about Turbine # ', key

        for key_Individual_Turbine in turbineDict[key].keys():
            if (key_Individual_Turbine == 'sectorDict'):
                continue
            print key_Individual_Turbine, ' : ', turbineDict[key][key_Individual_Turbine]

        print 'Sector Information : '

        #this will give the list of all the sector numbers.
        for sectorKey in turbineDict[key]['sectorDict'].keys():
            for tmpKey in turbineDict[key]['sectorDict'][sectorKey].keys():
                print "\t", tmpKey, ' : ', turbineDict[key]['sectorDict'][sectorKey][tmpKey]

            print "\n\n"
        print "\n\n\n\n"
