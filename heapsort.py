import heapq

#returns different list 
#returns smallest-to-largest
#seems to work fine for lexicographic ordering too
#O(nlogn)
def heapsort(list) :
    middlelist = []
    sortedlist = []
    heapq.heapify(middlelist)
    for element in list :
        heapq.heappush(middlelist,element)
    while len(middlelist) > 0 :
        sortedlist.append(heapq.heappop(middlelist))
    return sortedlist