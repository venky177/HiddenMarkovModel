import sys,re
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))
def tweaks(words,tags):
    for i in range(0,len(words)):
        tag=tags[i]
        word=words[i]
        if hasNumbers(word) and tag=="/DA":
            tags[i]="/ZZ"

    return words,tags

def veterbi_decode(observation):
    probability={}
    backpointer={}
    initial_state="Q0"
    for q in tags:
        probability[str(q+"-"+"0")]=transitions.get(initial_state+"-"+q)*emmisions.get(observation[0]+"-"+q,1)
        backpointer[str(q+"-"+"0")]=initial_state
    T=len(observation)
    for i in range(1,T):
        for q in tags:
            max_val=-1000
            max_state=""
            for qq in tags:
                running_val=probability[str(qq+"-"+str(i-1))]*transitions[qq+"-"+q]
                if(max_val<running_val):
                    max_val=running_val
                    max_state=qq
            probability[str(q+"-"+str(i))]=max_val*emmisions.get(observation[i]+"-"+q,1)
            backpointer[str(q+"-"+str(i))]=max_state

    #print probability
    #print backpointer

    most_prob_state=""
    max_val=-1000
    for q in tags:
        running_val=probability[str(q+"-"+str(T-1))]
        if(max_val<running_val):
            max_val=running_val
            most_prob_state=q
    back=most_prob_state

    for i in range(T-1,-1,-1):
        back=backpointer[back+"-"+str(i)]
        most_prob_state=back+" /"+most_prob_state

    observation,most_prob_state=tweaks(observation,most_prob_state.split(" ")[1:])
    #print map(lambda a, b: a + b, observation, most_prob_state.split(" ")[1:])
    return " ".join(map(lambda a, b: a + b, observation, most_prob_state))


fname="hmmmodel.txt"
model=open(fname,'r').read().strip().split("\n")

tags=model[1].split(" ")
words=model[3].split(" ")


index=model.index("Emissions_Probability")
tran_tags=model[5].split(" ")[0:]

transitions={}

lines=model[6].split(" ")
for i in range(2,len(tran_tags)+1):
    transitions[str(lines[0]+"-"+tran_tags[i-1])]=float(lines[i-1])

for lines in model[9:index]:
    lines=lines.split(" ")
    for i in range(2,len(tran_tags)+1):
        transitions[str(lines[0]+"-"+tran_tags[i-1])]=float(lines[i-1])

emm_tags=model[index+1].split(" ")[0:]
emmisions={}
for lines in model[index+2:]:
    lines=lines.split(" ")
    for i in range(2,len(emm_tags)+1):
        emmisions[str(lines[0]+"-"+emm_tags[i-1])]=float(lines[i-1])


fname=sys.argv[1]#"trydata.txt"
fname="dev.txt"
dataFilePointer=open(fname,'r').read().strip().split("\n")
writeToFile=""
for line in dataFilePointer:
    ans=veterbi_decode(line.split(" "))
    #print ans
    writeToFile+=ans+"\n"

outfname="hmmoutput.txt"
with open(outfname,"w+") as f:
    f.write(writeToFile)

print "Done"

