import sys
def baseline(observationString):
    ans=""
    for word in observationString:
        max_val=-1000
        max_state=""
        for q in tags:
            running_val=observations.get(word+"/"+q)
            if(max_val<running_val):
                max_val=running_val
                max_state=q
        ans+=word+"/"+max_state+" "
    return ans.strip()

observations=dict()
dataFilePointer=open('hmmmodel.txt','r').read().strip().split("\n")
tags=set(dataFilePointer[0].split(" "))
for line in dataFilePointer[1:]:
    line=line.split(" ")
    observations[line[0]]=float(line[1])

print tags

fname=sys.argv[1]#"trydata.txt"
#fname="dev.txt"
dataFilePointer=open(fname,'r').read().strip().split("\n")
writeToFile=""
for line in dataFilePointer:
    ans=baseline(line.split(" "))
    #print ans
    writeToFile+=ans+"\n"

outfname="hmmoutput.txt"
with open(outfname,"w+") as f:
    f.write(writeToFile)

print "Done"