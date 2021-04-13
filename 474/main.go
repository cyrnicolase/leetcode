package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(findMaxForm([]string{"10", "0001", "111001", "1", "0"}, 5, 3))
	// fmt.Println(findMaxForm([]string{"10", "0", "1"}, 1, 1))
}

func findMaxForm(strs []string, m int, n int) int {
	length := len(strs)
	items := make([]Item, length)
	for i, str := range strs {
		items[i] = NewItem(str)
	}

	// 初始化二维数组来存储所有的结果
	c := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		c[i] = make([]int, n+1)
	}

	for i := 1; i <= length; i++ {
		item := items[i-1]
		for j := m; j >= item.Zero; j-- {
			for k := n; k >= item.One; k-- {
				c[j][k] = max(c[j][k], c[j-item.Zero][k-item.One]+1)
			}
		}
	}
	return c[m][n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Item 字符串转换为对象格式
type Item struct {
	Zero int
	One  int
}

// NewItem ...
func NewItem(str string) Item {
	return Item{
		Zero: strings.Count(str, `0`),
		One:  strings.Count(str, `1`),
	}
}
