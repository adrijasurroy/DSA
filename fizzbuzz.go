// FIZZBUZZ: 
// Given a number n for each integer i in the range from 1 to n inclusive , 
// print one value per line as follows: if i is a multiple of both 3 and 5 print fizzbuzz 
//  if i is a multiple of of 3 but not 5 print fizz 
//  if i is a multiple of 5 but not 3 print Buzz 
//  if i is not a multiple of 3 or 5, print value of i. 
// For this write a function fizzBuzz which takes in the parameter n which is of int type and returns NONE

package main

import "fmt"

func fizzBuzz(n int) {
    for i := 1; i <= n; i++ {
        if i%3 == 0 && i%5 == 0 {
            fmt.Println("FizzBuzz")
        } else if i%3 == 0 {
            fmt.Println("Fizz")
        } else if i%5 == 0 {
            fmt.Println("Buzz")
        } else {
            fmt.Println(i)
        }
    }
}

func main() {
    // Example usage of the fizzBuzz function
    n := 20 
    fizzBuzz(n)
}
