from .google_sheets import fetch_sheet 
from .personality_tests import baron_cohen,brs,dgs,ipip,jung_part1,jung_part2,teq
import re

TEQ   = "TEQ"
BRS   = "BRS"
DGS   = "DGS"
IPIP  = "IPIP"
JUNG1 = "JUNG1"
JUNG2 = "JUNG2"
BARON_COHEN="BARON_COHEN"


# sections = {
#     1   : teq.get_question_score_map_function,
#     2   : brs.get_question_score_map_function,
#     3   : dgs.get_question_score_map_function,
#     4   : baron_cohen.get_question_score_map_function,
#     5   : ipip.get_question_score_map_function
# }

# parts = {
#     1  : jung_part1.get_question_score_map_function,
#     2  : jung_part2.get_question_score_map_function
# }


section_test_names = { # for decifing which columns map to which personality tests
    1   : TEQ,
    2   : BRS,
    3   : DGS,
    4   : BARON_COHEN,
    5   : IPIP
}

part_test_names = { # for decifing which columns map to which personality tests
    1  : JUNG1,
    2  : JUNG2
}


personality_test_functionality = {
    # maps some constant string names to modules containing required functionality
    TEQ         : teq,
    BRS         : brs,
    DGS         : dgs,
    BARON_COHEN : baron_cohen,
    IPIP        : ipip,
    JUNG1       : jung_part1,
    JUNG2       : jung_part2
}

column_names = { # this will hold the names of all the columns we care about for each test
    TEQ         : [],
    BRS         : [],
    DGS         : [],
    BARON_COHEN : [],
    IPIP        : [],
    JUNG1       : [],
    JUNG2       : []
}


def get_column_test_name_and_question(column:str):
    search = re.search("^Section (\d) of 6 \[(.*)\]$", column)
    if search:
        section = int(search[1])
        question = search[2]
        return (section_test_names[section],question)
    search = re.search("^Part (\d) : (.*) \[(.*)\]$",column)
    if search:
        part = int(search[1])
        part_desc = search[2]
        question = search[3]
        return (part_test_names[part],question)
    # it's an informative column, eg email address
    return None,None



def score_all_answers(df):
    for i,column in enumerate(df.columns):
        column_test_name,question = get_column_test_name_and_question(column)
        # map_function = get_question_score_map_function(column)
        if column_test_name:
            column_names[column_test_name].append(column)
            map_function = personality_test_functionality[column_test_name].get_question_score_map_function(question)
            df[column] = df[column].map(map_function)
        # else: it's personal info or meta data, eg email address. needs no mapping


def append_final_test_scores(df):
    for s in column_names:
        personality_test_functionality[s].append_final_test_score(df,s,column_names[s])


def main(sheet_name):
    df = fetch_sheet(sheet_name)
    score_all_answers(df)
    append_final_test_scores(df)
    df.to_csv("gitignore/scored_answers.csv")
    return df








# df = main("Applicant Personality Review (Dec 2018) (Responses)")


# column_list = column_names[IPIP]
# for category in categories:
#     df[f"{IPIP}_"] = df[column_list].sum(axis=1)
# df.to_csv("gitignore/scored_answers.csv")



