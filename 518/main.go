package main

import "fmt"

func main() {
	// fmt.Print(change(5, []int{1, 2, 5}))
	// fmt.Print(change(3, []int{2}))
	fmt.Print(change(10, []int{10}))
}

// 背包问题，非0、1情况，target在内层循环，且从1开始自增
func change(amount int, coins []int) int {
	if amount == 0 {
		return 1
	}
	if len(coins) == 0 {
		return 0
	}

	c := make([]int, amount+1)
	c[0] = 1
	for i := 1; i <= len(coins); i++ {
		w := coins[i-1]
		for j := w; j <= amount; j++ {
			c[j] = c[j] + c[j-w]
		}
	}

	return c[amount]
}
