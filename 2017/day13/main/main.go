package main

import (
	"fire"
	"fmt"
)

func main() {
	system := fire.CreateFirewall("main/input.txt")
	fmt.Println(len(system.Firewall))
	fmt.Println(system.Cycle())
}
