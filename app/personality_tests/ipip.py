
def _get_question_category_and_direction(question: str):
    """ returns a tuple where t[0] is the scoring category and t[1] is the direction of the scoring
    """
    questions = {
        "I am the life of the party"                              : (1,'+'),
        "I feel little concern for others"                        : (2,'-'),
        "I am always prepared"                                    : (3,'+'),
        "I get stressed out easily"                               : (4,'-'),
        "I have a rich vocabulary"                                : (5,'+'),
        "I don't talk a lot"                                      : (1,'-'),
        "I am interested in people"                               : (2,'+'),
        "I leave my belongings lying around"                      : (3,'-'),
        "I am relaxed most of the time"                           : (4,'+'),
        "I have difficulty understanding abstract ideas"          : (5,'-'),
        "I feel comfortable around people"                        : (1,'+'),
        "I insult people"                                         : (2,'-'),
        "I pay attention to details"                              : (3,'+'),
        "I worry about things"                                    : (4,'-'),
        "I have a vivid imagination"                              : (5,'+'),
        "I keep in the background"                                : (1,'-'),
        "I sympathize with others' feelings"                      : (2,'+'),
        "I make a mess of things"                                 : (3,'-'),
        "I seldom feel blue (down)"                               : (4,'+'),
        "I am not interested in abstract ideas"                   : (5,'-'),
        "I start conversations"                                   : (1,'+'),
        "I am not interested in other people's problems"          : (2,'-'),
        "I get chores done right away"                            : (3,'+'),
        "I am easily disturbed"                                   : (4,'-'),
        "I have excellent ideas"                                  : (5,'+'),
        "I have little to say"                                    : (1,'-'),
        "I have a soft (kind) heart"                              : (2,'+'),
        "I often forget to put things back in their proper place" : (3,'-'),
        "I get upset easily"                                      : (4,'-'),
        "I do not have a good imagination"                        : (5,'-'),
        "I talk to a lot of different people at parties"          : (1,'+'),
        "I am not really interested in others"                    : (2,'-'),
        "I like order"                                            : (3,'+'),
        "I change my mood a lot"                                  : (4,'-'),
        "I am quick to understand things"                         : (5,'+'),
        "I don't like to draw attention to myself"                : (1,'-'),
        "I take time out for others"                              : (2,'+'),
        "I neglect my duties"                                     : (3,'-'),
        "I have frequent mood swings"                             : (4,'-'),
        "I use difficult words"                                   : (5,'+'),
        "I don't mind being the center of attention"              : (1,'+'),
        "I feel others' emotions"                                 : (2,'+'),
        "I follow a schedule"                                     : (3,'+'),
        "I get irritated easily"                                  : (4,'-'),
        "I spend time reflecting on things"                       : (5,'+'),
        "I am quiet around strangers"                             : (1,'-'),
        "I make people feel at ease"                              : (2,'+'),
        "I am exacting (demanding) in my work"                                : (3,'+'),
        "I often feel blue (down)"                                : (4,'-'),
        "I am full of ideas"                                      : (5,'+')
    }

    question = question.lower()
    for match_question, (category,direction) in questions.items():
        if match_question.lower() in question:
            return category,direction
    raise Exception(f"could not find category for:\n\t{question}")


categories = {
    1: "Extraversion", 
    2: "Agreeableness",
    3: "Conscientiousness",
    4: "Emotional Stability/Neuroticism",
    5: "Intellect/Imagination / openness to experiences"
}


def _calculate_forward_score(student_answer):
    # @michelle. The README and the g sheet dont use the same scale  
    # the README says:
    # "Very Inaccurate" is assigned a value of 1, "Moderately Inaccurate" a value of 2, "Neither Inaccurate nor Accurate" a 3, "Moderately Accurate" a 4, and "Very Accurate" a value of 5
    return {
        'agree'    : 5,
        'neutral'  : 3,
        'disagree' : 1
    }[student_answer.lower()]
    

def _calculate_reverse_score(student_answer):
    # @michelle. The README and the g sheet dont use the same scale  
    # the README says:
    # "Very Inaccurate" is assigned a value of 1, "Moderately Inaccurate" a value of 2, "Neither Inaccurate nor Accurate" a 3, "Moderately Accurate" a 4, and "Very Accurate" a value of 5
    return {
        'agree'    : 1,
        'neutral'  : 3,
        'disagree' : 5
    }[student_answer.lower()]


def get_question_score_map_function(question:str):
    """returns a function tht takes in a student's answer to the above question and returns a score if appropriate"""
    category,direction = _get_question_category_and_direction(question)

    if direction == '+':
        def mapper(student_answer):
            return (category,_calculate_forward_score(student_answer))
        return mapper 

    if direction == '-':
        def mapper(student_answer):
            return (category,_calculate_reverse_score(student_answer))
        return mapper 
    
    
