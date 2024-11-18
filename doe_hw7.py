import numpy as np
import matplotlib.pyplot as plt

# Define the matrix X
X = np.array([
    [1, -1, -1, -1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, 1, 1, -1],
    [1, -1, -1, 1],
    [1, 1, -1, 1],
    [1, -1, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
])

# Define the matrix y
y = np.array([32, 46, 57, 65, 36, 48, 57, 68, 50, 44, 53, 56])


# Calculate X^T
X_T = X.T

# Calculate X^T X
XTX = np.dot(X_T, X)

# Compute the inverse of X^T X
try:
    XTX_inv = np.linalg.inv(XTX)
    #print("The inverse of (X^T X) is:")
    #print(XTX_inv)
except np.linalg.LinAlgError:
    print("(X^T X) is not invertible.")

XTy = np.dot(X.T, y)
# Calculate zone
## Calculate estimated_slope
b = np.dot(XTX_inv, XTy)

## Calculate SS_R, SS_E, SS_T
k = np.shape(X)[1] - 1 # A number of variables [factors], not include constant
n = np.shape(X)[0]
SS_R = round(np.dot(b.T,np.dot((X.T),y)) - np.sum(y)**2 / np.shape(y)[0], 3)
SS_E = round(np.dot(y.T, y) - np.dot(b.T, np.dot(X.T, y)), 3)
SS_T = round(np.dot(y.T, y) - np.sum(y)**2 / np.shape(y)[0], 3)
print(f'SSR = {SS_R}, SSE = {SS_E}, SST = {SS_T}')
print(f'degree of freedom = {k}, {n - k - 1}, {n - 1}, respectively')
print("#------------------------------------------#")

## Calculate MS_R, MS_E, MS_T
MS_R = round(SS_R / k, 3)
MS_E = round(SS_E / (n - k - 1), 3)
print(f'MSR = {MS_R}, MSE = {MS_E}')
print(f'F_ob = {round(MS_R / MS_E, 3)}')
print("#------------------------------------------#")

## Calculate R - sq
R_sq = round(SS_R / SS_T, 3)
R_sq_adj = round(1 - ((n - 1)/(n - k - 1))*(1 - R_sq**2), 3)
print(f'R - sq = {R_sq}')
print(f'R - sq - adjusted = {R_sq_adj}')
print("#------------------------------------------#")

## Calculate T ob
count = 0
for slope in b:
    se_b = round((MS_E * XTX_inv[count, count])**0.5, 3)
    t_ob = round(slope / se_b, 3)
    print(f'C_jj = {XTX_inv[count, count]}')
    print(f'Term b{count}: ({slope}, {se_b}, {t_ob}')
    count += 1

## Calculate Error of predicted
predicted = np.dot(X,b)
error = y - predicted
sort_error = sorted(error)

### Normally distributed of error
p_k = [(k-0.5)/12 for k in range (0, n)]
plt.title("Normality plot of residuals")
plt.scatter(x = p_k, y = error)
plt.show()
