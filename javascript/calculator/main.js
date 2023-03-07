// var num = document.querySelectorAll ()

// function press(id) {
//     document.getElementById('result').value += val
// }

// function calculate() {
//     var 
// }



var displayDiv = document.getElementById("display")
var num = document.querySelectorAll('.number')

function press(displayed) {
    num = displayed
    displayDiv.innerText = displayed
    displayDiv.innerText = num.innerText
}

console.log(num.innerText)

console.log(displayDiv.innerText)