def insertion_sort(bucket):
	for i in range(1, len(bucket)):
		key = bucket[i]
		j = i - 1

		while j >= 0 and bucket[j]["measurement"] < key["measurement"]:
			bucket[j + 1] = bucket[j]
			j -= 1

		bucket[j + 1] = key

	return bucket
