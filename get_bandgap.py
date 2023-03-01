import numpy as np

if __name__ == "__main__":
    feigenval = open('EIGENVAL', 'r')
    eigenval = feigenval.readlines()
    fdoscar = open('DOSCAR', 'r')
    doscar = fdoscar.readlines()
    fermi = float(doscar[5].split()[3])
    info = eigenval[5].split()
    num_points = int(info[2])
    num_bands = int(info[1])

    VB = []
    CB = []

    for b in range(num_bands):
        vals = eigenval[7 + (num_points+2)* b:7 + (num_points+2)*(b+1)]
        vals = vals [1:-1]
        vals = np.array([v.split() for v in vals])[:,1].astype(np.float64)
        VB += [vals[vals <= fermi]]
        CB += [vals[vals > fermi]]

    CBM = min([x[0] for x in CB])
    VBM = max([x[-1] for x in VB])
    bandgap = CBM - VBM
    print(bandgap)
