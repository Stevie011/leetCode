/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    for(let i=0; i<nums.length; i++){
        for(let j=i+1; j<nums.length; j++){
            if(nums[i] == nums[j]){
                return true
            }
        }
    }
    return false
};

//this is a standard nested loop to compare each item in array with each other item