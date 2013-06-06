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
    HasTraits, Instance, Button

from etsproxy.traits.ui.api import UItem, View

import platform
import time
if platform.system() == 'Linux':
    sysclock = time.time
elif platform.system() == 'Windows':
    sysclock = time.clock

from aramis_cdt import AramisCDT

class AramisView2D(HasTraits):
    '''This class manages 2D views for AramisCDT variables
    '''

    aramis_cdt = Instance(AramisCDT)

    plot2d = Button
    def _plot2d_fired(self):
        import matplotlib.pyplot as plt
        aramis_cdt = self.aramis_cdt
        plt.figure()
        plt.subplot(2, 2, 1)

        plt.plot(aramis_cdt.x_idx_init.T, aramis_cdt.d_ux_arr.T, color='black')
        plt.plot(aramis_cdt.x_idx_init[0, :], aramis_cdt.d_ux_arr_avg, color='red', linewidth=2)
        y_max_lim = plt.gca().get_ylim()[-1]
        plt.plot(aramis_cdt.x_idx_init[0, :-1], aramis_cdt.crack_filter_avg * y_max_lim,
                 color='magenta', linewidth=1)

        plt.subplot(2, 2, 2)
        plt.plot(aramis_cdt.x_idx_init.T, aramis_cdt.ux_arr.T, color='green')
        plt.plot(aramis_cdt.x_idx_init[0, :], aramis_cdt.ux_arr_avg, color='red', linewidth=2)

        plt.subplot(2, 2, 3)
        plt.plot(aramis_cdt.x_idx_init[0, :], aramis_cdt.dd_ux_arr_avg, color='black')
        plt.plot(aramis_cdt.x_idx_init[0, :], aramis_cdt.ddd_ux_arr_avg, color='blue')
        y_max_lim = plt.gca().get_ylim()[-1]
        plt.plot(aramis_cdt.x_idx_init[0, :-1], aramis_cdt.crack_filter_avg * y_max_lim,
                 color='magenta', linewidth=2)

        plt.subplot(2, 2, 4)
        plt.hist(aramis_cdt.crack_arr, bins=40, normed=True)
        plt.twinx()
        plt.hist(aramis_cdt.crack_arr, normed=True,
                 histtype='step', color='black',
                 cumulative=True, bins=40)

        plt.suptitle(aramis_cdt.aramis_info.basename + '%d' % aramis_cdt.evaluated_step)

        plt.show(block=False)

    view = View(
                UItem('plot2d'),
                )