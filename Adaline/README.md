## 🧠 About the Models

This project implements two classic linear models for binary classification:

---

### 🔹 Adaline (Adaptive Linear Neuron)

Adaline is one of the earliest neural models that builds the foundation for more complex networks. Unlike the Perceptron, which uses a step function during training, Adaline uses a **linear activation function** and optimizes a **continuous cost function** (Sum of Squared Errors).

#### 🔧 How It Works:
- Adaline computes the **net input** as a weighted sum of inputs.
- It uses a **linear activation function** (identity): `activation(x) = x`.
- The **error** is computed between the model's output and the true label:  
  \[
  error = y - \hat{y}
  \]
- It minimizes the **Sum of Squared Errors (SSE)** over the entire training set using **Batch Gradient Descent**.
- Weights are updated as:
  \[
  w_j := w_j + \eta \cdot \sum_i (y^{(i)} - \hat{y}^{(i)}) \cdot x_j^{(i)}
  \]
  where:
  - \( \eta \) is the learning rate,
  - \( x_j^{(i)} \) is the j-th feature of the i-th sample,
  - \( \hat{y}^{(i)} \) is the model output (net input),
  - \( y^{(i)} \) is the true label.

#### ✅ Strengths:
- Smooth convergence due to differentiable cost function
- Stable updates, especially on small to medium datasets
- Strong educational foundation for learning optimization and neural nets

---

### 🔹 Stochastic Adaline (SGD Variant)

Stochastic Adaline follows the same fundamental architecture but uses **Stochastic Gradient Descent (SGD)** for training, making it more scalable and responsive.

#### 🔧 How It Works:
- Instead of updating weights after the entire batch (epoch), it updates **after each individual sample**.
- Each sample contributes to a **small, noisy gradient update**:
  \[
  w_j := w_j + \eta \cdot (y^{(i)} - \hat{y}^{(i)}) \cdot x_j^{(i)}
  \]
- The dataset is **shuffled every epoch** to avoid cyclic patterns.
- The cost is averaged per sample, and tracked for each epoch to visualize convergence.

#### ⚡ Benefits:
- Faster convergence for large datasets
- Better exploration of the loss surface (due to noise)
- More realistic simulation of online learning environments

---

### 🔍 Comparison Summary

| Feature               | Adaline (Batch GD)     | Stochastic Adaline (SGD) |
|----------------------|------------------------|---------------------------|
| Update Frequency     | Once per epoch         | Once per sample           |
| Convergence Speed    | Slower                 | Faster (with variance)    |
| Memory Efficiency    | Lower                  | Higher (good for big data)|
| Loss Function        | SSE                    | SSE (per sample)          |
| Activation Function  | Linear (identity)      | Linear (identity)         |
| Stability            | High                   | Noisier                   |

---

### 📚 Use Cases

These models are well-suited for:
- Educational purposes to understand core ML concepts
- Simple linear classification tasks
- Building blocks for more complex models like MLPs
- Demonstrating optimization strategies in neural networks

---

### 📈 Visualization

During training, the models track and visualize **Sum of Squared Errors** across epochs. This provides insights into:
- Learning rate effectiveness
- Convergence behavior
- Overfitting or underfitting trends

---

### 🧪 Practical Implementation

In this project:
- The **Iris dataset** is used for binary classification (excluding class 2).
- Features are standardized for faster convergence.
- The model is evaluated using `accuracy_score` and training loss plots.
- Both Adaline variants are tested under the same conditions for comparison.

---

