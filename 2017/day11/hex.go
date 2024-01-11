package hex

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func ImportData(path string) []string {
	readfile, _ := os.Open(path)
	defer readfile.Close()
	scanlines := bufio.NewScanner(readfile)

	scanlines.Split(bufio.ScanLines)

	for scanlines.Scan() {
		line := scanlines.Text()
		split := strings.Split(line, ",")
		return split
	}
	return nil
}

func ShortestHexPath(input []string) {
	var x, y, z float64

	for _, step := range input {
		switch step {
		case "n":
			x--
			y++
		case "s":
			x++
			y--
		case "ne":
			y++
			z++
		case "sw":
			y--
			z--
		case "nw":
			x--
			z--
		case "se":
			x++
			z++
		}
	}

	distance := (math.Abs(x) + math.Abs(y) + math.Abs(z)) / 2
	fmt.Println(distance)
}
