from collections import Counter

def split_question_to_map(question):
    return Counter(word.lower() for word in question.split())

# common map entries and return sum of their values
def calculate_keyword_similarity(user_keywords, stored_keywords):
    common_keywords = user_keywords & stored_keywords
    return sum(common_keywords.values())

def findans(user_ques):
    with open("qna.txt", "r") as file:
        lines = file.readlines()
        best_match = None
        best_similarity = 0
        user_keywords_map = split_question_to_map(user_ques)

        for i in range(0, len(lines), 1):
            if(lines[i][0]=='Q'):
                question = lines[i].strip()[2:]
                question = question.strip('?')
        
                stored_keywords_map = split_question_to_map(question)
                similarity = calculate_keyword_similarity(user_keywords_map, stored_keywords_map)

                # print(f"{question} {similarity}")

                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = lines[i + 1].strip()

        if best_similarity > 0:  # At least one keyword must match
            return best_match
        else:
            return "Sorry, I don't have an answer for that."

while True:
    user_ques = input("Ask me a question. Type 'exit' to stop: ")
    if user_ques.lower() == 'exit':
        break
    answer = findans(user_ques)
    print("Answer:", answer[2:])