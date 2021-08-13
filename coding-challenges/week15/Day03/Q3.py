dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
        # made dictionary above
maxval=0
maxkey=''
sum=0
for key,value in dict.items():
    if value>maxval and value%2==1:
        maxval=value
        maxkey=key
				#finding the maximum odd dictionary value
    if value%2==0:
        sum+=value
				#adding all the even values
sumodd=0
for key,value in dict.items():
    if key!=maxkey and value%2==1:
        sumodd+=(value-1)
				#adding all the odd values(doing -1 to make them even) except maximum odd value
return sum+maxval+sumodd