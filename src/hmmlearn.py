import sys
from collections import Counter

fname=sys.argv[1]#"trydata.txt"
dataFilePointer=open(fname,'r').read().strip()
observations=Counter(dataFilePointer.replace("\n"," ").split(" "))
#print observations
initial_state="Q0"
lines= ["/Q0 "+ x for x in dataFilePointer.split("\n")]

trans={}
tagCount={}
tagOutBound={}
bagOfWord=set()

prevTag=""
for line in lines:
#    print line
    for words in line.split(" "):
        bagOfWord.add(words[:-3].strip())
        currTag=words[-2:]
#        print currTag

        if prevTag=="":
            prevTag=currTag
            continue

        key = prevTag+"-"+currTag
        trans[key]=trans.get(key,0)+1
        tagOutBound[prevTag]=tagOutBound.get(prevTag,0)+1
        tagCount[currTag]=tagCount.get(currTag,0)+1

        prevTag=currTag
    prevTag=""


bagOfWord.remove("")
'''
print bagOfWord
print trans
print tagCount
print tagOutBound
'''



write_to_file=""
write_to_file+="States\n"
write_to_file+=" ".join(tagCount)+"\n"
write_to_file+="Observations\n"
write_to_file+=" ".join(bagOfWord)+"\n"

print "Initial Probability"
write_to_file+="Initial Probability\n"
row=initial_state
#print "tag "+" ".join([str(x)  for x in set(tagCount)])
write_to_file+="tag "+" ".join([str(x)  for x in set(tagCount)])+"\n"
for tag in set(tagCount):
    row += " "+str(float(trans.get(initial_state+"-"+tag,0))/tagOutBound.get(initial_state,0))
#print row
write_to_file+=row+"\n"

print "\n--------------------------------------------------\n"
write_to_file+="Transitions\n"
#print "tag "+" ".join([str(x)  for x in set(tagCount)])
write_to_file+="tag "+" ".join([str(x)  for x in set(tagCount)])+"\n"
for tag1 in set(tagCount):
    if(tagOutBound.get(tag1,0)!=0):
        row=tag1
        for tag2 in set(tagCount):
            row += " "+str(float(trans.get(tag1+"-"+tag2,0)+1)/(tagOutBound.get(tag1,0)+len(tagCount)))
#        print row
        write_to_file+=row+"\n"

print "\n--------------------------------------------------\n"
write_to_file+="Emissions_Probability\n"
print "tag "+" ".join([str(x)  for x in set(tagCount)])
write_to_file+="tag "+" ".join([str(x)  for x in set(tagCount)])+"\n"
for word in bagOfWord:
    row=word
    for tag in set(tagCount):
        row += " "+str(float(observations.get(word+"/"+tag,0))/tagCount[tag])
#    print row
    write_to_file+=row+"\n"

outfname="hmmmodel.txt"
with open(outfname,"w+") as f:
    f.write(write_to_file)

print "Done"
