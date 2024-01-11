package bank

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func ProcessData(path string) []int {
	readFile, err := os.Open(path)
	if err != nil {
		fmt.Println(err)
	}

	scanlines := bufio.NewScanner(readFile)

	scanlines.Split(bufio.ScanLines)
	var bank []int
	for scanlines.Scan() {
		strtxt := scanlines.Text()
		strar := strings.Fields(strtxt)
		for _, val := range strar {
			conv, err := strconv.Atoi(val)
			if err != nil {
				fmt.Println(err)
			}
			bank = append(bank, conv)
		}
	}
	return bank
}

func ProcessBank(bank []int) {
	finalcount := iterate(bank)
	fmt.Println(finalcount)
	// return
}

func getMaxInd(bank []int) int {
	sortedBank := make([]int, 0, len(bank))
	sortedBank = append(sortedBank, bank...)
	sort.Ints(sortedBank)
	// fmt.Println(sortedBank, bank)
	max := sortedBank[len(sortedBank)-1]
	for ind, val := range bank {
		if val == max {
			return ind
		}
	}
	return -1
}

func distribute(bank []int, ind int) []int {
	maxval := bank[ind]
	newbank := make([]int, 0, len(bank))
	newbank = append(newbank, bank...)
	newbank[ind] = 0
	indtracker := (ind + 1) % len(bank)
	for maxval > 0 {
		maxval -= 1
		newbank[indtracker] += 1
		indtracker = (indtracker + 1) % len(bank)
	}
	return newbank

}

func arrayToString(a []int, delim string) string {
	return strings.Trim(strings.Replace(fmt.Sprint(a), " ", delim, -1), "[]")
	//return strings.Trim(strings.Join(strings.Split(fmt.Sprint(a), " "), delim), "[]")
	//return strings.Trim(strings.Join(strings.Fields(fmt.Sprint(a)), delim), "[]")
}

func iterate(bank []int) int {
	//configuration tracker
	configurations := make(map[string]bool)
	cycles := 0

	for {
		fmt.Println(bank)
		_, ok := configurations[arrayToString(bank, ",")]
		if !ok {
			configurations[arrayToString(bank, ",")] = true
			cycles += 1
			maxInd := getMaxInd(bank)
			bank = distribute(bank, maxInd)
		} else {
			return cycles
		}
	}

	// fmt.Println(maxInd)
}
