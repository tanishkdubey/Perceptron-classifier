🧠 Perceptron from Scratch with Decision Boundary Visualization
This project demonstrates a simple implementation of the Perceptron algorithm from scratch in Python, using NumPy for vector operations and Matplotlib for visualization.

It uses a synthetically generated binary classification dataset (make_classification) from sklearn.datasets with:

2 features (1 informative, 1 noise-free)

Well-separated classes

No hypercube structure for cleaner visualization

🚀 What This Code Does
📊 Generates a dataset of 100 samples with clearly separable classes using make_classification.

🧠 Implements the Perceptron algorithm manually using a simple step activation function and stochastic weight updates.

🔺 Plots the decision boundary learned by the perceptron after training.

🎨 Visualizes the data points by class:

Blue → Class 0 (Negative)

Green → Class 1 (Positive)

Red line → Decision boundary

📈 Algorithm Highlights
The Perceptron function adds a bias term to the features.

It uses stochastic updates (1 random point per epoch).

After training, the learned weights are used to plot the decision boundary in 2D space.

📎 Example Output
A clean scatter plot showing both classes

A red linear boundary separating the two classes

Output of weights, slope, and y-intercept printed in console

🧩 Requirements
bash
Copy code
pip install numpy matplotlib scikit-learn
🔍 Why It Matters
This mini-project is ideal for:

Understanding the mathematics behind the Perceptron

Seeing how weights affect decision boundaries

Building intuition for linear classifiers

