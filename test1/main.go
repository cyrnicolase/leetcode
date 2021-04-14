package main

import "fmt"

func main() {
	a := app()
	b := app()
	fmt.Println(a(`go`))  // Hi go
	fmt.Println(b(`all`)) // Hi all
	fmt.Println(a(`go`))  // Hi go
}

func app() func(string) string {
	t := `Hi`
	c := func(b string) string {
		t = t + ` ` + b
		return t
	}
	return c
}

// func main() {
// 	stus := []Student{
// 		{Name: `章三`, Age: 21, Score: 135},
// 		{Name: `里斯`, Age: 25, Score: 143},
// 		{Name: `王武`, Age: 21, Score: 128},
// 		{Name: `赵六`, Age: 18, Score: 138},
// 		{Name: `洛奇`, Age: 25, Score: 118},
// 	}

// 	sort.Slice(stus, func(i, j int) bool {
// 		if stus[i].Age == stus[j].Age {
// 			return stus[i].Score < stus[j].Score
// 		}

// 		return stus[i].Age < stus[j].Age
// 	})

// 	fmt.Println(stus)
// }

// // Student ...
// type Student struct {
// 	Name  string
// 	Age   int
// 	Score int
// }
