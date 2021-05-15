function login(name) {
    for (let i = 0; i < name.length; i++) {
        currentName = name[i]
        if (i === 0) {
            username = currentName;
            password = currentName.split("").reverse().join("")
        }
        else if (currentName === password) {
            console.log(`User ${username} logged in.`);
        }
        else if (i === 4) {
            console.log(`User ${username} blocked!`);
        }
        else {
            console.log(`Incorrect password. Try again.`);
        }
    }
}

// login( ['Acer','login','go','let me in','recA'] )
// login( ['momo','omom'])
login(['sunny','rainy','cloudy','sunny','not sunny'])