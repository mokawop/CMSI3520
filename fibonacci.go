package main
import "fmt"

func main(){
	fib := fibonacci()
	for i := 0; i < 15; i++{
		fmt.Println(fib())
	}
}

func fibonacci() func() int{
	a := 0
	b := 1
	return func() int{
		temp := a
		a, b = b, a + b
		return temp
	}
}
