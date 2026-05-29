from sklearn.model_selection import cross_val_score

def evaluate(model, X, y):

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5
    )

    print(
        "Accuracy:",
        scores.mean(),
        "+/-",
        scores.std()
    )
