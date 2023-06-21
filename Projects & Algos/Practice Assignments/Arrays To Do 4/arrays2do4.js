// In JavaScript, the Array object has numerous useful methods. It does not, however, contain a method that will randomize the order of an array’s elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?

// function shuffle(arr){
//     for (let i = arr.length -1; i > 0; i--){
//         const j = Math.floor(Math.random() * (i +1));
//         [arr[i]], arr[j] = [arr[j]], arr[i];
//     }
//     return arr;
// }
// const arr = [1, 2, 3, 4, 5];
// shuffle(arr);
// console.log(arr);

// Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array). Given ([20,30,40,50,60,70],2,4), change to [20,30,70] and return it.
// function removeRange(arr, start, end){
//     arr.splice(start, end - start +1)
//     return arr;
// }

// const arr = [20,30,40,50,60,70];
// removeRange(arr, 1, 2);
// console.log(arr)

// You will be given an array of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the array does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums. Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6]
// function addSums(arr) {
//     let sum = 0;
//     for (let i = 0; i < arr.length; i++) {
//         sum += arr[i];
//         if ((i + 1) % 10 === 0) {
//             arr.splice(i + 1, 0, sum);
//             sum = 0;
//         }
//         }
//         if (sum !== 0) {
//         arr.push(sum);
//         }
//         return arr;
//     }

//     const arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2];
// addSums(arr);
// console.log(arr); 

// Create a function that changes a given array to list each original element twice, retaining original order. Convert [4,"Ulysses",42,false] to [4,4,"Ulysses","Ulysses",42,42,false,false].

function doubleIt(arr){
    var result = [];
    for (let i = 0; i <arr.length; i++){
        result.push(arr[i], arr[i])
    }
    return result
}

var input = [4,"Ulysses",42,false]
var output = doubleIt(input)
console.log(output)

// Create a standalone function that accepts two arrays and combines their values sequentially into a new array, at alternating indices starting with first array. Extra values from either array should be included afterward. Given [1,2] and [10,20,30,40], return new array containing [1,10,2,20,30,40].

// Second: combine the two arrays’ values into the first array, instead of into a new array. Much more fun!

function alternateArray(arr1, arr2){
    let maxLength = Math.max(arr1.length, arr2.length);
    for (let i = 0; i < maxLength; i++){
        if (i < arr2.length){
            arr1.splice(i * 2 + 1, 0, arr2[i])
        }
    }
    return arr1;
}

let arr1 = [1,2];
let arr2 = [10,20,30,40];
alternateArray(arr1, arr2);
console.log(arr1)