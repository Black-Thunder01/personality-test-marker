def get_question_score_map_function(question:str):
    """returns a function that takes in a student's answer to the above question and returns a score according to the Toronto Empathy Questionnaire
    """
    num = _get_question_number(question)
    if num in [1, 3, 5, 6, 8, 9, 13, 16]:
        return _forward_mapper
    elif num in [2, 4, 7, 10, 11, 12, 14, 15]:
        return _reverse_mapper
    else:
        raise Exception(f"Question number {num} not recognised ({question})")


def _get_question_number(question:str):
    questions = {
        1 : "When someone else is feeling excited, I tend to get excited too",
        2 : "Other people’s misfortunes do not disturb me a great deal",
        3 : "It upsets me to see someone being treated disrespectfully",
        4 : "I remain unaffected when someone close to me is happy",
        5 : "I enjoy making other people feel better",
        6 : "I have tender, concerned feelings for people less fortunate than me",
        7 : "When a friend starts to talk about his\her problems, I try to steer the conversation towards something else",
        8 : "I can tell when others are sad even when they do not say anything",
        9 : "I find that I am “in tune” with other people’s moods",
        10 : "I do not feel sympathy for people who cause their own serious illnesses",
        11 : "I become irritated when someone cries",
        12 : "I am not really interested in how other people feel",
        13 : "I get a strong urge to help when I see someone who is upset",
        14 : "When I see someone being treated unfairly, I do not feel very much pity for them",
        15 : "I find it silly for people to cry out of happiness",
        16 : "When I see someone being taken advantage of, I feel kind of protective towards him\her"
    }
    question = question.lower()
    for number, match_question in questions.items():
        if match_question.lower() in question:
            return number
    raise Exception(f"could not find question number for:\n\t{question}")


def _reverse_mapper(student_answer):
    return {
        'never'     : 4, 
        'rarely'    : 3, 
        'sometimes' : 2,
        'often'     : 1, 
        'always'    : 0
        }[student_answer.lower()]


def _forward_mapper(student_answer):
    return {
        'never'     : 0, 
        'rarely'    : 1, 
        'sometimes' : 2,
        'often'     : 3, 
        'always'    : 4
        }[student_answer.lower()] 


def get_final_test_score():
    """once all the answers have individual scores, we add them up"""