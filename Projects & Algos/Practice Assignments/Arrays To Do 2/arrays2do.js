// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
// array – move values within the array that you are given. As always, do not use built-in array functions such as splice().

// function reverseArrayInPlace(arr){
//     for (var i =0; i < arr.length / 2; i++){
//         var temp = arr[i];
//         arr[i] = arr[arr.length - 1 - i];
//         arr[arr.length -1-i] = temp;
//     }
// }

// arr = [1,2,3,4,5]
// reverseArrayInPlace(arr);
// console.log(arr)

// Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
// change the array to [3,1,2]. Don't use built-in functions.
// Second: allow negative shiftBy (shift L, not R).
// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
// Fourth: minimize the touches of each element.

// function rotateArr(arr, moveBy){
//     var actualMovementsNeeeded;
//     if (moveBy > 0){
//         actualMovementsNeeeded = moveBy % arr.length;

//     }else{
//         actualMovementsNeeeded = Math.abs(moveBy) % arr.length;
//     }
//     if (moveBy >0){
//         for (var i = 0; i < actualMovementsNeeeded; i++){
//             var temp = arr[arr.length -1];
//             for (var k = arr.length -2; k >=0; k--){
//                 arr[k+1] = arr[k];
//             }
//             arr[0] = temp;
//         }
//     }else{
//         for (var i = 0; i < actualMovementsNeeeded; i++){
//             var temp = arr[0];
//             for (var k = 1; k< arr.length; k++){
//                 arr[k-1] = arr[k];
//             }
//             arr[arr.length-1] = temp;
//         }
//     }
// }

// arr = [1,2,3,4,5]

// rotateArr(arr);
// console.log(arr)


// Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.

// function filterArray(arr, minVal, maxVal){
//     for( var i =0; i < arr.length; i++){
//         if(arr[i] <minVal || arr[i]> maxVal){
//             for(var k = i+1; k <arr.length; k++){
//                 arr[k-1] = arr[k];
//             }
//             arr.length--;
//             i--
//         }
//     }
// }

// arr = [1,1,7,4,5,6,77]
// filterArray(arr)
// console.log(arr)

// Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].

function concatArrays(arr1, arr2){
    var newArr = [];
    var curInd = 0;
    for (var i = 0; i<arr1.length; i++){
        newArr[curInd] = arr1[i];
        curInd++;
    }
    for (var i = 0; i <arr2.length; i++){
        newArr[curInd] = arr2[i];
        curInd++;
    }
    return newArr;
}

arr1 = [2,3,4,5]
arr2 = [9,7,6]
concatArrays(arr1, arr2)
console.log(arr1, arr2)