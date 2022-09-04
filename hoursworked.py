h = list(map(int,input('Type hour/week : ').split()))
w = list(map(int,input('Type week : ').split()))
worked = list(map(str,input('Type name [worked,"pay/hour"]-example:"Eric,1.5" : ').split()))
for i in range(len(h)):
    index = worked[i].index(',')
    print(worked[i][0:index] + ' made ' + str(int(h[i]*w[i]*float(worked[i][index+1:]))) + ' silver in ' + str(int(h[i]*w[i])) + ' hours')
    
    