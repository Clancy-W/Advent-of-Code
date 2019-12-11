package main

import (
  "fmt"
  "io/ioutil"
  "os"
  "log"
)

func solve(offset int, inp []byte) int{
  ans := 0
  for i:=0; i<len(inp);i++ {
    if inp[i] == inp[(i+offset)%len(inp)] {
      ans += int(inp[i])-48
    }
  }
  return ans
}

func main() {
  file, err := os.Open("inp.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()


  inp, err := ioutil.ReadAll(file)
  inp = inp[:len(inp)-2]
  fmt.Println("PART A:", solve(1, inp))
  fmt.Println("PART B:", solve(len(inp)/2, inp))
}
