from itertools import chain

chained_tuples = chain((1,2,3),(4,5,6))
print chained_tuples
print dir(chained_tuples)

while True:
	try:
		print chained_tuples.next()
	except StopIteration:
		print "Done iterating.."
		break