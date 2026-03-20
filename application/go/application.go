package main

import (
	"fmt"

	"github.com/YoeaKai/leet_code/topic/count_special_triplets"
)

func run() {
	println(count_special_triplets.SpecialTriplets([]int{0, 1, 0, 0}))
}

func main() {
	fmt.Println("----------Start----------")
	run()
	fmt.Println("----------Finish----------")
}
