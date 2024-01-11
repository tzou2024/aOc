package strproc

import (
	"bufio"
	"os"
)

func ImportData(path string) string {
	readFile, _ := os.Open(path)
	defer readFile.Close()
	scanLines := bufio.NewScanner(readFile)
	scanLines.Split(bufio.ScanLines)
	for scanLines.Scan() {
		return scanLines.Text()
	}
	return ""
}

func CancelEx(str string) string {
	tracker := 0
	final := ""
	for tracker < len(str) {
		char := string(str[tracker])
		if char == "!" {
			tracker++
			tracker++
		} else {
			final = final + char
			tracker++
		}
	}
	return final
}

func StripArrrow(str string) string {
	tracker := 0
	final := ""
	for tracker < len(str) {
		char := string(str[tracker])
		if char == "<" {
			tracker++
			for string(str[tracker]) != ">" {
				tracker++
			}
			tracker++
		} else {
			final = final + char
			tracker++
		}
	}
	return final
}

func StripandFormat(str string) string {
	tracker := 0
	final := ""
	str = CancelEx(str)
	str = StripArrrow(str)
	for tracker < len(str) {
		char := string(str[tracker])
		if char == "{" || char == "}" {
			final = final + char
			tracker++
		} else {
			tracker++
		}
	}
	return final
}

func SplitParts(str string) []string {
	stacklist := make([]string, 0)
	depthcounter := 0
	lastdepth := 0
	for ind, val := range str {

		if string(val) == "{" {
			depthcounter++
		} else if string(val) == "}" {
			depthcounter--
		}
		if depthcounter == 0 {
			stacklist = append(stacklist, str[lastdepth:ind+1])
			lastdepth = ind + 1
		}

	}
	return stacklist
}

func RunningTotal(str string) int {
	str = StripandFormat(str)
	depthcounter := 0
	// lastdepth := 0
	total := 0
	for _, val := range str {
		if string(val) == "{" {
			depthcounter++
		} else if string(val) == "}" {
			total += depthcounter
			depthcounter--
		}
	}
	return total
}

func RecurseFunc(str string, prev int) int {

	//base case is empty string
	if len(str) == 0 {
		// fmt.Println(str, "Returning 0")
		return 0
	}
	strlist := SplitParts(str)
	//if there are outer brakcers, strip those and recurse
	if len(strlist) == 1 {
		str = str[1 : len(str)-1]
		newprev := prev + 1
		total := prev + RecurseFunc(str, newprev) + 1
		return total
	} else {
		//other case is if there aren't, and we'd want to
		//split the string into it's subcases and return those
		total := 0
		components := make([]int, 0)
		for _, val := range strlist {
			components = append(components, RecurseFunc(val, prev))
		}
		for _, val := range components {
			total += val
		}
		return total
	}
}
