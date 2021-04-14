package main

import "fmt"

func main() {
	// fmt.Println(canPlaceFlowers([]int{0}, 1))
	// fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 1))
	// fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 2))
	// fmt.Println(canPlaceFlowers([]int{0, 0, 0}, 2))

	fmt.Println(canPlaceFlowers([]int{0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0}, 6))
}

func canPlaceFlowers(flowerbed []int, n int) bool {
	l := len(flowerbed)
	fc, zeroCount := 0, 0
	head := true
	for i := 0; i < l; i++ {
		if flowerbed[i] == 0 {
			zeroCount++
			continue
		}

		if head {
			zeroCount = zeroCount - 1
		} else {
			zeroCount = zeroCount - 2
		}
		if zeroCount > 0 {
			fc += (zeroCount + 1) / 2
		}
		head = false
		zeroCount = 0
	}
	if head {
		fc += (zeroCount + 1) / 2
	} else if zeroCount > 1 {
		fc += zeroCount / 2
	}

	return fc >= n
}
