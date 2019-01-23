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
