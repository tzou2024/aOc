package dance

import "fmt"

func ExampleSpin() {
	program := []string{"a", "b", "c", "d", "e"}
	fmt.Println(Spin(program, 3))

	// Output:
	// [c d e a b]
}

func ExamplePartner() {
	program := []string{"e", "a", "b", "d", "c"}
	fmt.Println(Partner(program, "e", "b"))

	// Ouput:
	// [b a e d c]
}

func ExampleExchange() {
	program := []string{"e", "a", "b", "c", "d"}
	fmt.Println(Exchange(program, 3, 4))

	// Output:
	// [e a b d c]
}
