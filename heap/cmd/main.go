package main

import (
	"fmt"
	"heap/codes"
)

func main() {
	arr := IntHeap([]int{})
	codes.Heappush(&arr, 4)
	codes.Heappush(&arr, 3)
	fmt.Println(arr.arr)
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
func (arr *IntArrayHeap) Pop() {

}
func (arr *IntArrayHeap) Push(item int) {
	arr.arr = append(arr.arr, item)

}

func IntHeap(arr []int) IntArrayHeap {
	return IntArrayHeap{arr}
}
