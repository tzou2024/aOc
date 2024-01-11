package knot

import "fmt"

func ExampleGenerateSlots() {
	fmt.Println(GenerateSlots(4))
	fmt.Println(GenerateSlots(2))

	// Output:
	// [0 1 2 3 4]
	// [0 1 2]
}

func ExampleFlipSub() {
	testReg := GenerateSlots(4)
	testinput := 3

	fmt.Println(FlipSub(testReg, 0, testinput))
	testinput = 4
	fmt.Println(FlipSub(testReg, 3, testinput))

	// Output:
	// [2 1 0 3 4]
	// [4 3 0 1 2]
}

func ExampleShift() {
	testReg := GenerateSlots(4)
	testinput := []int{3, 4, 1, 5}

	fmt.Println(Shift(testReg, testinput))

	// Output
	// 3 4 2 1 0
}
