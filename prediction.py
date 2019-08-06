import pickle
def makeTokens(f):
    tokens = []
    for i in f:
        tokens.append(i)
    return tokens
def get_security(password):
    model = pickle.load(open('seq_model.sav', 'rb'))
    vectorizer = pickle.load(open('vectorizer.sav', 'rb'))
    X_predict = []
    X_predict.append(password)
    X_predict = vectorizer .transform(X_predict)
    y_Predict = model.predict_classes(X_predict)
    return int(y_Predict)


