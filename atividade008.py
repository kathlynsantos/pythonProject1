def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue

nlist = [53,9,25,347,109,69,97,245,299,343,5,89,101,21,73,205,99,329,111,43,351,229,161,39,201,337,15,167,293,555]
insertionSort(nlist)
print(nlist)