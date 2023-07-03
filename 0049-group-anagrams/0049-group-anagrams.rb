# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    strs.group_by do |word|
        word.chars.sort.join
    end.values
end