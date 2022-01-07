"""
    Plot model validation results of Warrick 1971
"""
import numpy as np
import matplotlib.pyplot as plt

finput = ''
fout = '../p1-output/'
dim = [1, 20, 10]
dy = 0.1
dz = 0.1
tend = '6000'

savefig = False

fs = 8

"""
    Load data
"""
data = np.genfromtxt(finput + 'frind_results', delimiter=',')

"""
    Load Frehg output
"""

yVec = np.linspace(0, 2.0, dim[1])
zVec = np.linspace(-1.0, 0.0, dim[2])


modl = np.genfromtxt(fout + 'scalar_subs1__' + tend)
modl = np.reshape(modl, (dim[2], dim[1]), order='F')
qy = np.genfromtxt(fout + 'qy_' + tend)
qz = np.genfromtxt(fout + 'qz_' + tend)
qy = np.reshape(qy, (dim[2], dim[1]), order='F')
qz = np.reshape(qz, (dim[2], dim[1]), order='F')

"""
    Make plot
"""
cm = 1.0 / 2.54
fig = plt.figure(1, figsize=[9*cm,7*cm])
ax = fig.gca()
pos1 = ax.get_position()
pos2 = [pos1.x0 + 0.04, pos1.y0+0.03, pos1.width, pos1.height]
ax.set_position(pos2)

plt.contourf(yVec, -zVec, modl/35.7, levels=[0.0,0.25,0.5,0.75,1.0], cmap='jet')

plt.plot(2.0-data[:,0], data[:,1], 'k-')
#
plt.xlim(0,2)
plt.ylim(0,1)
xlabel = [0.0,0.5,1.0,1.5,2.0]
xtick = np.linspace(0,2.0,5)
plt.xticks(xtick,xlabel,fontsize=fs)
ylabel = [-1.0,-0.75,-0.5,-0.25,0.0]
ytick = np.linspace(0,1.0,5)
plt.yticks(ytick,ylabel,fontsize=fs)
plt.xlabel('X [m]', fontsize=fs)
plt.ylabel('Y [m]', fontsize=fs)
plt.text(1.55,0.6,'0.25',fontsize=fs)
plt.text(1.58,0.45,'0.5',fontsize=fs)
plt.text(1.61,0.3,'0.75',fontsize=fs)

if savefig:
    plt.savefig('Fig2.eps', format='eps')


plt.show()
