from src.data_preprocessing import load_data, preprocess
from src.workload_analysis import analyze_workload
from src.prediction_model import train_model
from src.visualization import plot_workload

data = load_data()

data = preprocess(data)

data = analyze_workload(data)

model, predictions = train_model(data)

print(data)

plot_workload(data)