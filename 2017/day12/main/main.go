package main

import (
	"fmt"
	"plumb"
)

func main() {
	plumbing := plumb.ImportData("main/input.txt")
	val := plumb.GenerateLinks(plumbing)

	fmt.Println("count", val)
}
