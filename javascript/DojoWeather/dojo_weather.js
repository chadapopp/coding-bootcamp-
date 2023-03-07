function message(){
    alert ("Loading weather report...")
}

var footer = document.querySelector(".footer")

function ignore() {
    footer.remove()
}

function c2f(temp) {
    return Math.round (9 / 5 * temp + 32)
}

function f2c(temp) {
    return Math.round (5 / 9 * (temp - 32))
}


function convert(element) {
    for (var i=1; i<9; i++){
        var temp = document.querySelector("#temp" + i)
        var tempVal = temp.innerText
        if(element.value =="\xB0 C"){
            temp.innerText = f2c(tempVal)}
        else{
            temp.innerText = c2f(tempVal)
        }

    }

}