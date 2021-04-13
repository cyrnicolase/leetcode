package main

import (
	"fmt"
	"sort"
)

func main() {
	// fmt.Println(findMinArrowShots([][]int{
	// 	{10, 16},
	// 	{2, 8},
	// 	{1, 6},
	// 	{7, 12},
	// }))

	// fmt.Println(findMinArrowShots([][]int{
	// 	{1, 2},
	// 	{3, 4},
	// 	{5, 6},
	// 	{7, 8},
	// }))

	// fmt.Println(findMinArrowShots([][]int{
	// 	{3, 9}, {7, 12}, {3, 8}, {6, 8}, {9, 10}, {2, 9}, {0, 9}, {3, 9}, {0, 6}, {2, 8},
	// }))

	fmt.Println(findMinArrowShots([][]int{
		{9, 12}, {1, 10}, {4, 11}, {8, 12}, {3, 9}, {6, 9}, {6, 7},
	}))
}

func findMinArrowShots(points [][]int) int {
	length := len(points)
	balloons := make([]Balloon, length)
	for i, p := range points {
		balloons[i] = NewBalloon(p)
	}

	sort.Slice(balloons, func(i, j int) bool {
		if balloons[i].Start < balloons[j].Start {
			return true
		}
		if balloons[i].Start > balloons[j].Start {
			return false
		}

		return balloons[i].End < balloons[j].End
	})

	// 查询交集
	// count := 1
	// for i, j, end := 0, 1, balloons[0].End; i < length && j < length; j++ {
	// 	// 两个求有重叠，不用新箭
	// 	if end >= balloons[j].Start {
	// 		if balloons[j].End < end {
	// 			end = balloons[j].End
	// 		}

	// 		continue
	// 	}
	// 	count++
	// 	i = j
	// 	end = balloons[i].End
	// }

	count, end := 1, balloons[0].End
	for i := 1; i < length; i++ {
		if balloons[i].Start <= end {
			if balloons[i].End < end {
				end = balloons[i].End
			}
			continue
		}
		count++
		end = balloons[i].End
	}

	return count
}

// Balloon ...
type Balloon struct {
	Start int
	End   int
}

// NewBalloon ...
func NewBalloon(a []int) Balloon {
	return Balloon{
		Start: a[0],
		End:   a[1],
	}
}
