# @michelle
# Docs say: Part 1 instruction were ambiguous resulting in inconsistently reversed item responses.
# so skipping this for now


def get_question_score_map_function(question:str):
    """returns a function tht takes in a student's answer to the above question and returns a score if appropriate"""
    def mapper(student_answer):
        return student_answer
    return mapper # TODO


# Introversion (I) vs. Extroversion (E)
# Sensing (S) vs. Intuition (N)
# Feeling (F) vs. Thinking (T)
# Judging (J) vs. Perceiving (P)


# **Scoring: Part 1**
# IE = 30 - Q3 - Q7 - Q11 + Q15 - Q19 + Q23 + Q27 - Q31
# SN = 12 + Q4 + Q8 + Q12 + Q16 + Q20 - Q24 - Q28 + Q32
# FT = 30 - Q2 + Q6 + Q10 - Q14 - Q18 + Q22 - Q26 - Q30
# JP = 18 + Q1 + Q5 - Q9 + Q13 - Q17 + Q21 - Q25 + Q29

# If IE > 24, personality = extroverted (E), else introverted (I).
# If SN > 24, personality = intuitive (N), else sensing (S).
# If FT > 24, personality = thinking (T), else feeling (F).
# If JP > 24, personality = perceiving (P), else judging (J).