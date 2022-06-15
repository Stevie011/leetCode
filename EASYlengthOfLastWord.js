/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    //splits string into array, new item each space
    let newArr = s.trim().split(" ")
    //if length of new array is 0 return 0, else return length of last word
    return(newArr.length == 0 ? 0 : (newArr[newArr.length-1]).length)
};