package main

import "fmt"

func main() {
	fmt.Println(findTargetSumWays([]int{1, 1, 1, 1, 1}, 3))
}

// 可以理解为部分数之和为： (sum + S)/2
// 即： (sum + S)/ 2 ；剩余的值为： sum - (sum + S)/2 = (sum - S) / 2;
// 所以 (sum + S)/2 - (sum - S)/2 ==> S
func findTargetSumWays(nums []int, target int) int {
	sum := 0
	for _, k := range nums {
		sum += k
	}
	// 全部的和都比 target 小，那么就没办法了； 如果不能被拆分成2 个部分，也没办法
	if sum < target || (sum+target)%2 == 1 {
		return 0
	}

	// 初始化待DP的二维数组
	newTarget := (sum + target) / 2
	length := len(nums)
	c := make([]int, newTarget+1)
	c[0] = 1
	for i := 1; i <= length; i++ {
		w := nums[i-1]
		for j := newTarget; j >= w; j-- {
			// c[j] = c[j] + c[j-w]
			c[j] = max(c[j], c[j-w]+w)
		}
	}

	return c[newTarget]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
