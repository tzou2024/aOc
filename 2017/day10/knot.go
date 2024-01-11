package knot

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ProcessInput(path string) []int {
	readfile, _ := os.Open(path)

	defer readfile.Close()

	scanlines := bufio.NewScanner(readfile)

	scanlines.Split(bufio.ScanLines)

	inputs := make([]int, 0)
	for scanlines.Scan() {
		strlist := strings.Fields(scanlines.Text())
		for _, val := range strlist {
			prevonc := strings.ReplaceAll(val, ",", "")
			converted, _ := strconv.Atoi(prevonc)
			inputs = append(inputs, converted)
		}
	}
	return inputs
}

func GenerateSlots(end int) []int {
	ints := make([]int, 0)
	for i := 0; i <= end; i++ {
		ints = append(ints, i)
	}
	return ints
}

func FlipSub(register []int, ind, switchlen int) []int {
	// takes an ind and returns the subsection in reverse order
	torev := make([]int, 0)
	for i := 0; i < switchlen; i++ {
		nextpost := (i + ind) % len(register)
		torev = append(torev, register[nextpost])
	}
	for i, j := 0, len(torev)-1; i < j; i, j = i+1, j-1 {
		torev[i], torev[j] = torev[j], torev[i] // reverse the slice
	}
	for i := 0; i < switchlen; i++ {
		nextPost := (i + ind) % len(register)
		register[nextPost] = torev[i]
	}
	return register
}

func Shift(register, inputs []int) []int {
	ind := 0
	for skip, switchlen := range inputs {
		fmt.Println("shifting: ", skip)
		register = FlipSub(register, ind, switchlen)
		ind = ind + switchlen + skip
	}
	return register
}
