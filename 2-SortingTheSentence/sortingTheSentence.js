/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    s = s.split(' ')
    let result = ''
    let counter = 0
    for (const word of s) {
        counter += 1
        for (const w of s) {
            if (parseInt(w.split('').reverse()[0]) === counter) {
                result += w.replace(counter.toString(), ' ')
            }
        }
    }
    return result.trim()
};
