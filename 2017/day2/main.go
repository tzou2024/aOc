package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func importData(path string) [][]int {
	readFile, err := os.Open(path)

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	var filelines [][]int
	for fileScanner.Scan() {
		linestring := fileScanner.Text()

		strar := strings.Fields(linestring)
		var t2 = []int{}
		for _, i := range strar {
			j, _ := strconv.Atoi(i)
			t2 = append(t2, j)
		}
		filelines = append(filelines, t2)
	}
	return filelines

}

func processData(numbs [][]int) int {
	tots := 0
	for _, val := range numbs {
		sort.Ints(val)
		min := val[0]
		max := val[len(val)-1]
		dif := max - min
		tots += dif
	}
	return tots
}
func main() {
	filelines := importData("input.txt")
	fmt.Println(processData(filelines))
}

// func importData(path string) []int {
// 	readFile, err := os.Open(path)

// 	if err != nil {
// 		fmt.Println(err)
// 	}

// 	fileScanner := bufio.NewScanner(readFile)

// 	fileScanner.Split(bufio.ScanLines)

// 	var fileLines []string

// 	for fileScanner.Scan() {
// 		fileLines = append(fileLines, fileScanner.Text())
// 	}

// 	fmt.Println(fileLines[0])

// 	intlist := make([]int, len(fileLines[0]))

// 	for ind, val := range fileLines[0] {
// 		z, _ := strconv.Atoi(string(val))
// 		intlist[ind] = z

// 	}

// 	readFile.Close()
// 	fmt.Println(intlist)

// 	return intlist
// }
