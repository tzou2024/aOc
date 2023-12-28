package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func loadData(path string) [][]string {
	readfile, err := os.Open(path)

	if err != nil {
		fmt.Println(err)
	}

	scanlines := bufio.NewScanner(readfile)

	scanlines.Split(bufio.ScanLines)

	var readlines [][]string

	for scanlines.Scan() {
		readline := scanlines.Text()
		splitstring := strings.Fields(readline)
		readlines = append(readlines, splitstring)
	}
	return readlines

}

func processData(strs [][]string) int {
	sum := 0
	for _, line := range strs {
		if processLine(line) {
			sum += 1
		}
	}
	fmt.Println(sum)
	return sum
}

func processLine(strlist []string) bool {
	tracker := make(map[string]bool)
	for _, val := range strlist {
		_, ok := tracker[val]
		if !ok {
			tracker[val] = true
		} else {
			return false
		}
	}
	return true
}

func main() {
	dat := loadData("input.txt")
	processData(dat)

}
