package main

import "fmt"

func main() {
	fmt.Println(canPartition([]int{1, 5, 11, 5}))
}

func canPartition(nums []int) bool {
	// 判断是否可以被2 整除
	sum := 0
	for _, k := range nums {
		sum += k
	}
	if sum%2 != 0 {
		return false
	}

	// 和的计算值
	max := sum / 2
	// 元素的数量
	length := len(nums)

	var c [][]int
	c = make([][]int, length+1)
	for i := 0; i <= length; i++ {
		c[i] = make([]int, max+1)
	}

	for i := 1; i <= length; i++ {
		for j := max; j >= 1; j-- {
			w := nums[i-1] // 重量和价值相等
			v := nums[i-1]
			if w > j { // 放不下
				c[i][j] = c[i-1][j]
			} else {
				c[i][j] = calcMax(c[i-1][j], c[i-1][j-w]+v)
				if c[i][j] == max { // 可以提前返回
					return true
				}
			}
		}
	}

	// 以上就能够得到将放入i物品，容量为j 的价值整体情况
	// 然后逐个遍历，看看有哪一个价值是等于max 的

	// for i := 0; i <= length; i++ {
	// 	fmt.Println(c[i])
	// }

	// for i := 1; i <= length; i++ {
	// 	for j := 1; j <= max; j++ {
	// 		if c[i][j] == max {
	// 			return true
	// 		}
	// 	}
	// }

	return false
}

func calcMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}
