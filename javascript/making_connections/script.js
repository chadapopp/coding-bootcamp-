console.log("page loaded...")

var requestSpan= document.querySelector ("#requests")
var connectionSpan = document.querySelector ("#connections")

function accept(id) {
    var element = document.querySelector (id)
    element.remove (id)
    requestSpan.innerText--
    connectionSpan.innerText++
}

function ignore(id) {
    var element = document.querySelector (id)
    element.remove (id)
    requestSpan.innerText--
}

function edit(){
    var user_name = document.querySelector ("#user_name")
    user_name.innerText = "Your Name Here"
}