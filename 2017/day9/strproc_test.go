package strproc

import (
	"fmt"
)

func ExampleCancelEx() {
	fmt.Println(CancelEx("{}"))
	fmt.Println(CancelEx("{<>}"))
	fmt.Println(CancelEx("{<!>}"))
	fmt.Println(CancelEx("!!>"))
	// Output:
	// {}
	// {<>}
	// {<}
	// >
}

func ExampleStripArrrow() {
	fmt.Println(StripArrrow("<>"))
	fmt.Println(StripArrrow("<random char>"))
	fmt.Println(StripArrrow("<<<<>"))
	//Output:
	//
	//
	//
}

func ExampleSplitParts() {
	fmt.Println(SplitParts("{}{}"))
	fmt.Println(SplitParts("{}{}{}"))
	fmt.Println(SplitParts("{{}}{}{{}}"))
	// Output:
	//[{} {}]
	//[{} {} {}]
	//[{{}} {} {{}}]
}

func ExampleRunningTotal() {
	fmt.Println(RunningTotal("{}"))
	fmt.Println(RunningTotal("{{{}}}"))
	fmt.Println(RunningTotal("{{},{}}"))
	fmt.Println(RunningTotal("{{{},{},{{}}}}"))
	fmt.Println(RunningTotal("{<a>,<a>,<a>,<a>}"))
	fmt.Println(RunningTotal("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
	fmt.Println(RunningTotal("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
	fmt.Println(RunningTotal("{{<a!>},{<a!>},{<a!>},{<ab>}}"))

	// Output:
	// 1
	// 6
	// 5
	// 16
	// 1
	// 9
	// 9
	// 3
}
