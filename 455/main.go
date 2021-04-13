package main

import (
	"fmt"
	"sort"
)

func main() {

	fmt.Println(findContentChildren([]int{1, 2}, []int{1, 2, 3}))
	// fmt.Println(findContentChildren([]int{1, 2, 3}, []int{1, 1}))
}

func findContentChildren(g []int, s []int) int {
	sort.Ints(s)
	sort.Ints(g)

	count, k := 0, 0
	slen := len(s)
	for _, gi := range g {
		for i := k; i < slen; i++ {
			if gi <= s[i] {
				count++
				k = i + 1
				break
			}
		}
	}

	return count
}
