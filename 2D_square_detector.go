// You receive 2d gps coordinates.
// Task is to write a program that detects if a given point can create a square with any 3 previously seen square. 
// Only squares consisting of horizontal and vertical lines is considered which is parallely alignmed with x or y axis, 
// method add(x,y) adds the coordinates and another function that returns a boolean true if a square can be formed. 
// Also add a logic to check the possible values of y that can form a square if a square is not formed. 
// Make the code to check the lengths of sides and check if they are equal

package main

import (
	"fmt"
	"math"
)

type Point struct {
	X, Y int
}

type SquareDetector struct {
	Points map[Point]bool
}

func NewSquareDetector() *SquareDetector {
	return &SquareDetector{
		Points: make(map[Point]bool),
	}
}

func (sd *SquareDetector) Add(x, y int) {
	point := Point{X: x, Y: y}
	sd.Points[point] = true
}

func (sd *SquareDetector) CanFormSquare() (bool, int) {
	for point1 := range sd.Points {
		for point2 := range sd.Points {
			if point1 != point2 {
				if point1.X == point2.X || point1.Y == point2.Y {
					diagonalX := math.Abs(float64(point1.X - point2.X))
					diagonalY := math.Abs(float64(point1.Y - point2.Y))

					if diagonalX == diagonalY {
						sideLength := diagonalX
						if _, exists1 := sd.Points[Point{X: point1.X, Y: point1.Y + int(sideLength)}]; exists1 {
							if _, exists2 := sd.Points[Point{X: point2.X, Y: point2.Y + int(sideLength)}]; exists2 {
								return true, point1.Y + int(sideLength)
							}
						}
					}
				}
			}
		}
	}
	return false, 0
}

func main() {
	sd := NewSquareDetector()
	sd.Add(1, 1)
	sd.Add(1, 5)
	sd.Add(5, 1)
	sd.Add(5, 5)

	canFormSquare, possibleY := sd.CanFormSquare()
	if canFormSquare {
		fmt.Println("A square can be formed.")
	} else {
		fmt.Println("A square cannot be formed.")
		if possibleY > 0 {
			fmt.Println("Possible Y value for square formation:", possibleY)
		}
	}
}
