package main

import (
	"duel"
	"fmt"
)

func main() {
	gen := duel.NewGenerator(703, 516)

	fmt.Println(gen.Generate(40000000))

	// fmt.Println(gen.A_last)
	// fmt.Println(gen.B_last)

}
