#
# generate.py
#

# Code to generate the file veering_16.csv

assert False

import snappy
import veering

cen = veering.veering_census()

def csv_line(id, veer_sig):
    # id, name, cusps, betti, torsion, volume, chernsimons, tets, hash, triangulation, angles               
    data = [str(id), "veer" + str(id - 1)]
    sig, angles = veer_sig.split('_')
    M = snappy.Manifold(sig)
    data.append(str(M.num_cusps()))
    G = M.homology()
    data.append(str(G.betti_number()))
    torsion = G.elementary_divisors()
    torsion.sort()
    torsion = [e for e in torsion if e != 0]
    torsion = '"' + str(torsion) + '"'
    data.append(torsion)
    data.append(str(M.volume()))
    data.append(str(M.chern_simons()))
    data.append(str(M.num_tetrahedra()))
    data.append(snappy.db_utilities.db_hash(M))
    data.append(sig)
    data.append(angles)
    return ','.join(data) + '\n'

f = open('veering_16.csv', 'w')
f.write('id,name,cusps,betti,torsion,volume,chernsimons,tets,hash,triangulation,angles\n')
for i, sig in enumerate(cen):
    try:
        _ = f.write(csv_line(i+1, sig))
    except:
        print(i, sig)
        break
    if i % 100 == 0: print( i, sig )
f.close()
