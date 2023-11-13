from itertools import permutations
def solve_cryptarithmetic(word1, word2, result):
    cnt = 0
    unique_chars = set(word1 + word2 + result)
    chars = ''.join(unique_chars)
    digits = '0123456789'

    for perm in permutations(digits, len(unique_chars)):
        mapping = dict(zip(chars, perm))

        if '0' not in mapping[word1[0]] and '0' not in mapping[word2[0]] and '0' not in mapping[result[0]]:
            num1 = int("".join(mapping[char] for char in word1))
            num2 = int("".join(mapping[char] for char in word2))
            num_result = int("".join(mapping[char] for char in result))
            flag = True
            if num1 + num2 == num_result:
                # for carry always 1
                # str1= str(num1)
                # str2= str(num2)
                # if(int(str1[-1])+int(str2[-1])>9):
                #     for i in range(min(len(str1),len(str2))-1, 0, -1):
                #         if(int(str1[i])+int(str2[i])<9):
                #             flag = False
                # else:
                #     flag = False

                if flag==True:
                    cnt = cnt + 1
                    print(f"Solution {cnt}:\n{word1} = {num1}\n{word2} = {num2}\n{result} = {num_result}\n")
    return cnt

words = input("Enter all words: ").lower().split(" ")
cnt = solve_cryptarithmetic(words[0],words[1],words[2])
print("No Solution Found") if (cnt == 0) else print(f"Total {cnt} solutions found")