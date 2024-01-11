package plumb

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ImportData(path string) map[int][]int {
	readfile, _ := os.Open(path)

	defer readfile.Close()

	scanlines := bufio.NewScanner(readfile)

	scanlines.Split(bufio.ScanLines)

	progs := make(map[int][]int)

	for scanlines.Scan() {
		line := scanlines.Text()
		split := strings.Split(line, " <-> ")
		key := split[0]
		convkey, _ := strconv.Atoi(key)
		vals := split[1]
		vallist := strings.Fields(vals)
		intvals := make([]int, 0)
		for _, val := range vallist {
			commdown := strings.ReplaceAll(val, ",", "")
			convval, _ := strconv.Atoi(commdown)
			intvals = append(intvals, convval)

		}
		progs[convkey] = intvals

	}

	return progs
}

func GenerateLinks(progs map[int][]int) int {
	count := 0
	toCheck := []int{0}
	checked := make(map[int]bool)

	for len(toCheck) > 0 {
		//pull from the list of items to check
		inspect := toCheck[0]
		//see if we've seen it before
		_, ok := checked[inspect]
		//if we haven't seen it before, add it's components to the toCheck
		if !ok {
			toCheck = append(toCheck, progs[inspect]...)
			checked[inspect] = true
		}
		//remove what we just checked
		if len(toCheck) >= 1 {
			toCheck = toCheck[1:]
		} else {
			toCheck = []int{}
		}

	}

	for key, _ := range checked {
		fmt.Println(key)
		count++
	}

	return count
}
