package register

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func ImportData(path string) int {
	readfile, err := os.Open(path)

	if err != nil {
		log.Fatal(err)
	}
	defer readfile.Close()

	scanlines := bufio.NewScanner(readfile)

	scanlines.Split(bufio.ScanLines)
	reg := make(Register)
	for scanlines.Scan() {
		text := scanlines.Text()
		reg = processline(reg, text)
		// break
	}
	fmt.Println(reg.maxSlotVal())
	return 0
}

type Register map[string]int

func (reg Register) maxSlotVal() int {
	max := 0
	for _, val := range reg {
		if val > max {
			max = val
		}
	}
	return max
}

var compMap = map[string]func(Register, string, int) bool{
	">": func(reg Register, slot string, comp int) bool {
		return reg[slot] > comp
	},
	"<": func(reg Register, slot string, comp int) bool {
		return reg[slot] < comp
	},
	">=": func(reg Register, slot string, comp int) bool {
		return reg[slot] >= comp
	},
	"<=": func(reg Register, slot string, comp int) bool {
		return reg[slot] <= comp
	},
	"==": func(reg Register, slot string, comp int) bool {
		return reg[slot] == comp
	},
	"!=": func(reg Register, slot string, comp int) bool {
		return reg[slot] != comp
	},
}

func processConditional(condStat []interface{}) func(Register, string, int) bool {
	symbol := condStat[1].(string)
	return compMap[symbol]
}

var evalMap = map[string]func(Register, string, int) Register{
	"inc": func(reg Register, slot string, amnt int) Register {
		reg[slot] = reg[slot] + amnt
		return reg
	},
	"dec": func(reg Register, slot string, amnt int) Register {
		reg[slot] = reg[slot] - amnt
		return reg
	},
}

func processEval(evalStat []interface{}) func(Register, string, int) Register {
	symbol := evalStat[1].(string)
	return evalMap[symbol]
}

func processline(reg Register, line string) Register {
	//take in a line and return a function that
	//checks condition and increases
	parts := strings.Fields(line)
	test := []interface{}{}

	amnt, err := strconv.Atoi(parts[2])
	if err != nil {
		fmt.Println(err)
	}

	cond, err := strconv.Atoi(parts[6])
	if err != nil {
		fmt.Println(err)
	}

	test = append(test, parts[0], parts[1], amnt, parts[4], parts[5], cond)

	condparts := test[len(test)-3:]
	evalparts := test[:3]

	// if any slot mentioned in the condition of evaluated is not used hard
	//assign a 0 in that slot
	_, ok := reg[condparts[0].(string)]
	if !ok {
		reg[condparts[0].(string)] = 0
	}
	_, ok = reg[evalparts[0].(string)]
	if !ok {
		reg[evalparts[0].(string)] = 0
	}

	condfunc := processConditional(condparts)
	evalfunc := processEval(evalparts)

	toEval := condfunc(reg, condparts[0].(string), condparts[2].(int))
	if toEval {
		reg = evalfunc(reg, evalparts[0].(string), evalparts[2].(int))
	}
	// fmt.Println(testReg)
	return reg

}
