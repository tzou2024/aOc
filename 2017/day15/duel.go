package duel

import (
	"strconv"
	"strings"
)

type Generator struct {
	A_last  int
	B_last  int
	a_start int
	b_start int
	a_fac   int
	b_fac   int
}

func NewGenerator(a_start, b_start int) *Generator {
	a_fac := 16807
	b_fac := 48271

	return &Generator{-1, -1, a_start, b_start, a_fac, b_fac}
}

func (g *Generator) Generate(numb int) int {
	mod := 2147483647

	match := 0

	var a_prev, b_prev int

	for i := 0; i < numb; i++ {
		if g.A_last == -1 {
			a_prev = g.a_start
			b_prev = g.b_start
		} else {
			a_prev = g.A_last
			b_prev = g.B_last
		}

		next_a := (a_prev * g.a_fac) % mod
		next_b := (b_prev * g.b_fac) % mod

		a_bin := strconv.FormatInt(int64(next_a), 2)
		b_bin := strconv.FormatInt(int64(next_b), 2)
		a_fill := 16 - len(a_bin)
		b_fill := 16 - len(b_bin)

		if a_fill > 0 {
			// fmt.Println(a_fill, b_fill)
			a_bin = strings.Repeat("0", a_fill) + a_bin
		} else {
			a_bin = a_bin[len(a_bin)-16:]
		}

		if b_fill > 0 {
			b_bin = strings.Repeat("0", b_fill) + b_bin
		} else {
			b_bin = b_bin[len(b_bin)-16:]
		}

		// fmt.Println(a_bin)
		// fmt.Println(b_bin, len(b_bin))

		if a_bin == b_bin {
			match++
		}

		g.A_last = next_a
		g.B_last = next_b
	}
	return match
}
