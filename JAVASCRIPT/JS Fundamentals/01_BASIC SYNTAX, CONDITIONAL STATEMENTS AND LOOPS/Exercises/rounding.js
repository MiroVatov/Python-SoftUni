function rounding( num, presicion ) {
    if (presicion > 15){
        presicion = 15;
    }
    num = num.toFixed(presicion);
    console.log(parseFloat(num))
//    i can use  Number(num)  in order to get rid ot the trailing zeros 15.003
}

rounding(10.5,3);