# Men:
# Above average: >= 17
# Below average: <= 9

# Women:
# Above average: >= 13
# Below average: <= 4

def _get_question_number(question:str) -> int:
    questions = {
        1 : "I find it difficult to read and understand maps",
        2 : "I find it easy to grasp exactly how odds work in betting",
        3 : "I find it difficult to understand information the bank sends me on different investment and saving systems",
        4 : "I do not enjoy games that involve a high degree of strategy (e.g. chess, Risk, poker)",
        5 : "I am fascinated by how machines work",
        6 : "I find it difficult to understand instruction manuals for putting appliances together",
        7 : "If I were buying a computer, I would want to know exact details about its hard disc drive capacity and processor speed",
        8 : "If I were buying a hifi, I would want to know about its precise technical features",
        9 : "I can easily visualize how the highways in my area link up",
        10 : "I do not enjoy in-depth political discussions"
    }
    question = question.lower()
    for number, match_question in questions.items():
        if match_question.lower() in question:
            return number
    raise Exception(f"could not find question number for:\n\t{question}")


def _forward_mapper(student_answer):
    return {
        "strongly agree"    : 2, 
        "slightly agree"    : 1, 
        "slightly disagree" : 0,
        "strongly disagree" : 0 
        }[student_answer.lower()]


def _reverse_mapper(student_answer):
    return {
        "strongly agree"    : 0, 
        "slightly agree"    : 0, 
        "slightly disagree" : 1,
        "strongly disagree" : 2
        }[student_answer.lower()]


def get_question_score_map_function(question:str):
    """returns a function tht takes in a student's answer to the above question and returns a score if appropriate"""
    num = _get_question_number(question)
    if num in [2, 5, 7, 8, 9]:
        return _forward_mapper
    elif num in [1,3,4,6,10]:
        return _reverse_mapper
    else:
        raise Exception(f"Question number {num} not recognised ({question})")



def append_final_test_score(df,BARON_COHEN,column_list):
    df[BARON_COHEN] = df[column_list].sum(axis=1)
