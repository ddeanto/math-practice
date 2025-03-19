// define a function that returns truthy or falsies
function isStringSmall(str) {
    if (str.length <= 5) {
        return true
    }
    return false
}

// define test array
const arr = ["I", "Darren", "Deanto", "am", "such", "a", "ridiculously", "sexually", "attractive", "bitch"];

// can use built in filter method on an array
// call it via arr.filter and pass in a function that 
// returns falsie or truthies
// it only keeps the elements that return truthy when passed to the
// function you give it
const filteredArray = arr.filter(isStringSmall);
console.log(filteredArray);

// similarly, instead of defining a function the usual way, we can use
// () => blah notation to define the function in the filter cuz we only need it there once
const filteredArray2 = arr.filter(str => str.length <= 5 ? true : false);
console.log(filteredArray2);








const numberArray = [2, 3, 4, 5, 35];

// PASSING AN INLINE ARROW FUNCTION TO .map
const doubleArray = numberArray.map(numberItem =>{
	return numberItem * 2
}) 

console.log(doubleArray) // [4, 6, 8, 10, 70]


// PASSING A STANDARD FUNCTION TO .map

function doubleNumber(numberItem) {
    return 2 * numberItem
}

const doubleArray2 = numberArray.map(doubleNumber) 

console.log(doubleArray2) // [4, 6, 8, 10, 70]


// same as this
const doubleArray3 = [];
for (const numberItem of numberArray) {
    const numberDoubled = numberItem * 2;
    doubleArray3.push(numberDoubled);
}

console.log(doubleArray3) // [4, 6, 8, 10, 70]


//
const original = [2, 3, 4, 5, 35];
const mapped = [doubleNumber(2), doubleNumber(3), doubleNumber(4), doubleNumber(5), doubleNumber(35)];
