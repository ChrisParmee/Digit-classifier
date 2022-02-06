# Digit-classifier
This is a repository for code for a machine learning code to classify digits.
The code is available as Jupyter notebooks or as standard python files.

The first code (?.ipynb or ?.py) trains and saves the model. 
Either a dense neural network or CNN can be trained on the data, and the output for both models was submitted the the Kaggle competition 'Digit recognizer'.
In this competition, the dense neural network had a 95% accuracy on the data, while the CNN performed better with a 98% accuracy.

The second code (?.ipynb or ?.py) loads in the saved model and has an interactive widget where a user can draw a number.
The code then scales the number to an appropriate size and feeds it into the saved trained neural network to get a prediction.
As was found for the Kaggle competition, the CNN model tends to perform much better when classifying the drawings.
If the model correctly predicts the drawn number, this is an option to save the image and label for use in later training if needed.
