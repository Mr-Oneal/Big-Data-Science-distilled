# Data mining

Data mining is the human activity consisting in extracting **knowledge** from data

**Data** -> anything that has been recorded

**Datasets** -> <u>***collections***</u> of items, described by a set of attribute. 



## Knowledge

Knowledge can be represented in 3 ways:

- Proposition/Statement: *Smaller animals have a faster heartbeat*

- Narrative (description / storytelling): The size of an animal seems to be related to its heartbeat. In general, larger animals...

- Model (mathematical | computer): 
  $$ {^}
  r = 235 × m^{-1/4}
  $$



Science is about **evaluating** propositions, narratives and models. In other words, science is about evaluating the **knowledge**



## Life of a model

During the life of a model, we can distinguish two stages:

1. Learning stage: The model is built.
2. Deployment (inference, production) stage: The model is used.



![Screenshot from 2019-09-24 14-05-01](/home/gerardo/Pictures/Screenshot from 2019-09-24 14-05-01.png)

## Types of variables

The basic types of variables are:

- Numeric/continuous: 
  - Real numbers (temperature, voltage, pixel intensity value).
  -  Ordering and distance are defined
- Categorical/discrete:  
  - Equality is defined. 
  - Neither ordering nor distance are defined
- Ordinal
  - <u>**Categories**</u> with ordering (low/medium/high)
  -  Ordering and distance are defined



## Mathematical and computer models

Mathematical and computer models are equivalent: mathematical models can be implemented numerically and for every computer model there is a mathematical formulation.

- Mathematical models express the relationship between features and responses by using mathematical expressions.
  $$
  y = x + 3*x^{2}
  $$

- Computer or numerical models are computer programs

*In statistics, the **mean squared error** (**MSE**) or **mean squared deviation** (**MSD**) of an estimator (of a procedure for estimating an unobserved quantity) measures the average of the squares of the error*



## Models families	

- Parametric models

  ​	have a pre-defined shape that can be adjusted by tuning a set of parameters.

- Non-parametic models

  ​	make no assumptions about the shape and have no parameters that need adjusting.

  

Non-parametric models are more flexible than parametric ones. However, they need more data and are harder to interpret.



**Hyperparameters** allow us to distinguish specific models within a family of models and shouldn't be confused with conventional parameters. (Eg: the equalizer with 5 and 8 parameters)



## Model training and testing

Data Mining approaches incorporate the following two stages:

- **Training**: Given some notion of <u>quality</u> and <u>data</u>, a model is <u>created</u>.
- **Testing**: Using <u>unseen data</u>, the quality of the model is <u>reassessed</u>.

Therefore, models need to be able to **generalise**. The situation where a model performs well for training data, but poorly for test data, is known as **overfitting**.

Model **validation** provides different techniques to select our final model. For instance, if we consider a polynomial family of models, validation allows us to set the hyperparameter (degree) and training would adjust the parameters (coefficient).



## Data Science pipeline

![Screenshot from 2019-09-24 14-58-36](/home/gerardo/Pictures/Screenshot from 2019-09-24 14-58-36.png)

Problem formulation

![Screenshot from 2019-09-24 14-59-17](/home/gerardo/Pictures/Screenshot from 2019-09-24 14-59-17.png)

### **Supervised learning**

Mathematically, our challenge is to build a model that maps one attribute x to another attribute y which we call the label, by learning from a dataset of labelled examples (xi, yi)

![Screenshot from 2019-09-24 20-17-50](/home/gerardo/Pictures/Screenshot from 2019-09-24 20-17-50.png)

Supervised learning can be further divided into two categories depending on the type of label:

- Classification: The label is a discrete variable.
  Ex: In a spam detector, label 0 means email is spam, label 1 it isn’t.
- Regression: The label is a continuous variable.
  Ex: The heart rate of an animal is a continuous label.

![Screenshot from 2019-09-24 20-21-40](/home/gerardo/Pictures/Screenshot from 2019-09-24 20-21-40.png)

### Unsupervised learning

In unsupervised learning, we set out to f<u>ind the underlying structure of our dataset</u>. Among other uses, this can be useful to gain understanding, identify anomalies, compress our data and reduce processing time.

