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
	ints := make([]int, 0)
	for scanlines.Scan() {
		list := scanlines.Text()
		for _, val := range list {
			conv, _ := strconv.Atoi(string(val))
			ints = append(ints, conv)
		}
	}
	return ints
}

func getSum(ints []int) int {
	sum := 0
	for ind, val := range ints {
		nextind := (ind + 1) % len(ints)
		if ints[nextind] == val {
			fmt.Println(ind, val)
			sum += val
		}
	}
	return sum
}

func main() {
	ints := processData("input.txt")
	fmt.Println(getSum(ints))
}
