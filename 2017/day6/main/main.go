package main

import (
	"bank"
	"flag"
)

func main() {
	var svar string
	flag.StringVar(&svar, "input", "main/input.txt", "input path of file")
	flag.Parse()
	banky := bank.ProcessData(svar)
	bank.ProcessBank(banky)

}
