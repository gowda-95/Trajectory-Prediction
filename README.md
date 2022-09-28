# Motion_Prediction
Predict trajectory for objects (vehicles, bicycles, pedestrians) in a trajectory dataset collected by drones howering over road intersection using models based on Artificial Neural Networks. 


## Dataset
[inD Dataset](https://www.ind-dataset.com/) is used for this study. The dataset is free for non commercial use but requires prior [registration](https://www.ind-dataset.com/#download). Download the data and place it in [dataset folder](https://github.com/gowda-95/Motion-Prediction/tree/main/dataset). 

The inD dataset was recorded by drones howering over 4 different German road intersections near the city of Aachen. The dataset includes trajectory information for object categories such as vehicles (car, truck, bus), pedestrians and bicyclists. 


## Requirements
Python version > = 3.6

PyTorch, NumPy, sklearn, Pandas. 

## Evaluation 

The following three error metrics are used to evaluate the model

1. **Average Displacement Error (ADE):** 
Average Displacement Error (ADE): ADE refers to the mean square error (MSE) over all estimated points of every trajectory and the true points.


$$
\text{ADE} = \frac
{\sum_{i=1}^{n}\sum_{t=T_{Frame}}^{T_{pred}} \quad  \big[(\hat{x}_i^t - x_i^t)^2 + (\hat{y}_i^t - y_i^t)^2 \big]}
{n(T_{pred}-(T_{Frame}+1))}
$$

2. **Final displacement error (FDE):** 
FDE means the distance between the predicted final destination and the true final destination at the $T_{pred}$ time.


$$
\text{FDE} = \frac
{\sum_{i=1}^n \sqrt{\big( \, \hat{x}_i^{T_{pred}} - x_i^{T_{pred}} \, \,\big)^2  + \big( \, \hat{y}_i^{T_{pred}} - y_i^{T_{pred}} \, \,\big)^2 }}
{n}
$$ 

3. **Average Absolute Heading Error (AHE):** 
This is a bit like ADE but we take the 1-norm of the error and we only consider the heading prediction here.


$$
\text{AHE} = \frac
{\sum_{i=1}^{n}\sum_{t=T_{Frame}}^{T_{pred}} \quad \big| \hat{y}_i^t - y_i^t \big| }
{n(T_{pred}-(T_{Frame}+1))}
$$

## Results

Recording id = 28

Epochs = 5000

|  | Custom network |
|---|--------|
|Average Displacement Error (ADE)| 2.267 m |
|Final displacement error (FDE) | 2.021 m |
|Average Absolute Heading Error (AHE)| 4.72 degrees |
