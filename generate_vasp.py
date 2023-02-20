import pandas as pd
import os
import numpy as np
from ase.io import read
import sys
path = './'

if __name__ == "__main__":
    cif_file_name = sys.argv[1]
    psuedosFolder = sys.argv[2]

    atom_label_pseudo = pd.read_csv('pseudos.csv', index_col='element')

    file_name = cif_file_name.replace('.cif', '')
    f = path + '/VASP_'+file_name
    cif_file = file_name+'.cif'

    cif = read(path+cif_file)

    print('Generating VASP files for',f)

    os.mkdir(f)

    cif.write(f+'/POSCAR')

    kpoints = 'Sys\n' +\
        '0\n' +\
        'Gamma\n' +\
        '6 6 6\n'
    kpointsf = open(f+'/KPOINTS', 'w')
    kpointsf.write(kpoints)
    kpointsf.flush()
    kpointsf.close()

    l = open(f+'/POSCAR', 'r')
    l = l.readlines()
    l = l[0].split()
    potcar = ""
    for atom_label in l:
        if atom_label in atom_label_pseudo.index:
            atom_label = atom_label_pseudo[atom_label_pseudo.index ==
                                            atom_label].pseudo.values[0]
        atom_potcar = open(
            psuedosFolder + '/PBE/'+atom_label+'/POTCAR')
        atom_potcar = atom_potcar.read()
        potcar += atom_potcar
        potcar_f = open(f+'/POTCAR', 'w')
        potcar_f.write(potcar)

    cif.set_velocities(np.random.random([cif.get_number_of_atoms(), 3])/10)
    l = open(f+'/POSCAR', 'a')
    l.write('\n')
