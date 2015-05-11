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

from turbineDefs import *
import sys


try:
    filePath = sys.argv[1]
    print 'You\ve specified path from commandline : ', filePath, ' will be used'
except Exception, e:
    print 'You\'ve NOT provided the file path as commandline parameter'
    print filePath, ' will be used'


ListOfIndividualWECS =  getCompleteIndividual_WECS_Text(filePath)[1]


tmpDict = {}
tmpDict['sectorDict'] = {}

turbineDict = {}
for WECS in ListOfIndividualWECS:
    myDict = {}
    tmpDict = getHighLevelItemsDict_From_Individual_WECS_Text(WECS)[1]

    for key in tmpDict.keys():
        myDict[key] = tmpDict[key]

    myDict['sectorDict'] = {}
    #print 'High Level dictionary : ', tmpDict
#    for key in tmpDict.keys():
#        print key, ' : ', tmpDict[key]

    ListOfSectors = getIndividualSector_From_Individual_WECS_Text(WECS)[1]

    for sector in ListOfSectors:
        tmpSectorDict = getDataStructureAboutIndividualSector(sector)[1]
        myDict['sectorDict'][tmpSectorDict['sector']] = tmpSectorDict


    turbineDict[myDict['WECS number']] = myDict



#Application code starts from here.
print 'turbineDict = ', turbineDict
print "\n\n\n\n\n"


#Access Speed_2D of sector 300 of turbine number 89
Speed_2DList = turbineDict['89']['sectorDict']['300']['Speed_2D']

print 'Speed_2DList = ', Speed_2DList

#number of sectors in a particular turbine =
#len(turbineDict['89']['sectorDict'].keys())

#print len(ListOfIndividualWECS)

printTurbineSummary(turbineDict)



# Help

