package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func importData(path string) []int {
	readFile, err := os.Open(path)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	fmt.Println(fileLines[0])

	intlist := make([]int, len(fileLines[0]))

	for ind, val := range fileLines[0] {
		z, _ := strconv.Atoi(string(val))
		intlist[ind] = z

	}

	readFile.Close()
	fmt.Println(intlist)

	return intlist
}

func sum(s []int, c chan int) {
	sum := 0
	for i, v := range s {
		trui := s[(i+1)%len(s)]
		if trui == v {
			sum += v
		}
	}
	c <- sum
}

func main() {
	intlist := importData("input.txt")
	c1 := make(chan int)
	c2 := make(chan int)

	go sum(intlist[len(intlist)/2:], c1)
	go sum(intlist[:len(intlist)/2], c2)
	x, y := <-c1, <-c2

	fmt.Println(x, y, x+y)
}
