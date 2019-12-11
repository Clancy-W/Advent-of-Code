package main

import (
  "fmt"
  "io/ioutil"
  "os"
  "log"
  "strconv"
)

func main() {
  file, err := os.Open("inp.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

  inp, err := ioutil.ReadAll(file)

  var current []byte
  var rowNums []int
  a, b, biggest, smallest := 0, 0, 0, 10000
  for _, s := range inp {
    switch s {
    case 9:
      temp, _ := strconv.Atoi(string(current))
      if temp > biggest {biggest = temp}
      if temp < smallest {smallest = temp}
      rowNums = append(rowNums, temp)
      current = nil
    case 10:
      temp, _ := strconv.Atoi(string(current))
      if temp > biggest {biggest = temp}
      if temp < smallest {smallest = temp}
      rowNums = append(rowNums, temp)

      // PART B:
      partb:
        for i:=0;i<len(rowNums);i++ {
          for j:=0;j<len(rowNums);j++ {
            if rowNums[i] % rowNums[j] == 0 && i != j {
              b += rowNums[i]/rowNums[j]
              break partb
            }
          }
        }

      current = nil
      rowNums = nil
      a += biggest - smallest
      biggest = 0
      smallest = 10000
    case 13:
      continue
    default:
      current = append(current, s)
    }
  }
  fmt.Println("PART A:", a)
  fmt.Println("PART B:", b)
}
