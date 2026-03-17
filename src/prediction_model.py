from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(data):
    
    X = data[["Tasks_Assigned", "Deadlines"]]
    y = data["Hours_Worked"]
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    model = LinearRegression()
    model.fit(X_train,y_train)

    predictions = model.predict(X_test)

    return model,predictions