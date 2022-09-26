/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let sorted = [].concat(nums)
    sorted.sort(function(a, b){return a - b})
    let result = []
    for (const num in nums) {
        result.push(sorted.indexOf(nums[num]))
    }
    return result
};
