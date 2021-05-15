function divisiblebyThree() {
    let num = 1
    for (i = num; i <= 100; i++)
        if (i % 3 === 0)
            console.log(i)
}

divisiblebyThree()