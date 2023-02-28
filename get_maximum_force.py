import numpy as np
TAG = 'TOTAL-FORCE (eV/Angst)'

if __name__ == "__main__":
    outcarf = open('example/OUTCAR', 'r')
    outcar = outcarf.readlines()
    outcarf.close()
    poscarf = open('example/POSCAR', 'r')
    poscar = poscarf.readlines()
    poscarf.close()
    num_atoms = sum([int(x) for x in poscar[6].split()])
    list_of_tags = []
    for il in range(len(outcar)):
        if TAG in outcar[il]:
            list_of_tags += [il]
    i = list_of_tags[-1]
    if i >= len(outcar) or i+2+num_atoms >= len(outcar):
        i = list_of_tags[-2]
    lines = outcar[i+2:i+2+num_atoms]
    forces = np.array([l.split()[3:6] for l in lines]).astype(np.float64)
    print('Maximum force =', forces.max())
