package main

import (
	"dance"
	"fmt"
)

func main() {
	// program := dance.CreatePrograms()
	dirs := dance.LoadDirs("main/input.txt")
	program := dance.CreatePrograms()

	fmt.Println(dance.OperateDirs(program, dirs))
}
