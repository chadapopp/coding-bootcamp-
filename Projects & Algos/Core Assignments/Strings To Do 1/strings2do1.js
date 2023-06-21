// Create a function that, given a string, returns all of that string’s contents, but without blanks. 

// If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

function noBlanks(string){
    var result = "";
    for (var i = 0; i < string.length; i++){
        if (string[i] !==" "){
            result += string[i];
        }
    }
    return result    
}

input = " Pl ayTha tF u nkyM usi c "
output = noBlanks(input)
console.log(output)

// Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.

function returnInteger(str){
    var result = 0;
    for (var i =0; i<str.length; i++){
        const digit = parseInt(str[i]);
        if(!isNaN(digit)){
            result = result * 10 + digit;
        }
    }
    return result;
}

var input = "0s1a3y5w7h9a2t4?6!8?0"
result = returnInteger(input)
console.log(result)


// Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 
// Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 
// Given "Live from New York, it's Saturday Night!", return "LFNYISN".

function returnAcronym(str){
    let words = str.split(' ');
    let result = '';
    for(let i =0; i<words.length; i++){
        let word = words[i];
        if(word[0] >= 'a' && word[0]<='z'){
            result += word[0].toUpperCase();
        }
        else if (word[0] >='A' && word[0]<='Z'){
            result += word[0]
        }
    }
    return result
}

var input = "Live from New York, it's Saturday Night!"
var output = returnAcronym(input)
console.log(output)


// Dictionaries are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

let arr1 = ["abc", 3, "yo"];
let arr2 = [42, "wassup", true];
map = {}

for (let i = 0; i <arr1.length; i++){
    let key = arr1[i];
    let value = arr2[i];
    map[key] = value;
}

console.log(map)

// Dictionaries are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys. 

// Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.

function invertHash(assocArr){
    const inverted = {}
    for (const key in assocArr){
        if(Object.hasOwnProperty.call(assocArr,key)){
            const value = assocArr[key];
            inverted[value] = key;
        }
    }
    return inverted
}

const assocArr = {"name": "Zaphod", "charm": "high", "morals": "dicey"}
const inverted = invertHash(assocArr)
console.log(inverted)