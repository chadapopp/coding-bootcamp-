// Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order. As always, do not use built-in array functions.

function removeNegatives(array){
    let index = 0;
    for (let i = 0; i <array.length; i++){
        if (array[i] >= 0){
            array[index] = array[i];
            index ++
        }
    }
    array.length = index;
    return array
}
var array = [-2,2,4,5,-6,-9]
removeNegatives(array)
console.log(array)

// Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.

function secondToLast(arr){
    if (arr.lenth < 2 ){
        return null;
    }
    return arr[arr.length-2];
}
var input = [42,true,4,"Kate",7]
var output = secondToLast(input)
console.log(output)

// Return the second-largest element of an array. Given [42,1,4,Math.PI,7], return 7. If the array is too short, return null.

// function secondToLargest(arr){
//     if (arr.lenth < 2 ){
//         return null;
//     }
//     let largest = arr[0];
//     let secondLargest = null;
//     for (let i = 1; i <arr.length; i++){
//         if (arr[i]> largest){
//             secondLargest = largest;
//             largest = arr[i];
//         }else if(arr[i] < largest && (secondLargest === null || arr[i] > secondLargest)){
//             secondLargest = arr[i]
//         }
//     }
//     return secondLargest
// }
// let arr = [42, 1, 4, Math.PI, 7];
// let secondLargest =secondToLargest(arr);
// console.log(secondLargest)


// Return the element that is N-from-array’s-end. Given ([5,2,3,6,4,9,7],3), return 4. If the array is too short, return null.

// function nFromEnd(arr,n){
//     if(arr.length <n){
//         return null;
//     }else{
//         return arr[arr.length - n];
//     }
// }
// const arr = [5,2,3,6,4,9,7];
// const n = 3;
// const result = nFromEnd(arr,n)
// console.log(result)

// Liam has "N" number of Green Belt stickers for excellent Python projects. Given arr and N, return the Nth-largest element, where (N-1) elements are larger. Return null if needed.

function nthLargest(arr, N){
    if (N >arr.length){
        return null;
    }
    arr.sort(function(a,b){
        return b-a;
    });
    return arr[N-1];
}
const arr = [5, 8, 2, 6, 9, 3];
const N = 3;
const result = nthLargest(arr, N);
console.log(result);

// Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().

function visibleBuildings(buildings){
    const visibleBuildings = [];
    let maxHeight = 0;
    for (let i=buildings.length-1; i > 0; i--){
        if (buildings[i] > maxHeight){
            visibleBuildings.push(buildings[i]);
            maxHeight = buildings[i]
        }
    }

    return visibleBuildings
}

const buildings1 = [-1, 1, 1, 7,3];
const visible1 = visibleBuildings(buildings1);
console.log(visible1); 

const buildings2 = [0, 4];
const visible2 = visibleBuildings(buildings2);
console.log(visible2);