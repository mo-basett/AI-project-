import pandas as pd
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

decision_tree = pickle.load(open("DT.pkl", "rb"))
pca = pickle.load(open("PCAX.pkl", "rb"))
MLP = pickle.load(open("MLP.pkl", "rb"))
scaler = pickle.load(open("Scaler.pkl", "rb"))

MLP_bf = np.array([0 ,1 ,4 ,5 ,6 ,7])
# DT_bf=np.array([0 ,2 ,5 ,6 ,7])

def printt():
    printview=[ ]
@app.route("/predict", methods=["POST"])
def prediction():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    x = scaler.transform(query_df)
    x = pca.transform(x)
    answers_DT = []
    answers_MLP = []
    for i in x:
        res = decision_tree.predict([i])
        if res == 0:
            res = "B"
        else:
            res = "M"
        answers_DT.append(res)
        res2 = MLP.predict([i])
        res2 = np.round(res2).astype(int)
        if res2 == 0:
            res2 = "B"
        else:
            res2 = "M"
        answers_MLP.append(res2)

    return jsonify({"Decision Tree": answers_DT, "MLP": answers_MLP})


if __name__ == "__main__":
    app.run()







# import pandas as pd
# import pickle
# import numpy as np
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# decision_tree = pickle.load(open("DT.pkl", "rb"))
# pca = pickle.load(open("PCAX.pkl", "rb"))
# MLP = pickle.load(open("MLP.pkl", "rb"))
# scaler = pickle.load(open("Scaler.pkl", "rb"))

# MLP_bf = np.array([0 ,1 ,4 ,5 ,6 ,7])
# # DT_bf=np.array([0 ,2 ,5 ,6 ,7])


# @app.route("/predict", methods=["POST"])
# def prediction():
#     json_ = request.json
#     query_df = pd.DataFrame(json_)
#     x = scaler.transform(query_df)
#     x = pca.transform(x)
#     answers_DT = []
#     answers_MLP = []
#     for i in x:
#         res = decision_tree.predict([i])
#         if res == 0:
#             res = "B"
#         else:
#             res = "M"
#         answers_DT.append(res)
#         res2 = MLP.predict([i])
#         res2 = np.round(res2).astype(int)
#         if res2 == 0:
#             res2 = "B"
#         else:
#             res2 = "M"
#         answers_MLP.append(res2)

#     return jsonify({"Decision Tree": answers_DT, "MLP": answers_MLP})


# if __name__ == "__main__":
#     app.run()    