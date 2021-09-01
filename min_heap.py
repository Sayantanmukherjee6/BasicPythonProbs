####################################
# Env : python3
# #input:
# coordinate_vectors = [[1,2],[1,5],[3,4],[2,1],[2,5],[3,9],[4,5]]
# search_condition = [2,2]
# int k = 2

# #output:

# output_coordinate= [[1,2],[2,1]]
#####################################

import heapq.math


class Heap(object):

    def __init__(self,k):
        """ create a new min-heap. """
        self._heap = []
        self.k = k

    def push(self, priority,item):
        """ push items into fixed heap (size k) """
        assert priority >= 0
 
        if len(self._heap)< self.k:
            heapq.heappush(self._heap, (priority,item))
        else:
            r = heapq.heappop(self._heap)
            q = heapq.heappop(self._heap)
            if priority <= r[0] and priority <= q[0] and r[0] <= q[0]:
                heapq.heappush(self._heap, (priority,item))
                heapq.heappush(self._heap, r)
            elif priority <= r[0] and priority <= q[0] and r[0] >= q[0]:
                heapq.heappush(self._heap, (priority,item))
                heapq.heappush(self._heap, q)
            elif priority >= r[0] and priority <= q[0] and r[0] <= q[0]:
                heapq.heappush(self._heap, (priority,item))
                heapq.heappush(self._heap,r)
            elif priority <= r[0] and priority >= q[0] and r[0] >= q[0]:
                heapq.heappush(self._heap, (priority,item))
                heapq.heappush(self._heap,q)
            elif priority >= r[0] and priority >= q[0] and r[0] >= q[0]:
                heapq.heappush(self._heap,r)
                heapq.heappush(self._heap,q)
     
    def pop(self):
        """ Returns the item with lowest priority. """
        item = heapq.heappop(self._heap)[1] # (prio, item)[1] == item
        return item
    
    def k_smallest(self):
        """ returns k smallest integer """
        k_list= heapq.nsmallest(self.k, self._heap)
        return [val[1] for val in k_list]

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        """ Get all elements ordered by asc. priority. """
        return self

    def next(self):
        """ Get all elements ordered by their priority (lowest first). """
        try:
            return self.pop()
        except IndexError:
            raise StopIteration


if __nme__=="__main__": 

	coordinate_vectors = [[1,2],[1,5],[3,4],[2,1],[2,5],[3,9],[4,5]]
	search_condition = [2,2]
	k = 2

	h = Heap(k)
	coord_iter=iter(coordinate_vectors)
	for _ in coordinate_vectors:
	    c=coord_iter.__next__()
	    h.push(math.sqrt(sum([(a - b) ** 2 for a, b in zip(c, search_condition)])),c)

	print (h.k_smallest())