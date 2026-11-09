"""
RECORD CHECK  -  my version
===========================
Name  : Farhaan Ahmed
Lane  : IT      
Date  : 19/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# =================================================================== FUNCTIONS
# 1
def check_record(value, limit):
    """determine if value is over limit"""
    if value > limit:
        return "OVER LIMIT"
    else:
        return "OK"

def print_report(label, status):
    """print the record label and status"""
    print(f"{label}: {status}")

# ====================================================================== STORE
# 2. 

records = []   
def load_records(path):
    """load records from file into a list of dicts"""
    try:
        records = []
        with open(path) as f:
            for line in f:
                label, val, lim = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(val),
                    "limit": float(lim)
                })
        return records
    except FileNotFoundError:
        print("File not found.")
        return []

records = load_records("records_sample.txt")

# =============================================================== PROCESS + OUTPUT
# 3. 
over_count = 0
results_file = open("results.txt", "w")

for r in records:
    status = check_record(r["value"], r["limit"])
    print_report(r["label"], status)
    
    results_file.write(f"{r['label']},{status}\n")
    
    if status == "OVER LIMIT":
        over_count += 1

results_file.close()
print(f"{over_count} of {len(records)} were over limit")
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
