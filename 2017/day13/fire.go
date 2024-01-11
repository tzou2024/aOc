package fire

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type scanner struct {
	srange int
	strack int
	sdir   int
}

func NewScanner(r int) *scanner {
	return &scanner{r, 0, 1}
}

func (s *scanner) Inc() {
	if s.strack == 0 {
		s.sdir = 1
	} else if s.strack >= s.srange-1 {
		s.sdir = -1
	}
	s.strack = s.strack + s.sdir
}

func CreateFirewall(path string) *System {
	readfile, _ := os.Open(path)

	defer readfile.Close()

	scanlines := bufio.NewScanner(readfile)

	scanlines.Split(bufio.ScanLines)

	layers := make(map[int]int)

	max := 0

	for scanlines.Scan() {
		text := strings.Fields(scanlines.Text())

		fmt.Println(text)

		key := strings.ReplaceAll(text[0], ":", "")

		val := text[1]

		keyint, _ := strconv.Atoi(key)

		valueint, _ := strconv.Atoi(val)

		layers[keyint] = valueint

		if keyint > max {
			max = keyint
		}
	}

	firewall := make([]*scanner, 0)
	fmt.Println("max ", max)
	for i := 0; i <= max; i++ {
		rangy, ok := layers[i]
		if ok {
			firewall = append(firewall, NewScanner(rangy))
		} else {
			firewall = append(firewall, NewScanner(0))
		}
	}
	return &System{Firewall: firewall, Packet: -1}
}

type System struct {
	Firewall []*scanner
	Packet   int
}

func (s *System) step() int {
	// each step, packet moves first, then layers move
	s.Packet = s.Packet + 1
	severity := 0

	fmt.Println("packet stepping into: ", s.Packet)
	fmt.Println("layer atm: ", s.Firewall[s.Packet].strack, "of", s.Firewall[s.Packet].srange)

	//if it's moved into and gotten caught, count its severity
	if s.Firewall[s.Packet].strack == 0 {
		if s.Firewall[s.Packet].srange != 0 {
			fmt.Println("caught", s.Packet)
			severity += s.Packet * s.Firewall[s.Packet].srange
		}

	}

	//take a step
	for i := 0; i < len(s.Firewall); i++ {
		s.Firewall[i].Inc()
	}
	return severity
}

func (s *System) Cycle() int {
	totalseverity := 0
	for i := 0; i < len(s.Firewall); i++ {
		totalseverity += s.step()
	}
	return totalseverity
}
