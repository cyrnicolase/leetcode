package main

import "fmt"

func main() {
	fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 9))
	// fmt.Println(search([]int{-1, 0, 3, 5, 9, 12}, 2))
	fmt.Println(search([]int{1}, 1))

}

func search(nums []int, target int) int {
	low := 0
	high := len(nums)

	for low < high {
		mid := (high + low) >> 1
		if nums[mid] == target {
			return mid
		}
		if nums[mid] > target {
			high = mid
			continue
		}
		low = mid + 1
	}

	return -1
}