Two main unsupervised learning techniques are:

- Clustering: Clusters of data points of similar nature are identified.
- Dimensionality reduction: Reduced set of attributes is generated.

Other techniques include outlier detection and quantile estimation

![Screenshot from 2019-09-24 20-30-04](/home/gerardo/Pictures/Screenshot from 2019-09-24 20-30-04.png)

---

## Regression

### Dataset as a table

rows -> instances (samples)

columns -> attributes(features)

Label -> one of the attributes of our dataset (missing)

predictors -> value of the remaining attributes 

Our job is then to find the best model that associates a unique label to a given set of predictors.

![Screenshot from 2019-10-01 14-17-35](/home/gerardo/Pictures/Screenshot from 2019-10-01 14-17-35.png)

**Mathematical** **notation**

![Screenshot from 2019-10-01 14-25-15](/home/gerardo/Pictures/Screenshot from 2019-10-01 14-25-15.png)

Dataset:

``````
- N is the number of samples in our dataset
- i identifies one of the samples
- xi is the predictor of sample i
- yi is the label of sample i
- The dataset is {(xi, yi) ∶ 1 ≤ i ≤ N}
``````

Model:

``````
- f(⋅) denotes our model
- yˆi = f(xi) is the label produced by f(⋅) when the predictor is xi
- ei = yi − yˆi is the prediction error for sample i
``````



### Basic regression models

#### Simple linear regression

In simple linear regression, one predictor *"x"* and one label *"y"* are considered and models are defined by the mathematical expression
$$
f(x) = w0 + w1x
$$
Lineal models are *<u>parametric</u>* and have <u>*two*</u> parameters *W0* and *W1*. The best value for these are the ones that minimize the loss function. (MSE)

#### Multiple linear regression

In multiple regression, there are <u>two or more</u> predictors.

Using vector notation, predictors can be expressed as a vector
$$
x = [1, x1, x2, . . . , xP ]^{T}
$$
where *"Xp"* denotes the p-th predictor, *P* is the number of predictors and the constant 1 is appended for convenience.

A multiple regression model can then be expressed as the function
$$
yˆ = f(x)
$$
We will use the symbol xi to denote the i-th sample in a dataset,
$$
xi = [1, xi,1, xi,2, . . . , xi,P ]^{T}
$$
where xi,p is the p-th predictor of the i-th sample

Using the proposed vector notation, linear multiple models can be expressed as:
$$
f(x) = w^{T}x = w0 + w1x1 + ⋅ ⋅ ⋅ + wP xP
$$

#### The MMSE solution for linear regression models

$$
w = (X^{T}X)^{−1}X^{T} Y
$$

In general there will not exist an analytical expression that allows us to calculate the optimal parameters of a model. Instead, we will need to use numerical optimisation (gradient descent, evolutionary algorithms, grid search...) to find the optimal parameters of a model

#### Simple polynomial regression

The general form of a polynomial regression model is:
$$
f(x) = w0 + w1x + w2x^2 + ⋅ ⋅ ⋅ + wDx^D
$$
where D is the degree of the polynomial.

### Flexibility

Flexible models allow us to generate multiple shapes by tuning their parameters.

Characteristics

- Degrees of freedom
- complexity

Linear models are inflexible, as they can only generate straight lines. They have only 2 parameters.

Cubic models are more flexible and are characterized by 4 parameters.

#### Interpretability

Model interpretability is crucial for us, as humans, to understand in a qualitative manner how a predictor is mapped to a label. Inflexible models produce solutions that are usually simpler and easier to interpret.

![Screenshot from 2019-10-01 18-31-00](/home/gerardo/Pictures/Screenshot from 2019-10-01 18-31-00.png)

#### Accuracy

The accuracy of a model is also related to its flexibility. Flexible models will have in general lower MSE than inflexible models.

![Screenshot from 2019-10-01 18-31-47](/home/gerardo/Pictures/Screenshot from 2019-10-01 18-31-47.png)

### Generalization

Generalization is the ability of our model to work well in production, in other words, to successfully translate what we have learnt during the learning stage to the production stage.

