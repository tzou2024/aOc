package dance

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func CreatePrograms() []string {
	programs := strings.Split("abcdefghijklmnop", "")
	return programs
}

func Spin(p []string, n int) []string {
	for i := 0; i < n; i++ {
		p = append([]string{p[len(p)-1]}, p[:len(p)-1]...)

	}
	return p
}

func Exchange(p []string, a, b int) []string {
	p[b], p[a] = p[a], p[b]
	return p
}

func Partner(p []string, a, b string) []string {
	var inda, indb int

	for ind, val := range p {
		if val == a {
			inda = ind
		}
		if val == b {
			indb = ind
		}
	}

	p[inda], p[indb] = p[indb], p[inda]

	return p

}

func LoadDirs(path string) []string {
	file, _ := os.Open(path)
	defer file.Close()

	lines := bufio.NewScanner(file)

	lines.Scan()

	output := strings.Split(lines.Text(), ",")
	return output
}

func OperateDirs(p []string, dirs []string) string {
	for _, val := range dirs {
		leftover := val[1:]
		switch string(val[0]) {
		case "s":
			spinnumb, _ := strconv.Atoi(leftover)
			p = Spin(p, spinnumb)
		case "x":
			prepost := strings.Split(leftover, "/")
			a, _ := strconv.Atoi(prepost[0])
			b, _ := strconv.Atoi(prepost[1])
			p = Exchange(p, a, b)
		case "p":
			prepost := strings.Split(leftover, "/")
			p = Partner(p, prepost[0], prepost[1])

		}

	}
	return strings.Join(p, "")
}
