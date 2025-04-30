package codes

type Interface[K any] interface {
	Len() int
	Less(i, j int) bool
	Push(item K)
	Swap(i, j int)
}

func Heappush[K any](heap Interface[K], item K) {
	heap.Push(item)
	heapify_up(heap, 0, heap.Len()-1)
}

func heapify_up[K any](heap Interface[K], startPos, lastPos int) {
	for lastPos > startPos {
		parentpos := _parent(lastPos)
		if heap.Less(lastPos, parentpos) {
			heap.Swap(lastPos, parentpos)
			lastPos = parentpos
			continue
		}
		break
	}
}

func _left(i int) int {
	return 2*i + 1
}

func _rigth(i int) int {
	return 2*i + 2
}

func _parent(i int) int {
	return (i - 1) >> 1
}
