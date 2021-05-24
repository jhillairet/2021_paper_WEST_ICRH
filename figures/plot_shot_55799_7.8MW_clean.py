# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:50:39 2019

@author: JH218595
"""
#%%
import sys
from pppat.control_room.signals import *
import numpy as np
from matplotlib.pyplot import *


#%%
pulse = 55799


#%%
Ip, t_Ip = get_sig(pulse, signals['Ip'])
nl, t_nl = get_sig(pulse, signals['nl'])


P_IC_tot, t_tot = get_sig(pulse, signals['IC_P_tot'])
P_Q1, t_Q1 = get_sig(pulse, signals['IC_P_Q1'])
P_Q2, t_Q2 = get_sig(pulse, signals['IC_P_Q2'])
P_Q4, t_Q4 = get_sig(pulse, signals['IC_P_Q4'])

Prad, trad = get_sig(pulse, signals['Prad'])
Psep, tsep = get_sig(pulse, signals['Separatrix_P'])

#%%
# Te, t_Te = get_sig(pulse, signals['Te'])
neutron1, t_neutron1 = get_sig(pulse, signals['Neutron1'])

#%%
Rc_Q1, t_Rc_Q1 = get_sig(pulse, signals['IC_Rc_Q1_avg'])
Rc_Q2, t_Rc_Q2 = get_sig(pulse, signals['IC_Rc_Q2_avg'])
Rc_Q4, t_Rc_Q4 = get_sig(pulse, signals['IC_Rc_Q4_avg'])

R_IC, t_R_IC = get_sig(pulse, signals['IC_Positions'])
Rext, t_Rext = get_sig(pulse, signals['Rext_median'])

#%%
## interpolate LH and IC power
P_LH_tot, t_LH_tot = get_sig(pulse, signals['LH_P_tot'])
P_LH1, t_LH1 = get_sig(pulse, signals['LH_P_LH1'])
P_LH2, t_LH2 = get_sig(pulse, signals['LH_P_LH2'])

_P_LH_tot = np.interp(t_tot, t_LH_tot, P_LH_tot)
_P_LH1 = np.interp(t_tot, t_LH1, P_LH1)
_P_LH2 = np.interp(t_tot, t_LH2, P_LH2)

# #%%
# fig, ax = plt.subplots(2,1,sharex=True,  figsize=(10, 8.5))
# ax[0].plot(t_Ip, Ip, lw=2)
# ax[0].set_ylabel('Ip [kA]', fontsize=14, color='C0')
# ax[0].tick_params(color='C0', labelcolor='C0')
# ax[0].set_xlim(-0.1, 13)
# ax[0].set_title(f'WEST #{pulse} - Preliminary', fontsize=14)

# ax0 = ax[0].twinx()
# ax0.plot(t_nl, nl, lw=2, color='C1')
# ax0.set_ylabel('nl [$10^{19}$ $m^{-3}$]', fontsize=14, color='C1')
# ax0.tick_params(color='C1', labelcolor='C1')

# ax[1].fill_between(t_Q4, (P_Q1+P_Q2+P_Q4) + _P_LH_tot, alpha=0.2, label='Total RF Power')
# ax[1].plot(t_LH1, P_LH1, label='LH1', lw=2, color='C1')
# ax[1].plot(t_LH2, P_LH2, label='LH2', lw=2, color='C2')
# ax[1].plot(t_Q1, P_Q1, label='IC Q1', lw=2, color='C3')
# ax[1].plot(t_Q2, P_Q2, label='IC Q2', lw=2, color='C4')
# ax[1].plot(t_Q4, P_Q4, label='IC Q4', lw=2, color='C5')


# ax[1].set_ylabel('RF Power [MW]', fontsize=14)
# ax[1].legend(fontsize=12, loc='upper left', ncol=2)

# # ax[2].plot(trad, Prad, lw=2, label='Radiated (total)')
# # ax[2].plot(tsep, Psep, lw=2, label='Separatrix')
# # ax[2].set_ylim(0, 5)
# # ax[2].set_ylabel('Power [MW]', fontsize=14)
# # ax[2].legend(fontsize=12, loc='upper left')

# # ax2 = ax[2].twinx()
# # ax2.plot(t_Te, Te, lw=2, color='C2')
# # ax2.set_ylabel('Te [eV]', fontsize=14, color='C2')
# # ax2.set_ylim(bottom=0)
# # ax2.tick_params(color='C2', labelcolor='C2')

# [a.grid(True, alpha=0.2) for a in ax]
# [a.tick_params(labelsize=14) for a in ax]
# ax[-1].set_xlabel('Time [s]', fontsize=14)

# fig.tight_layout()

# #%%
# fig.savefig(f'WEST_IC_{pulse}.png', dpi=150)



#%%
fig, ax = plt.subplots(1,1,sharex=True,  figsize=(10, 7))
ax.set_xlim(3.3, 12.4)
ax.set_title(f'WEST #{pulse}', fontsize=14)

ax0 = ax.twinx()
ax0.plot(t_nl, nl, lw=2, color='C1')
ax0.set_ylabel('$n_l$ [$10^{19}$ $m^{-3}$]', fontsize=16, color='C1')
ax0.tick_params(color='C1', labelcolor='C1', labelsize=14)

ax.fill_between(t_Q4, (P_Q1+P_Q2+P_Q4)+_P_LH_tot , alpha=0.3, label='Total RF Power')
ax.plot(t_LH1, P_LH1, label='LH1', lw=2, color='C0')
ax.plot(t_LH2, P_LH2, label='LH2', lw=2, color='C2')
ax.plot(t_Q1, P_Q1, label='IC Q1', lw=2, color='C3')
ax.plot(t_Q2, P_Q2, label='IC Q2', lw=2, color='C4')
ax.plot(t_Q4, P_Q4, label='IC Q4', lw=2, color='C5')

ax.set_ylabel('RF Power [MW]', fontsize=14)
# ax.plot(trad, Prad, lw=2, color='k', label='Radiated', alpha=0.5)
# ax[2].plot(tsep, Psep, lw=2, label='Separatrix')
ax.set_ylim(0, 9)
ax.set_ylabel('Power [MW]', fontsize=16)
ax.legend(fontsize=12, loc='upper left', ncol=3)

# ax2 = ax[2].twinx()
# ax2.plot(t_Te, Te, lw=2, color='C2')
# ax2.set_ylabel('Te [eV]', fontsize=14, color='C2')
# ax2.set_ylim(bottom=0)
# ax2.tick_params(color='C2', labelcolor='C2')

ax.grid(True, alpha=0.2) 
ax.tick_params(labelsize=14) 
ax.set_xlabel('Time [s]', fontsize=16)

fig.tight_layout()

#%%
fig.savefig(f'WEST_IC_{pulse}_Power.png', dpi=150)






