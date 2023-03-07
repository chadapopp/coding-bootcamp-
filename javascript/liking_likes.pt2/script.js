console.log("working")




function addLike(id){
    var element = document.querySelector(id)
    var count = parseInt(element.innerText)
    element.innerText= count+1

}

