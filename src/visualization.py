import matplotlib.pyplot as plt

def plot_workload(data):

    plt.hist(data["Hours_Worked"])
    plt.title("Employee Workload Distribution")
    plt.xlabel("Hours Worked")
    plt.ylabel("Frequency")
    plt.show()