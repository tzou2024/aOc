package main

import (
	"fmt"
	"knot"
)

func main() {
	inputs := knot.ProcessInput("main/input.txt")
	fmt.Println(inputs)

	register := knot.GenerateSlots(255)

	final := knot.Shift(register, inputs)

	fmt.Println(final)
	fmt.Println(final[0] * final[1])

}
