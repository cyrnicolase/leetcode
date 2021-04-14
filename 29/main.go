package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(divide(-7, -3))
	fmt.Println(divide(-16, 8))
	fmt.Println(divide(16, -5))
	fmt.Println(divide(8, -3))
	fmt.Println(divide(-1, -1))
	fmt.Println(divide(0, -1))
	fmt.Println(divide(-2147483648, -1))
	fmt.Println(divide(2147483648, -1))
}

func divide(dividend int, divisor int) int {
	// 同符号类型
	mark := (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0)
	de := math.Abs(float64(dividend))
	di := math.Abs(float64(divisor))

	dividend = int(de)
	divisor = int(di)
	n := 0
	for dividend >= divisor {
		count, d := 1, divisor
		for dividend >= (d << 1) {
			d = d << 1
			count = count << 1
		}

		n += count
		dividend -= d
	}

	if mark {
		if n > 2147483647 {
			return 2147483647
		}
		return n
	}

	return -n
}
