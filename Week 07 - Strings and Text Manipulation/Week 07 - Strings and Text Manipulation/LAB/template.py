"""
RECORD CHECK  -  my version
===========================

Name  : Farhaan Ahmed
Lane  :  AI 
Date  : 11-11-2026

Run it:   python template.py


"""

# =================================================================== FUNCTIONS


def parse_line(raw_line):
    """Clean and parse one raw survey line into a dictionary."""
    line = raw_line.strip()
    dataset_part, rest = line.split(",", 1)
    dataset_name = dataset_part.strip().lower()
    
    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
        
    return {
        "dataset": dataset_name, 
        "rating": fields["rating"], 
        "age": fields["age"]
    }

def status_of(data):
    """Determine if a survey record is flagged based on rating."""
    if data["rating"] <= 2:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT

raw_records = [
    "  SURVEY_2026 , RATING = 4 , AGE = 23 ",
    "census_data, rating=1, age=45",
    " SALES_LOG , rating = 5 , age = 30",
    "feedback_form,RATING=2,AGE=19",
    "  User_Poll , rating = 3 , age = 52 "
]




# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

total_records = 0
flagged_count = 0

for raw_record in raw_records:
    parsed_dict = parse_line(raw_record)
    record_status = status_of(parsed_dict)
    
    total_records = total_records + 1
    if record_status == "FLAGGED":
        flagged_count = flagged_count + 1
        
    print(parsed_dict, record_status)

print(f"Total records: {total_records}, Flagged records: {flagged_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
