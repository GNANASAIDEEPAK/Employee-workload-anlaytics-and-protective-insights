def classify_workload(score):
    if score > 1:
        return "Overloaded"
    elif score < 0.5:
        return "Underutilized"
    else:
        return "Balanced"

def analyze_workload(data):
    data["Status"] = data["Workload_Score"].apply(classify_workload)
    return data