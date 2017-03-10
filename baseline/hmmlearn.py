import sys
from collections import Counter
fname=sys.argv[1]#"trydata.txt"
dataFilePointer=open(fname,'r').read().strip().replace("\n"," ").split(" ")
observations=dict(Counter(dataFilePointer))
tags=set(Counter([x[-2:] for x in dataFilePointer]))
#print observations
print tags

write_to_file=" ".join(tags)+"\n"
for key,val in observations.iteritems():
    write_to_file+=str(key+" "+str(val)+"\n")

outfname="hmmmodel.txt"
with open(outfname,"w+") as f:
    f.write(write_to_file)

print "Done"
