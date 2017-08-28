import sys
import csv
import vatnumber

if vatnumber.check_vies(sys.argv[1]) == True:
	print sys.argv[1] + "\tZweryfikowane"
else:
	print sys.argv[1] + "\tNie zweryfikowane"
