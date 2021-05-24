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
pulse = 55629  # Q4 automatic matching OK


#%%
# Ip, t_Ip = get_sig(pulse, signals['Ip'])
# nl, t_nl = get_sig(pulse, signals['nl'])


# P_IC_tot, t_tot = get_sig(pulse, signals['IC_P_tot'])
# P_Q1, t_Q1 = get_sig(pulse, signals['IC_P_Q4'])
# P_Q2, t_Q2 = get_sig(pulse, signals['IC_P_Q2'])
# P_Q4, t_Q4 = get_sig(pulse, signals['IC_P_Q4'])

# Prad, trad = get_sig(pulse, signals['Prad'])
# Psep, tsep = get_sig(pulse, signals['Separatrix_P'])

# Rc_Q1, t_Rc_Q1 = get_sig(pulse, signals['IC_Rc_Q1_avg'])
# Rc_Q2, t_Rc_Q2 = get_sig(pulse, signals['IC_Rc_Q2_avg'])
Rc_Q4_left, t_Rc_Q4_left = get_sig(pulse, signals['IC_Rc_Q4_left'])
Rc_Q4_right, t_Rc_Q4_right = get_sig(pulse, signals['IC_Rc_Q4_right'])

Q4_left_top, t_Q4_left_top = get_sig(pulse, signals['IC_Capa_Q4_left_upper']) 
Q4_left_bot, t_Q4_left_bot = get_sig(pulse, signals['IC_Capa_Q4_left_lower']) 
Q4_right_top, t_Q4_right_top = get_sig(pulse, signals['IC_Capa_Q4_right_upper']) 
Q4_right_bot, t_Q4_right_bot = get_sig(pulse, signals['IC_Capa_Q4_right_lower']) 

VSWR_Q4_left, t_VSWR_Q4_left = get_sig(pulse, signals['IC_VSWR_Q4_left'])
VSWR_Q4_right, t_VSWR_Q4_right = get_sig(pulse, signals['IC_VSWR_Q4_right'])

Pf_Q4_left, t_Pf_Q4_left = get_sig(pulse, signals['IC_P_Q4_left_fwd'])
Pr_Q4_left, t_Pr_Q4_left = get_sig(pulse, signals['IC_P_Q4_left_ref'])

Rext, t_Rext = get_sig(pulse, signals['Rext_median'])
# R_Q4, t_R_Q4 = get_sig(pulse, signals['IC_Q4_position'])
# ROG
Rog_Q4 = 2949 - Rext

#%%
with plt.style.context('seaborn-paper'):
    fig, ax = plt.subplots(4,1,sharex=True)
    
    # ax[0].plot(t_Pf_Q4_left, Pf_Q4_left)
    # ax[0].plot(t_Pr_Q4_left, Pr_Q4_left)
    
    ax[0].plot(t_Q4_left_top, Q4_left_top, color='k', ls='-', lw=2, label='$C_{top}$')
    ax[0].plot(t_Q4_left_bot, Q4_left_bot, color='k', ls='--', lw=2, label='$C_{bot}$')
    ax[0].set_ylabel('[pF]')
    ax[0].set_title(f'WEST #{pulse} - Q4 (left side)', fontsize=14)
    ax[0].set_xlim(4.05, 6.04)

    ax[1].plot(t_Rext, Rog_Q4, lw=2, label='ROG')
    ax[1].set_ylim(0, 25)
    ax[1].set_ylabel('[mm]')
    
    ax[2].plot(t_Rc_Q4_left, Rc_Q4_left, lw=2, label='$R_c$', color='C2')
    ax[2].set_ylim(0, 3)
    ax[2].set_ylabel('[$\Omega$]')
 
    ax[3].plot(t_VSWR_Q4_left, VSWR_Q4_left, lw=2, label='SWR', color='C2')
    ax[3].set_ylim(1, 1.5)
    ax[3].set_ylabel('')
    
    [a.legend(fontsize=12, ncol=2) for a in ax]
    [a.grid(True, alpha=0.2) for a in ax]
    [a.tick_params(labelsize=12)  for a in ax ]
    ax[-1].set_xlabel('Time [s]', fontsize=14)
    fig.tight_layout()
    fig.subplots_adjust(hspace=0.12)

#%%
fig.savefig(f'WEST_IC_{pulse}_auto_matching.png', dpi=150)




# #%%
# #%%
# # reflectometry timings for average
# ts = [(5.0, 5.4),  # before IC
#       (6.7, 7.0),  # IC ramp up
#       (7.55, 7.75),  # IC plateau
#       (8.2, 8.5),  # IC reduced Rc
#       (8.68, 8.83),  # IC huge reduced Rc
#       ]

