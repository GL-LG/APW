#!/usr/bin/python
# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

import os

def iparts (filePath):
    fileList=os.listdir(filePath)
    for i in fileList:
        filedir=os.path.join(filePath, i)       # 获得文件绝对路径
        partn, extension = os.path.splitext(i)  # 获得文件名和后缀
        # 判断文件类型，读取文件
        if extension == ('.stp' or '.STEP'):
            par = mdb.openStep(filedir, scaleFromFile=OFF)
        elif extension == '.igs':
            par=mdb.openIges(filedir, msbo=False, trimCurve=DEFAULT, scaleFromFile=OFF)
        elif extension == '.x_t':
            par=mdb.openParasolid(fileName=filedir, topology=SOLID)
        elif extension == '.sat':
            par = mdb.openAcis(filedir, scaleFromFile=OFF)
        else:
            continue
        # 创建以文件名命名的model
        mdb.Model(name='Model-p'+partn, modelType=STANDARD_EXPLICIT)
        # 按照将部件模型依次导入
        pn, pnum=1, acis.numberOfParts
        while pn <= pnum:
            pp='P'+partn+'-'+str(pn)
            mdb.models['Model-p'+partn].PartFromGeometryFile(name=pp, 
              geometryFile=par, bodyNum=pn, combine=False, dimensionality=THREE_D, 
              type=DEFORMABLE_BODY, scale=1.0)
            pp='P'+partn+'-'+str(pn)
            pn+=1
        print 'Part %s has been imported.'%i
            
if  __name__=='__main__':
    # filePath = ''
    iparts (filePath)