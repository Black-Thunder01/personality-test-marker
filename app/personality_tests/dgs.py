



def _forward_mapper(student_answer):
    return {
        'very much like me'     : 5, 
        'mostly like me'        : 4, 
        'somewhat like me'      : 3,
        'not much like me'      : 2, 
        'not like me at all'    : 1
        }[student_answer.lower()] 


def _reverse_mapper(student_answer):
    return {
        'very much like me'     : 1, 
        'mostly like me'        : 2, 
        'somewhat like me'      : 3,
        'not much like me'      : 4, 
        'not like me at all'    : 5
        }[student_answer.lower()] 





def _get_question_number(question):
    questions = {
        1 : "New ideas and projects sometimes distract me from previous ones",
        2 : "Setbacks don’t discourage me",
        3 : "I often set a goal but later choose to pursue a different one",
        4 : "I am a hard worker",
        5 : "I have difficulty maintaining my focus on projects that take more than a few months to complete",
        6 : "I finish whatever I begin",
        7 : "My interests change from year to year",
        8 : "I am diligent. I never give up",
        9 : "I have been obsessed with a certain idea or project for a short time but later lost interest",
        10 : "I have overcome setbacks to conquer an important challenge",
    }
    question = question.lower()
    for number, match_question in questions.items():
        if match_question.lower() in question:
            return number
    raise Exception(f"could not find question number for:\n\t{question}")


def get_question_score_map_function(question:str):
    """returns a function tht takes in a student's answer to the above question and returns a score according to the Duckworth Grit Scale"""
    num = _get_question_number(question)
    if num in [2, 4, 6, 8, 10]:
        return _forward_mapper
    elif num in [1, 3, 5, 7, 9]:
        return _reverse_mapper
    else:
        raise Exception(f"Question number {num} not recognised ({question})")


def append_final_test_score(df,DGS,column_list):
    """once all the answers have individual scores, we find the average"""
    assert len(column_list) == 10
    df[DGS] = df[column_list].mean(axis=1)




def _human_friendly_map_function(final_score:int) -> str:
    if final_score == 5:
        return "high grit"
    if final_score <= 2:
        return "low grit"
    return "medium grit"


def append_human_friendly_test_score(df,DGS,column_list):
    """
    high grit: = 5
    low grit: <= 2
    """
    df[f"human_{DGS}"] = df[DGS].map(_human_friendly_map_function)

