package main

import (
	"fmt"
	"heap/codes"
)

func main() {
  initialArr := []int{12,312,3,5,345,345,12,3,6,85,46,456,1,23,5,234,7,8}
	arr := IntHeap(initialArr)
	codes.Heappush(&arr, 9)
	codes.Heappush(&arr, 8)
	codes.Heappush(&arr, 7)
	codes.Heappush(&arr, 6)
	codes.Heappush(&arr, 5)
	codes.Heappush(&arr, 4)
	codes.Heappush(&arr, 3)
	codes.Heappush(&arr, 2)
	for {
		value, err := codes.Heappop(&arr)
		if err != nil {
      fmt.Println(err)
			break
		}
		println(value)
	}
}

type IntArrayHeap struct {
	arr []int
}

func (arr *IntArrayHeap) Len() int {
	return len(arr.arr)
}

func (arr *IntArrayHeap) Less(a, b int) bool {
	return arr.arr[a] < arr.arr[b]
}

func (arr *IntArrayHeap) Swap(a, b int) {
	arr.arr[a], arr.arr[b] = arr.arr[b], arr.arr[a]
}
func (arr *IntArrayHeap) Pop() (int, error) {
	if len(arr.arr) == 0 {
		return -1, fmt.Errorf("empty array")
	}
	length := len(arr.arr)
	lastEle := (arr.arr)[length-1]
	arr.arr = arr.arr[:length-1]
	return lastEle, nil
}
func (arr *IntArrayHeap) Push(item int) {
	arr.arr = append(arr.arr, item)

}

func IntHeap(arr []int) IntArrayHeap {
	myHeap := IntArrayHeap{}
	for item := range arr {
		codes.Heappush(&myHeap, arr[item])
	}
	return myHeap
}
