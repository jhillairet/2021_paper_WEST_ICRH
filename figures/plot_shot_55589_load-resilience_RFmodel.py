# -*- coding: utf-8 -*-
"""
Reproducing the load tolerance curve obtained from WEST shot #55589

@author: J.Hillairet
"""
#%% import
from matplotlib.pylab import *
import numpy as np
from pppat.control_room.signals import *

from west_ic_antenna import *

#%% pulse
pulse = 55589

#%%  Fetch experimental data
Ip, t_Ip = get_sig(pulse, signals['Ip'])
nl, t_nl = get_sig(pulse, signals['nl'])

P_IC_tot, t_tot = get_sig(pulse, signals['IC_P_tot'])
P_Q1, t_Q1 = get_sig(pulse, signals['IC_P_Q1'])
P_Q2, t_Q2 = get_sig(pulse, signals['IC_P_Q2'])
P_Q4, t_Q4 = get_sig(pulse, signals['IC_P_Q4'])

Rc_Q1, t_Rc_Q1 = get_sig(pulse, signals['IC_Rc_Q1_avg'])
Rc_Q2, t_Rc_Q2 = get_sig(pulse, signals['IC_Rc_Q2_avg'])
Rc_Q4, t_Rc_Q4 = get_sig(pulse, signals['IC_Rc_Q4_avg'])

R_IC, t_R_IC = get_sig(pulse, signals['IC_Positions'])
Rext, t_Rext = get_sig(pulse, signals['Rext_median'])

VSWR_Q1_l, t_VSWR_Q1_l = get_sig(pulse, signals['IC_VSWR_Q1_left'])
VSWR_Q1_r, t_VSWR_Q1_r = get_sig(pulse, signals['IC_VSWR_Q1_right'])
VSWR_Q2_l, t_VSWR_Q2_l = get_sig(pulse, signals['IC_VSWR_Q2_left'])
VSWR_Q2_r, t_VSWR_Q2_r = get_sig(pulse, signals['IC_VSWR_Q2_right'])
VSWR_Q4_l, t_VSWR_Q4_l = get_sig(pulse, signals['IC_VSWR_Q4_left'])
VSWR_Q4_r, t_VSWR_Q4_r = get_sig(pulse, signals['IC_VSWR_Q4_right'])

_Rc_Q1, _ = in_between(Rc_Q1, t_Rc_Q1, 7.0, 8 )
_Rc_Q2, _ = in_between(Rc_Q2, t_Rc_Q2, 5.5, 6.0)
_Rc_Q4, _ = in_between(Rc_Q4, t_Rc_Q4, 7.0, 8 )
_VSWR_Q1_l, _ = in_between(VSWR_Q1_l, t_VSWR_Q1_l, 7.0, 8 )
_VSWR_Q1_r, _ = in_between(VSWR_Q1_r, t_VSWR_Q1_r, 7.0, 8 )
_VSWR_Q2_l, _ = in_between(VSWR_Q2_l, t_VSWR_Q2_l, 5.5, 6.0)
_VSWR_Q2_r, _ = in_between(VSWR_Q2_r, t_VSWR_Q2_r, 5.5, 6.0)
_VSWR_Q4_r, _ = in_between(VSWR_Q4_r, t_VSWR_Q4_r, 7.0, 8 )
_VSWR_Q4_l, _ = in_between(VSWR_Q4_l, t_VSWR_Q4_l, 7.0, 8 )



#%% numerical model
import skrf as rf
from tqdm import tqdm

freqs, _ = get_sig(pulse, signals['IC_Frequencies'])
f_Q4 =  freqs[2]*1e6 # Q4 frequency 

freq = rf.Frequency(f_Q4, f_Q4, npoints=1, unit='Hz')
ant = WestIcrhAntenna(frequency=freq)

Z_load = 0.65 + 30j
Rc_match = 0.8
Z_match = 30 - 6*1j # matching impedance 

ant.load(Rc_match)
C_match = ant.match_both_sides(f_match=f_Q4, z_match=[Z_match, Z_match])

#%%
Rcs = np.linspace(0.4, 1.8, 101) + 0.2j
vswrs = []
for Rc in tqdm(Rcs):
    ant.load(Rc)
    _vswr = ant.vswr_act([1, 1], [0, np.pi], Cs=C_match)
    vswrs.append(_vswr)
vswrs = np.array(vswrs).squeeze()

fig, ax = plt.subplots()
ax.plot(Rcs, vswrs)

#%% Q4 
fig, ax = plt.subplots()
ax.plot(_Rc_Q4, _VSWR_Q4_l, '.', alpha=0.6, label='Q4 - Experimental', color='C2')
# ax.plot(_Rc_Q4, _VSWR_Q4_r, '.', alpha=0.6, label='Q4 right')
ax.plot(Rcs, vswrs[:,0], lw=2, color='k',label=f'Q4 - RF Model')
ax.plot(Rcs, Rcs/Z_load.real, ls='--', color='gray')
ax.text(1.3, 2.1, 'Non Resilient', color='gray', rotation=45)

ax.axhline(2, ls='--', color='darkred')
ax.text(0.8, 2.02, 'SWR Limit', color='darkred')

ax.set_ylim(1, 2.5)
ax.set_xlim(0.35, 2.01)
ax.grid(True, alpha=0.6)
ax.set_xlabel('Rc [$\Omega$]', fontsize=14)
ax.set_ylabel('SWR', fontsize=14)
ax.set_title(r'WEST #55589 ($t\in[7-8]$s)')
ax.legend(fontsize=12)
ax.set_xlim(left=0.4, right=1.8)
ax.plot(Rcs, vswrs, color='k')
fig.tight_layout()

#%%
fig.savefig('WEST_ICRH_55589_load_resilience_Q4.png', dpi=150)
