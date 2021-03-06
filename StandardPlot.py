#the standard plot code for generate python-based plot
#update in time
plt.rcParams.update({'font.size': 16})
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif'] = 'Computer Modern'
plt.rcParams['text.usetex'] = 'True'
fig, ax1 = plt.subplots(figsize = [8,6])

#something in between
ax1.set_xlabel(r"Principal quantum number, $n$")
ax1.set_ylabel(r"$\Gamma_{BBR}$ (s$^{-1}$)")
ax1.set_title(r'BBR induced decay rate $\Gamma_{BBR}$, T=30K')


ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth='0.75', color='red')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

GoldenRatio(fig)
fig.savefig('N50_StarkDefect_Up52.pdf',bbox_inches="tight")
