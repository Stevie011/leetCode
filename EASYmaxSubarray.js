/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    //one variable for max
    let ansSum = -Infinity
    //variable for current
    let tempSum = 0
    //loop through the array
    for(let i=0; i < nums.length; i++){
        //tempSum becomes whichever is the most out of nums[i] and tempSum + nums[i]
        //ie. if adding the current number reduces the total, tempSum becomes that number
        tempSum = Math.max(nums[i], tempSum + nums[i])
        //if tempSum is bigger than ansSum it replaces anSum
        ansSum = Math.max(tempSum, ansSum)
    }
    return ansSum
};