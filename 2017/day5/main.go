package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func processData(path string) []int {
	readfile, err := os.Open(path)
	if err != nil {
		fmt.Println(err)
	}

	scanlines := bufio.NewScanner(readfile)

	scanlines.Split(bufio.ScanLines)

	var maze []int

	for scanlines.Scan() {
		convert, err := strconv.Atoi(scanlines.Text())
		if err != nil {
			fmt.Println("conversion error: ", err)
		}
		maze = append(maze, convert)
	}
	return maze

}

func checkbounds(max, cur int) bool {
	return 0 <= cur && cur < max
}

func escapecount(maze []int) int {
	step := 0
	max := len(maze)
	currind := 0
	for checkbounds(max, currind) {
		currval := maze[currind]
		maze[currind] += 1
		currind += currval
		step += 1
	}
	return step
}

func main() {
	maze := processData("input.txt")
	fmt.Println(maze)
	fmt.Println(escapecount(maze))
}
