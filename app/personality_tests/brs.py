# Resilient: >= 5
# Low resilience / risk for stress and anxiety: < 3

def _mapper(student_answer:str):
    return {
        "strongly disagree" : 1,
        "disagree"          : 2,
        "neutral"           : 3,
        "agree"             : 4,
        "strongly agree"    : 5
    }[student_answer.lower()]


def get_question_score_map_function(question:str):
    """returns a function tht takes in a student's answer to the above question and returns a score if appropriate"""
    return _mapper 




def append_final_test_score(df,BRS,column_list):
    """once all the answers have individual scores, we find the average"""
    df[BRS] = df[column_list].mean(axis=1)