#Suppose the original .dat file is below:
#
#WECS number        :          3
#WECS name          : Turbine1
#Manufacturer       : francesco
#Type               : ws2000
#Nominal effect     :       2000
#Hub height         :       80.0
#x (local)          :     5581.8
#y (local)          :     4764.0
#x (global)         :   397934.8
#y (global)         :  5065174.0
#
#
#
#sector:   180
#
#  k       z-coord        UCRT         VCRT         WCRT      Speed_2D       Inflow        Shear    Shear_low   Shear_high           KE           TI        alpha
# (-)        (m)          (m/s)        (m/s)        (m/s)        (m/s)        (deg)        (1/s)        (1/s)        (1/s)    (m*2/s*2)          (%)          (-)
#   1       24.200       -2.616        3.475       -0.504        4.350       -6.604        0.082        0.180        0.034        1.035       27.000        0.457
#   2       73.450       -2.384        5.538        0.288        6.029        2.738        0.025        0.034        0.017        1.370       22.420        0.310
#   3      124.110       -2.131        6.554        0.763        6.892        6.317        0.016        0.017        0.015        1.197       18.334        0.291
#   4      178.548       -1.895        7.492        1.107        7.728        8.152        0.014        0.015        0.013        0.943       14.511        0.328
#   5      239.851       -1.664        8.372        1.314        8.535        8.750        0.012        0.013        0.011        0.626       10.704        0.331
#   6      309.716       -1.457        9.155        1.383        9.271        8.482         -           0.011         -           0.315        6.988         -
#
#
#
#WECS number        :          89
#WECS name          : Turbine2
#Manufacturer       : francesco
#Type               : ws2000
#Nominal effect     :       2000
#Hub height         :       80.0
#x (local)          :     3530.3
#y (local)          :     2967.0
#x (global)         :   395883.3
#y (global)         :  5063377.0
#
#
#
#sector:   190
#
#  k       z-coord        UCRT         VCRT         WCRT      Speed_2D       Inflow        Shear    Shear_low   Shear_high           KE           TI        alpha
# (-)        (m)          (m/s)        (m/s)        (m/s)        (m/s)        (deg)        (1/s)        (1/s)        (1/s)    (m*2/s*2)          (%)          (-)
#   1       20.293       -0.863        5.080        1.010        5.153       11.084        0.129        0.254        0.068        2.224       33.418        0.507
#   2       61.807       -1.188        7.867        1.035        7.956        7.410        0.052        0.068        0.038        2.376       22.372        0.407
#   3      105.392       -1.230        9.528        0.909        9.607        5.403        0.030        0.038        0.023        1.545       14.941        0.331
#   4      154.020       -1.203       10.673        0.823       10.741        4.382        0.019        0.023        0.014        0.830        9.794        0.266
#   5      211.191       -1.199       11.504        0.768       11.566        3.799        0.009        0.014        0.005        0.308        5.537        0.172
#   6      278.943       -1.206       11.857        0.708       11.918        3.401         -           0.005         -           0.077        2.689         -
#
#
#
#sector:   300
#
#  k       z-coord        UCRT         VCRT         WCRT      Speed_2D       Inflow        Shear    Shear_low   Shear_high           KE           TI        alpha
# (-)        (m)          (m/s)        (m/s)        (m/s)        (m/s)        (deg)        (1/s)        (1/s)        (1/s)    (m*2/s*2)          (%)          (-)
#   1       20.293       -1.002       -2.788        1.290        2.963       23.529        0.056        0.146        0.012        0.822       35.345        0.384
#   2       61.807       -0.286       -3.449        0.736        3.461       12.004        0.011        0.012        0.010        0.876       31.231        0.193
#   3      105.392        0.584       -3.838        0.302        3.882        4.446        0.014        0.010        0.017        1.067       30.723        0.373
#   4      154.020        1.940       -4.310       -0.418        4.727       -5.052        0.019        0.017        0.020        1.051       25.046        0.615
#   5      211.191        3.346       -4.833       -0.927        5.879       -8.960        0.020        0.020        0.020        0.850       18.114        0.726
#   6      278.943        4.801       -5.435       -1.284        7.252      -10.039         -           0.020         -           0.614       12.471         -
#
#
#
#sector:   330
#
#  k       z-coord        UCRT         VCRT         WCRT      Speed_2D       Inflow        Shear    Shear_low   Shear_high           KE           TI        alpha
# (-)        (m)          (m/s)        (m/s)        (m/s)        (m/s)        (deg)        (1/s)        (1/s)        (1/s)    (m*2/s*2)          (%)          (-)
#   1       20.293        0.036       -5.109        0.078        5.109        0.874        0.117        0.252        0.052        2.016       32.093        0.466
#   2       61.807        1.055       -7.174       -0.590        7.251       -4.655        0.047        0.052        0.042        1.459       19.237        0.397
#   3      105.392        1.924       -8.866       -1.036        9.072       -6.514        0.035        0.042        0.029        1.064       13.126        0.409
#   4      154.020        2.685      -10.151       -1.334       10.500       -7.242        0.024        0.029        0.019        0.744        9.483        0.346
#   5      211.191        3.385      -11.061       -1.479       11.567       -7.288        0.015        0.019        0.011        0.503        7.082        0.268
#   6      278.943        4.035      -11.657       -1.453       12.336       -6.716         -           0.011         -           0.321        5.302         -


#After the code is executed till the line saying 'application code starts here'
# a dictionary variable "turbineDict" is created.
#The structure of this variable is mentioned below:
#
#turbineDict {
#             '89' : {  #this the turbine number 'WECS number'
#                     'Nominal effect': '2000',
#                     'y (global)': '5063377.0',
#                     'WECS number': '89',
#                     'y (local)': '2967.0',
#                     'WECS name': 'Turbine2',
#                     'Hub height': '80.0',
#                     'x (global)': '395883.3',
#                     'x (local)': '3530.3',
#                     'Type': 'ws2000',
#                     'Manufacturer': 'francesc',
#                     'sectorDict' : {
#                                     '190' : {'k': [1, 2 ,3 ,4 ,5 ,6],
#                                              'z-coord' : [20.293, 61.807, 105.392, 154.020, 211.191, 278.943],
#                                              'UCRT': [actual values],
#                                                'VCRT': [actual values],
#                                                'WCRT': [actual values],
#                                                'Speed_2D': [actual values],
#                                                'Inflow': [actual values],
#                                                'Shear': [actual values],
#                                                'Shear_low': [actual values],
#                                                'Shear_high': [actual values],
#                                                'KE': [actual values],
#                                                'TI': [actual values],
#                                                'alpha': [actual values]
#
#                                              } #End of '190'
#
#                                     '300' : {same as for sector 190},
#                                     '330' : {same as for sector 190}
#                                     }# End of 'sectorDict'
#                    }, #End of '89'
#
#             '3' : { Same structure as above
#                    }, #End of '3'
#
#
#             }#End of turbineDict





