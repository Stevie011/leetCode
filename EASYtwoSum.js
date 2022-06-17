/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    for(let i=0; i<nums.length; i++){
        for(let j=i+1; j<nums.length; j++){
            if(nums[i]+nums[j] == target){
                return [i,j]
            }
        }
    }
};

//nested for loops, compare sum at each iteration to target, make sure to return i & j instead of nums[i] and nums[j]