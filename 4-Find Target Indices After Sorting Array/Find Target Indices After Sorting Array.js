/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    let sorted = [].concat(nums)
    sorted.sort(function(a,b) {return a-b})
    let result = []
    let counter = 0
    for ( const num in nums) {
        if (nums[num] == target) {
            result.push(sorted.indexOf(nums[num]) + counter)
            counter ++
        }
    }
    return result
};
