def mergr(li):
    if len(li) > 1:
        mid=len(li)//2
        leftar=li[:mid]
        rightar=li[mid:]
        mergr(leftar)
        mergr(rightar)

        i=j=k=0
        while i < len(leftar) and j < len(rightar):
            if leftar[i] > rightar[j]:
                li[k]=rightar[j]
                j=j+1
                
            else:
                li[k]=leftar[i]
                i=i+1
            k=k+1     

        while i < len(leftar):
            li[k]=leftar[i]
            i=i+1
            k=k+1

        while j < len(rightar):
            li[k]=rightar[j]
            j=j+1
            k=k+1


    return li
