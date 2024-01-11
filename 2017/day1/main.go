package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
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
		// fmt.Println(len(fileScanner.Text()))
		fileLines = append(fileLines, fileScanner.Text())
	}

	// fmt.Println(fileLines[0])

	intlist := make([]int, len(fileLines[0]))

	for ind, val := range fileLines[0] {
		z, _ := strconv.Atoi(string(val))
		intlist[ind] = z

	}

	// fmt.Println(len(intlist))

	readFile.Close()
	// fmt.Println(intlist)

	return intlist
}

func getcompare(path1, path2 string) {
	readFile, _ := os.Open(path1)
	scanlines := bufio.NewScanner(readFile)
	scanlines.Split(bufio.ScanLines)
	checker := make(map[string]bool)
	for scanlines.Scan() {
		strl := strings.Fields(scanlines.Text())
		checker[strl[0]] = true

	}
	readFile.Close()
	readFile, _ = os.Open(path2)
	scanlines = bufio.NewScanner(readFile)
	scanlines.Split(bufio.ScanLines)
	for scanlines.Scan() {
		strl := strings.Fields(scanlines.Text())
		_, ok := checker[strl[0]]
		if !ok {
			fmt.Println(strl[0])
		}
	}
}

func valret(intlist []int, ind int, val int, som *incrementer, wg *sync.WaitGroup) {

	nextind := (ind + 1) % len(intlist)

	if intlist[nextind] == val {
		// fmt.Println(ind, val)
		// fmt.Println(val)
		som.Add(val)
	}
	wg.Done()
}

type incrementer struct {
	sync.Mutex
	i int
}

func (i *incrementer) Add(n int) {
	i.Lock()
	defer i.Unlock()
	i.i += n
}

func main() {
	intlist := importData("input.txt")

	sum := incrementer{sync.Mutex{}, 0}

	var wg sync.WaitGroup
	wg.Add(len(intlist))
	// wg.Add(1)
	for ind, val := range intlist {
		go valret(intlist, ind, val, &sum, &wg)
	}
	wg.Wait()
	// time.Sleep(2 * time.Second)

	fmt.Println(sum.i)
	// getcompare("straightmatching.txt", "asyncmatching.txt")
}
