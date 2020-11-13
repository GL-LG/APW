#!/usr/bin/python
# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *

for n,m in mdb.models.items():
    # 完全弹性材料，样例Q235钢
    m.Material(name='Q235')
    m.materials['Q235'].Elastic(table=((220000.0, 0.3), ))
    # 弹塑性材料，样例聚乙烯
    m.Material(name='JUYIXI')
    m.materials['JUYIXI'].Elastic(table=((660.0, 0.46), ))
    # 塑性
    m.materials['JUYIXI'].Plastic(table=((15.0, 0.0), 
                                         (16.25, 0.006), 
                                         (17.8125, 0.016), 
                                         (18.75, 0.028), 
                                         (20.0, 0.038), 
                                         (21.25, 0.056), 
                                         (26.25, 0.174), 
                                         (28.125, 0.226)))
    # 创建实体截面
    m.HomogeneousSolidSection(name='SecQ235', 
          material='Q235', thickness=None)
    m.HomogeneousSolidSection(name='juyixi', 
          material='JUYIXI', thickness=None)
 