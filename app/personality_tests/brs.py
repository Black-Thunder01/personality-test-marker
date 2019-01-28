def _forward_mapper(student_answer:str):
    return {
        "strongly disagree" : 1,
        "disagree"          : 2,
        "neutral"           : 3,
        "agree"             : 4,
        "strongly agree"    : 5
    }[student_answer.lower()]

def _reverse_mapper(student_answer):
    return {
        "strongly disagree" : 5,
        "disagree"          : 4,
        "neutral"           : 3,
        "agree"             : 2,
        "strongly agree"    : 1
        }[student_answer.lower()]

def _get_question_number(question):
    questions = {
        1 : "I tend to bounce back quickly after hard times.",
        2 : "I have a hard time making it through stressful events.",
        3 : "It does not take me long to recover from a stressful event.",
        4 : "It is hard for me to snap back when something bad happens.",
        5 : "I usually come through difficult times with little trouble.",
        6 : "I tend to take a long time to get over set-backs in my life.",
    }
    question = question.lower()
    for number, match_question in questions.items():
        if match_question.lower() in question:
            return number
    raise Exception(f"could not find question number for:\n\t{question}")

def get_question_score_map_function(question:str):
    """returns a function tht takes in a student's answer to the above question and returns a score if appropriate"""
    num = _get_question_number(question)
    if num in [1, 3, 5]:
        return _forward_mapper
    elif num in [2, 4, 6]:
        return _reverse_mapper
    else:
        raise Exception(f"Question number {num} not recognised ({question})")

def append_final_test_score(df,BRS,column_list):
    """once all the answers have individual scores, we find the average"""
    df[BRS] = df[column_list].mean(axis=1)
