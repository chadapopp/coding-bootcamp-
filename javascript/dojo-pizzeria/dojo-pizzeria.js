function pizzaOven(crust, sauce, cheese, toppings){
    var pizza = {}
    pizza.crust = crust
    pizza.sauce = sauce
    pizza.cheese = cheese
    pizza.toppings = toppings
    return pizza

}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni" , "sausage"])
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella","feta"], ["mushrooms" , "olives", "onions"])
var pizza3 = pizzaOven("stuffed", "alfredo", ["mozzarella"], ["pepperoni" , "sausage", "bacon"])
var pizza4 = pizzaOven("thin", "marinara", ["provolone","feta"], ["bacon", "mushrooms" , "olives", "onions"])

console.log(pizza1)



// var crust = ["deep dish", "thin", "stuffed", "pan" , "hand tossed", ]
// var sauce = ["marinara" , "alfredo", "traditional", "bbq", "hot sauce"]
// var cheese = ["mozzarella", "cheddar", "provolone", "swiss"]
// var toppings = ["pepperoni", "sasuage", "bacon", "hamburger", "chicken", "black olives", "green olives", "green peppers", "jalapenos", "onions", "anchovies", "mushrooms" ]
// function randomChoice(arr){
//     var i = Math.floor (arr.length * Math.random())
//     return arr[i]
// }
// randomChoice()

// function randomPizza(){
//     var pizza = {}
//     pizza.crust = randomChoice(crust)
//     pizza.sauce = randomChoice(sauce)
//     pizza.cheese = randomChoice(cheese)
//     pizza.toppings = randomChoice(toppings)
//     return pizza
    
// }

// randomPizza()


