package main

import (
	"fmt"
	"time"
)

type TargetDummy struct {
	name   string
	health int
	armour int
}

func updateName(n string) {
	n = "wood"
}

func updateNamePtr(n *string) {
	*n = "Wood"
}

func main() {
	fmt.Println("Starting combat...")
	time.Sleep(time.Second)

	scores := []int{3, 4, 5, 6}
	scores = append(scores, 7)
	fmt.Println(scores)

	var x int = 5
	println(x)

	for i, v := range scores {
		fmt.Println(i, v)
	}

	testMap := map[string]int{
		"shrek":  64,
		"shrek2": 64,
		"shrek3": 65,
	}

	fmt.Println(testMap)

	for k, v := range testMap {
		fmt.Println(k, v)
	}

	var shrek string = "Shrek"

	fmt.Printf("%T\n", &shrek)
	updateName(shrek)
	fmt.Println(shrek)
	updateNamePtr(&shrek)
	fmt.Println(shrek)

	T := TargetDummy{armour: 10, health: 100, name: "Dummy"}
	fmt.Println(T)

}
