package codes

type Interface[K any] interface {
	Len() int
	Less(i, j int) bool
	Push(item K)
	Swap(i, j int)
	Pop() (K, error)
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
func Heappop[K any](heap Interface[K]) (K, error) {
	if heap.Len() <= 1 {
		return heap.Pop()
	}
	heap.Swap(0, heap.Len()-1)
	result, err := heap.Pop()
	heapify_down(heap, 0)
	return result, err

}

func heapify_down[K any](heap Interface[K], pos int) {
	for {
		left := _left(pos)
		right := _right(pos)
		smallest := pos

		if left < heap.Len() && heap.Less(left, smallest) {
			smallest = left
		}
		if right < heap.Len() && heap.Less(right, smallest) {
			smallest = right
		}

		if smallest == pos {
			break
		}
		heap.Swap(pos, smallest)
		pos = smallest
	}
}

func _left(pos int) int {
	return 2*pos + 1
}

func _right(pos int) int {
	return 2*pos + 2
}

func _parent(pos int) int {
	return (pos - 1) >> 1
}
