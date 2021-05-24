# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:50:39 2019

@author: JH218595
"""
#%%
import numpy as np
from matplotlib.pyplot import *
from pppat.control_room.signals import *


#%%
pulse = 55589

# reflectometry timings for average
ts = [(8.81, 8.88), 
      (8.93, 9.00),   
      ]

ts = [(4.07, 4.70),
      (5.57, 6.03),
      (7.09, 7.59),
      (8.58, 9.02),
      (10.08, 10.45)
      ]

# maximum voltages in DFCI
max_Vs = pw.tsmat(pulse, 'AFCI ;+VME_FCI ;V_limite')
max_Is = pw.tsmat(pulse, 'AFCI ;+VME_FCI ;I_limite')

#%%
do_smooth=False
Ip, t_Ip = get_sig(pulse, signals['Ip'])
nl, t_nl = get_sig(pulse, signals['nl'])

P_IC_tot, t_tot = get_sig(pulse, signals['IC_P_tot'], do_smooth)
P_Q1, t_Q1 = get_sig(pulse, signals['IC_P_Q1'], do_smooth)
P_Q2, t_Q2 = get_sig(pulse, signals['IC_P_Q2'], do_smooth)
P_Q4, t_Q4 = get_sig(pulse, signals['IC_P_Q4'], do_smooth)

Prad, trad = get_sig(pulse, signals['Prad'])
Psep, tsep = get_sig(pulse, signals['Separatrix_P'])

# Te, t_Te = get_sig(pulse, signals['Te'])
neutron1, t_neutron1 = get_sig(pulse, signals['Neutron1'])

Rc_Q1, t_Rc_Q1 = get_sig(pulse, signals['IC_Rc_Q1_avg'], do_smooth)
Rc_Q2, t_Rc_Q2 = get_sig(pulse, signals['IC_Rc_Q2_avg'], do_smooth)
Rc_Q4, t_Rc_Q4 = get_sig(pulse, signals['IC_Rc_Q4_avg'], do_smooth)

R_IC, t_R_IC = get_sig(pulse, signals['IC_Positions'])
Rext, t_Rext = get_sig(pulse, signals['Rext_median'])


VSWR_Q1_l, t_VSWR_Q1_l = get_sig(pulse, signals['IC_VSWR_Q1_left'], do_smooth)
VSWR_Q1_r, t_VSWR_Q1_r = get_sig(pulse, signals['IC_VSWR_Q1_right'], do_smooth)
VSWR_Q4_l, t_VSWR_Q4_l = get_sig(pulse, signals['IC_VSWR_Q4_left'], do_smooth)
VSWR_Q4_r, t_VSWR_Q4_r = get_sig(pulse, signals['IC_VSWR_Q4_right'], do_smooth)

VSWR_Q1 = (VSWR_Q1_l + VSWR_Q1_r)/2
VSWR_Q4 = (VSWR_Q4_l + VSWR_Q4_r)/2

Rant, _ = get_sig(pulse, signals['IC_Positions'])
Rant_Q1 = Rant[0]
Rant_Q4 = Rant[2]

#%% corrige valeur de repli pour les figures
Rc_Q4[P_Q4 < 0.1] = 0
Rc_Q1[P_Q1 < 0.1] = 0


#%%
fig, ax = plt.subplots(4,1, sharex=True,  figsize=(6, 5))
ax[0].plot(t_Ip, Ip, lw=2)
ax[0].set_ylabel('Ip [kA]', fontsize=12, color='C0')
ax[0].tick_params(color='C0', labelcolor='C0')
ax[0].set_xlim(-0.1, 13)
ax[0].set_title(f'WEST #{pulse}', fontsize=14)

ax0 = ax[0].twinx()
ax0.plot(t_nl, nl, lw=2, color='C1')
ax0.set_ylabel('nl [$10^{19}$ $m^{-3}$]', fontsize=12, color='C1')
ax0.tick_params(color='C1', labelcolor='C1')

# ax[1].fill_between(t_Q4, (P_Q2+P_Q1+P_Q4)*1e-3, alpha=0.2, label='IC Total')
# ax[1].plot(t_Q1, P_Q1, label='IC Q1', lw=2, color='C0')
# ax[1].plot(t_Q2, P_Q2, label='IC Q2', lw=2, color='C1')
ax[1].plot(t_Q4, P_Q4, label='Coupled Power Q4', lw=2, color='C2')
ax[1].set_ylabel('[MW]', fontsize=12)
ax[1].legend(fontsize=10, loc='upper left', ncol=1)

# ax[2].plot(t_Rc_Q1, Rc_Q1, label=r'$\overline{R}_c$ Q1', color='C0')
ax[2].plot(t_Rc_Q4, Rc_Q4, label=r'$\overline{R}_c$ Q4', color='C2')
ax[2].set_ylabel('[$\Omega$]', fontsize=12)
ax[2].legend(fontsize=12)

# ax[3].plot(t_VSWR_Q1_l, VSWR_Q1, lw=2, label=r'$\overline{VSWR}$ Q1', color='C0')
ax[3].plot(t_VSWR_Q4_l, VSWR_Q4, lw=2, label=r'$\overline{SWR}$ Q4', color='C2')
ax[3].set_ylim(1, 2)
ax[3].set_ylabel('', fontsize=12)
ax[3].legend(fontsize=10)

[a.grid(True, alpha=0.2) for a in ax]
[a.tick_params(labelsize=14) for a in ax]
ax[-1].set_xlabel('Time [s]', fontsize=14)
fig.tight_layout()
fig.subplots_adjust(hspace=0.13)

#%%
for idx, _ts in enumerate(ts):
    ax[0].axvspan(_ts[0], _ts[1], color=f'C2', alpha=0.2)
    ax[1].axvspan(_ts[0], _ts[1], color=f'C2', alpha=0.2)
    ax[2].axvspan(_ts[0], _ts[1], color=f'C2', alpha=0.2)
    ax[3].axvspan(_ts[0], _ts[1], color=f'C2', alpha=0.2)


#%%
fig.savefig(f'WEST_IC_{pulse}_summary_pellet.png', dpi=150)