# #%%
# data = loadmat(f'../reflectometry/profiles/WEST_{pulse}_prof.mat')


# #%%
# def time_averaged_profile(data, t_start, t_stop):
#     idx_t_start = np.argmin(abs(data['tX'] - t_start -32))
#     idx_t_stop = np.argmin(abs(data['tX'] - t_stop -32))
    
#     ne_mean = np.mean(data['NEX'][:,idx_t_start:idx_t_stop], axis=1)
#     ne_std = np.std(data['NEX'][:,idx_t_start:idx_t_stop], axis=1)
#     r_mean = np.mean(data['RX'][:,idx_t_start:idx_t_stop], axis=1)
#     r_std = np.std(data['RX'][:,idx_t_start:idx_t_stop], axis=1)

#     return r_mean, r_std, ne_mean, ne_std


# # %%
# fig, ax = plt.subplots()

# for (t_start, t_stop) in ts:
#     # ne and r mean, error bar repr with std
#     r, rs, ne, nes = time_averaged_profile(data, t_start, t_stop)
    
#     ax.fill_betweenx(ne, r-rs, r+rs, alpha=.4)
#     ax.plot(r, ne, lw=2, label=f'{t_start}-{t_stop}')


# ax.legend()
# ax.set_yscale('log')
# ax.set_xlim((2.84, 2.98))
# ax.grid(True)
# ax.grid(True, which='minor', alpha=0.5)
# ax.axvline(2.95, color='k')
# ax.set_ylabel('Density [$m^{-3}$]', fontsize=12)
# ax.set_xlabel('Radius [m]', fontsize=12)
# ax.set_title(f'WEST #54903 (LSN, Q1 + Q4)')
             
# #%%
# # plot R(nco) vs time
# nco = 1e19
# Rant = R_IC[2]
# idx_nco = np.argmin(abs(data['NEX'] - 1e19), axis=0)

# Dext = Rant*1e3 - Rext

# Dco = (Rant - data['RX'][idx_nco][0] )* 1e3

# Rc_Q4, t_Rc_Q4 = get_sig(pulse, signals['IC_Rc_Q4_avg'])
# Rc_Q4_left, t_Rc_Q4_left = get_sig(pulse, signals['IC_Rc_Q4_left'])
# Rc_Q4_right, t_Rc_Q4_right = get_sig(pulse, signals['IC_Rc_Q4_right'])

# #%%
# fig, ax = plt.subplots(4,1,sharex=True)
# ax[0].plot(t_Ip, Ip, lw=2)
# ax[1].fill_between(t_Q4, np.squeeze(P_Q1+P_Q2+P_Q4), alpha=0.2, label='Total RF Power')
# ax[1].plot(t_Q1, P_Q1, label='IC Q1', lw=2, color='C0')
# ax[1].plot(t_Q2, P_Q2, label='IC Q2', lw=2, color='C1')
# ax[1].plot(t_Q4, P_Q4, label='IC Q4', lw=2, color='C2')

# ax[2].plot(t_Q1, Rc_Q1, label='IC Q1', lw=2, color='C0')
# ax[2].plot(t_Q2, Rc_Q2, label='IC Q2', lw=2, color='C1')
# ax[2].plot(t_Q4, Rc_Q4, label='IC Q4', lw=2, color='C2')

        
# ax2 = ax[0].twinx()
# ax2.plot(t_nl, nl, lw=2, color='C1')


# ax[0].set_ylabel('Ip [kA]', fontsize=14, color='C0')
# ax2.set_ylabel('nl [$10^{19}$ $m^{-3}$]', fontsize=14, color='C1')
# ax[1].set_ylabel('IC Power [kW]', fontsize=14)
# ax[1].legend(fontsize=12, loc='upper left')
# [a.grid(True, alpha=0.2) for a in ax]
# [a.tick_params(labelsize=14) for a in ax]
# ax[0].tick_params(color='C0', labelcolor='C0')
# ax2.tick_params(color='C1', labelcolor='C1')

# ax[0].set_xlim(-0.1, 12.3)

# ax[0].set_title(f'WEST #{pulse}', fontsize=14)
# fig.tight_layout()

# # Max allowable power

# ax[3].plot(data['tX'].squeeze() - 32, Dco, label='Dco [mm]')
# ax[3].plot(t_Rext, Dext, label='Dext [mm]')

# ax[3].set_xlabel('Time [s]', fontsize=14)
# ax[3].legend()
# ax[3].set_ylim(0, 75)
# fig.tight_layout()
# fig.subplots_adjust(hspace=0)

# #%%
# savefig(f'WEST_IC_{pulse}_Dco.png', dpi=150)






