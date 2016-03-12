import csv
import numpy as np
b = open('/Users/bernice/Documents/dc_pums/ss14pdc.csv','rb')
vars = b.next()
dcpums = []

for row in b:
    dcpums.append(row)
    
dcpums = np.array(dcpums)

print "Variables", vars
print "First row of data",dcpums[0]
#sample_size = np.size(dcpums[0::,1].astype(np.float))
print "Number of observations", dcpums.shape
#dcpums.close()
