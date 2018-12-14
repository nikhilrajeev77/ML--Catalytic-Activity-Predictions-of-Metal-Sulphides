from ase.io import read,write
import glob

for name in glob.glob('*.traj'):
    a=read(name)
    a=a.repeat((2,2,1))
    a.write(name[0:-5]+'.xyz')
