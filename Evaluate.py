import Preprocess
import Dependencies



#Testing the accuracy of the trained model. 

model = Preprocess.model 
X = Preprocess.X
Y = Preprocess.Y
X_t = Preprocess.X_t
Y_t = Preprocess.Y_t




#1) Testing accuracy of the model with the train dataset 
xPrediction = model.predict(X)
accuracyScore = Dependencies.accuracy_score(xPrediction, Y)

print("Accuracy score of training data: ", accuracyScore)



#2) Testing accuracy of the model with the test dataset 
xPrediction = model.predict(X_t)
accuracyScore = Dependencies.accuracy_score(xPrediction, Y_t)

print("Accuracy score of testing data: ", accuracyScore)



