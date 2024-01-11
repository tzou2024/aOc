package main

import (
	"fmt"
	"strproc"
)

func main() {
	text := strproc.ImportData("main/input.txt")
	text = strproc.StripandFormat(text)
	fmt.Println(text)
	fmt.Println("straight: ", strproc.RunningTotal(text))
	fmt.Println("recursed: ", strproc.RecurseFunc(text, 0))
}
