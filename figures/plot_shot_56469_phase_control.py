# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:50:39 2019

@author: JH218595
"""
#%%
import numpy as np
from matplotlib.pyplot import *
from pppat.control_room.signals import *


pulse = 56469  # phase control is OK


# Ip, t_Ip = get_sig(pulse, signals['Ip'])
# nl, t_nl = get_sig(pulse, signals['nl'])

# P_IC_tot, t_tot = get_sig(pulse, signals['IC_P_tot'])
# P_Q1, t_Q1 = get_sig(pulse, signals['IC_P_Q1'])
P_Q2, t_Q2 = get_sig(pulse, signals['IC_P_Q2'])
# P_Q4, t_Q4 = get_sig(pulse, signals['IC_P_Q4'])

#%%
# Rc_Q1_left, t_Rc_Q1_left = get_sig(pulse, signals['IC_Rc_Q1_left'])
# Rc_Q1_right, t_Rc_Q1_right = get_sig(pulse, signals['IC_Rc_Q1_right'])

# Rc_Q2_left, t_Rc_Q2_left = get_sig(pulse, signals['IC_Rc_Q2_left'])
# Rc_Q2_right, t_Rc_Q2_right = get_sig(pulse, signals['IC_Rc_Q2_right'])

# Rc_Q4_left, t_Rc_Q4_left = get_sig(pulse, signals['IC_Rc_Q4_left'])
# Rc_Q4_right, t_Rc_Q4_right = get_sig(pulse, signals['IC_Rc_Q4_right'])

# Rc_Q1, t_Rc_Q1 = get_sig(pulse, signals['IC_Rc_Q1_avg'])
Rc_Q2, t_Rc_Q2 = get_sig(pulse, signals['IC_Rc_Q2_avg'])
# Rc_Q4, t_Rc_Q4 = get_sig(pulse, signals['IC_Rc_Q4_avg'])

R_IC, t_R_IC = get_sig(pulse, signals['IC_Positions'])
Rext, t_Rext = get_sig(pulse, signals['Rext_median'])

ROG = R_IC.max()*1e3 - Rext
#%%
# phaseQ1, t_phaseQ1 = get_sig(pulse, signals['IC_Phase_Q1'], do_smooth=True) 
phaseQ2, t_phaseQ2 = get_sig(pulse, signals['IC_Phase_Q2'], do_smooth=False) 
# phaseQ4, t_phaseQ4 = get_sig(pulse, signals['IC_Phase_Q4'], do_smooth=True)

#%% 

with plt.style.context('seaborn-paper'):
    fig, ax = plt.subplots(4, 1, sharex=True)
    ax[0].plot(t_Q2, P_Q2, lw=2, color='C1', label='Coupled Power (Q2)')
    ax[0].set_ylabel('[MW]', fontsize=12)
    ax[0].legend(fontsize=10)
    ax[0].set_ylim(0, 0.5)
    
    ax[1].plot(t_Rext, ROG, lw=2, color='k', label='ROG')
    ax[1].set_ylim(10, 25)
    ax[1].set_ylabel('[mm]', fontsize=12)
    ax[1].legend(fontsize=10)
    
    ax[2].plot(t_Rc_Q2, Rc_Q2, label='$R_c$ (Q2)', lw=2, color='C1')
    ax[2].set_ylim(0, 1.3)
    ax[2].set_ylabel('[$\Omega$]', fontsize=12)
    ax[2].legend(fontsize=10)
    
    ax[3].plot(t_phaseQ2, phaseQ2, lw=2, color='C1', label='Toroidal Phase (Q2)')
    ax[3].set_ylim(175, 185)
    ax[3].set_ylabel('[deg]', fontsize=12)
    ax[3].axhline(180, color='gray', ls='--', label='Target')
    ax[3].legend(fontsize=10, ncol=2)
    
    [a.grid(True, alpha=0.2) for a in ax]
    [a.tick_params(labelsize=12) for a in ax]
    ax[0].set_title(f'WEST #{pulse}', fontsize=14)
    ax[-1].set_xlabel('Time [s]', fontsize=12)
    ax[-1].set_xlim(10, 10.6)
    fig.tight_layout()
    fig.subplots_adjust(hspace=0.13)

#%%
fig.savefig(f'WEST_IC_{pulse}.png', dpi=150)
