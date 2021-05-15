function sumOfOddNumbers(num) {
    let n = 1
    let oddsSum = 0
    for (i = 1; n <= num; i++) {
        if (i % 2 !== 0) {
            console.log(i)
            n++
            oddsSum += i
        }
    }
    console.log(`Sum: ${oddsSum}`)
}

sumOfOddNumbers(9)