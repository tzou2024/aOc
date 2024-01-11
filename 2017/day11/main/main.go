package main

import (
	"hex"
)

func main() {
	dirlist := hex.ImportData("main/input.txt")

	hex.ShortestHexPath(dirlist)
}
