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

def append_final_test_score(df,JUNG,column_list):
    pass

# Makes lists |  Relies on memory,
# Sceptical | Wants to believe,
# Bored by time alone | Needs time alone,
# Accepts things as they are | Unsatisfied with the way things are,
# Keeps a clean room | just puts stuff where ever,
# Thinks ""robotic"" is an insult | Strives to have a mechanical mind,
# Energetic | Mellow,
# Prefer to take multiple choice test | Prefer essay answers,
# Chaotic | Organized,
# Easily hurt | Thick-skinned,
# Works best in groups | Works best alone,
# Focused on the present | Focused on the future,
# Plans far ahead | Plans at the last minute,
# Wants people's respect | Wants their love,
# Gets worn out by parties | Gets fired up by parties,
# Fits in | Stands out,
# Keeps options open | Commits,
# Wants to be good at fixing things | Wants to be good at fixing people,
# Talks more | Listens more,
# When describing an event, will tell people what happened | When describing an event, will tell people what it meant,
# Gets work done right away | Procrastinates,
# Follows the heart | Follows the head,
# Stays at home | Goes out on the town,
# Wants the big picture | Wants the details,
# Improvises | Prepares,
# Bases morality on justice | Bases morality on compassion,
# Finds it difficult to yell very loudly |  Yelling to others when they are far away comes naturally,
# Theoretical | Empirical,
# works hard |  plays hard,
# uncomfortable with emotions |  values emotions,
# Likes to perform in front of other people | Avoids public speaking,
# Likes to know ""who?"", ""what?"", ""when?"" | Likes to know ""why?"",