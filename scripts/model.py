from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
from pathlib import Path
import json
import time
from joblib import load

def train_and_save():
    digits = load_digits()
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=100)

    start_time = time.time()
    clf.fit(X_train, y_train)
    end_time = time.time()

    train_acc = accuracy_score(y_train, clf.predict(X_train))
    test_acc = accuracy_score(y_test, clf.predict(X_test))

    Path("model").mkdir(exist_ok=True)
    dump(clf, "model/mnist_model.joblib")
    print("✅ Model trained and saved to model/mnist_model.joblib")

    # Create docs directory for GitHub Pages
    Path("docs").mkdir(exist_ok=True)

    training_log = {
        "n_estimators": clf.n_estimators,
        "train_accuracy": train_acc,
        "test_accuracy": test_acc,
        "training_time_seconds": round(end_time - start_time, 4)
    }





def predict():
 
    digits = load_digits()
    _, X_test, _, y_test = train_test_split(
        digits.data, digits.target, test_size=0.2, random_state=42
    )

    model = load("model/mnist_model.joblib")
    y_pred = model.predict(X_test[1].reshape(1, -1))

  

    print("📊 prediction:")
    print(y_pred)

    



if __name__ == "__main__":
    train_and_save()
    predict()
