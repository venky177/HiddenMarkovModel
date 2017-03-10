import sys
from collections import Counter

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

fname=sys.argv[1]#"trydata.txt"
dataFilePointer=open(fname,'r').read().strip().replace("\n"," ").split(" ")
observations=dict(Counter(dataFilePointer))
tags=set(Counter([x[-2:] for x in dataFilePointer]))
print observations
print tags
test="time flies like an arrow"
print baseline(test.split(" "))