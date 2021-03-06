#-------------------------------------------------------------------------------
#
# Copyright (c) 2012
# IMB, RWTH Aachen University,
# ISM, Brno University of Technology
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in the Spirrid top directory "licence.txt" and may be
# redistributed only under the conditions described in the aforementioned
# license.
#
# Thanks for using Simvisage open source!
#
#-------------------------------------------------------------------------------

from etsproxy.traits.api import \
    HasTraits, Instance

from etsproxy.traits.ui.api import UItem, View

import os

import numpy as np

import platform
import time
if platform.system() == 'Linux':
    sysclock = time.time
elif platform.system() == 'Windows':
    sysclock = time.clock

from aramis_cdt.aramis_info import AramisInfo
from aramis_cdt.aramis_cdt import AramisCDT
from aramis_cdt.aramis_view2d import AramisPlot2D
from aramis_cdt.aramis_view3d import AramisView3D
from aramis_cdt.aramis_ui import AramisUI

from aramis_cdt.report_gen import report_gen

aramis_dir = '/media/data/_linux_data/aachen/Aramis_07_2013/'

specimen_name = os.path.split(os.getcwd())[-1]

data_dir = os.path.join(aramis_dir, specimen_name)

AI = AramisInfo(data_dir=data_dir)
AC = AramisCDT(aramis_info=AI,
               integ_radius=1,
               evaluated_step_idx=203,
               crack_detect_idx=203,
               transform_data=True)

AUI = AramisUI(aramis_info=AI,
                aramis_cdt=AC)

report_gen(AUI)

