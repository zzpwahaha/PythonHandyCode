import seaborn as sns
from matplotlib.colors import LogNorm
from matplotlib.ticker import LogFormatter

plt.rcParams.update({'font.size': 16})
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif'] = 'Computer Modern'
plt.rcParams['text.usetex'] = True
#xv, yv = np.meshgrid(np.linspace(10,210,501),np.linspace(10,210,501))
fig, ax1 = plt.subplots(figsize = [8,6])
data = test
xsns = xv[0,:]
ysns = yv[:,0]
# for logarithm plot
# log_norm = LogNorm(vmin=10**-3, vmax=1)
# cbar_ticks = [10**i for i in range(int(np.floor(np.log10(np.abs(data)).min())),
#                                   int(np.ceil(np.log10(np.abs(data)).max())))]
# ax = sns.heatmap(data,norm = log_norm,
#                   cbar_kws={"ticks": cbar_ticks},
#                   xticklabels=100,
#                   yticklabels = 10, cmap = 'rainbow')

ax = sns.heatmap(np.abs(data),
                 xticklabels = 50, 
                 yticklabels = 50,
                 cmap = 'rainbow')
ax.invert_yaxis()

#set x,y tickslabel
for i in ax.get_xticklabels():
    i.set_text('{:.0f}'.format(xsns[int(i.get_text())]))
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)    
for i in ax.get_yticklabels():
    i.set_text('{:.0f}'.format(ysns[int(i.get_text())]))
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

ax.tick_params(which = 'both',direction = 'in')
ax.tick_params(which = 'both',top=True, right = True)
ax.minorticks_on()

# set on colorbar frames
cbar_ax = fig.axes[-1]
cbar_ax.set_frame_on(True)
# set on the frame of the main plot
for _, spine in ax.spines.items():
    spine.set_visible(True)
# for log cbar add minor ticks label    
#formatter = LogFormatter(labelOnlyBase = False,  
#                         minor_thresholds = (2, 1))
#cbar_ax.yaxis.set_minor_formatter(formatter)     
ax1.set_xlabel(r'')
ax1.set_ylabel(r'')
ax1.set_title(r'')
GoldenRatio(fig)
# fig.savefig(r'.pdf',dpi = 600,bbox_inches="tight")
