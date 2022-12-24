# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from euller_beam import *
# add h to global and import it

def mean_squared_error(y_true, y_predicted):
    
    # Calculating the loss or cost
    cost = np.sum((y_true-y_predicted)**2) / len(y_true)
    return cost

h = 10

def f(v_x_anchor):
    dx = 0.001
    beam = clBeam(h , 90)
    vvc = beam.vvc_get(v_x_anchor)
    ix = 0
    x = 0
    m = 0
    while x <= h:
        iInterval=beam.iInterval_get(x,v_x_anchor)
        vc = vvc[iInterval*4:iInterval*4 + 4]
        w2=beam.ww2(x,vc)
        if ix == 0 or abs(w2) > m :
            m = abs(w2)
        x += dx
        ix += 1

    return m*beam.E_Ic



def ggg(vx):
    return (vx[0] - 2)**2 + (vx[1] - 5)**2 

def test():
    vx = [0,0]
    f_min, vx_best = gradient_descent(vx, ggg, True, 0.001)
    print(f"f_min = {f_min}")
    print(f"vx_best = {vx_best}")
    return

def test_wall(n):
    vx = init_solution(n)
    f_min, vx_best = gradient_descent(vx, f, True, 1)
    print(f"f_min = {f_min}")
    print(f"vx_best = {vx_best}")
    return


def init_solution(n):
    dx = h/n
    vx = []

    for i in range(n):
        vx.append(dx*(i + 1))

    return vx

def gradient_descent(vx, f, b_min, dx):
    f0 = f(vx)
    dx_min = 0.01
    n = len(vx)
    while dx > dx_min:
            
        b = True
        while b:
            vdf = []
            y = 0

            for i in range(n):
                vxi = []

                for j in range(n):
                    vxi.append(vx[j])
                
                vxi[i] += dx
                dy = (f(vxi) - f0) / dx
                y += dy**2
                vdf.append(dy)
            
            y = y**0.5
            vx_new = []
            sign = -1 if b_min else 1
            
            for i in range(n):
                vx_new.append(vx[i] + sign * dx * vdf[i] / y)
            
            f1 = f(vx_new)
            if b_min:
                b = f1 < f0
            else:
                b = f1 > f0

            if b:
                f0 = f1
                vx = vx_new

        dx = dx / 2

    return f0, vx
            






# # Gradient Descent Function
# # Here iterations, learning_rate, stopping_threshold
# # are hyperparameters that can be tuned
# def gradient_descent(x, f, iterations = 1000, learning_rate = 0.0001,
#                     stopping_threshold = 1e-6):

#     # Initializing weight, bias, learning rate and iterations
#     current_weight = 0.1
#     current_bias = 0.01
#     iterations = iterations
#     learning_rate = learning_rate
#     n = float(len(x))
    
#     costs = []
#     weights = []
#     previous_cost = None

#     # Estimation of optimal parameters
#     for i in range(iterations):

#         # Making predictions
#         y_predicted = (current_weight * x) + current_bias
        
#         # Calculating the current cost
#         current_cost = mean_squared_error(y, y_predicted)

#         # If the change in cost is less than or equal to
#         # stopping_threshold we stop the gradient descent
#         if previous_cost and abs(previous_cost-current_cost)<=stopping_threshold:
#             break
        
#         previous_cost = current_cost

#         costs.append(current_cost)
#         weights.append(current_weight)
        
#         # Calculating the gradients
#         weight_derivative = -(2/n) * sum(x * (y-y_predicted))
#         bias_derivative = -(2/n) * sum(y-y_predicted)

#         # Updating weights and bias
#         current_weight = current_weight - (learning_rate * weight_derivative)
#         current_bias = current_bias - (learning_rate * bias_derivative)

#         # Printing the parameters for each 1000th iteration
#         print(f"Iteration {i+1}: Cost {current_cost}, Weight \
#         {current_weight}, Bias {current_bias}")
    
    
#     # Visualizing the weights and cost at for all iterations
#     plt.figure(figsize = (8,6))
#     plt.plot(weights, costs)
#     plt.scatter(weights, costs, marker='o', color='red')
#     plt.title("Cost vs Weights")
#     plt.ylabel("Cost")
#     plt.xlabel("Weight")
#     plt.show()
    
#     return current_weight, current_bias


def main():
    test_wall(1)
    # # Data
    # X = [anchor places]
    # Y = max

    # # Estimating weight and bias using gradient descent
    # estimated_weight, estimated_bias = gradient_descent(X, Y, iterations=2000)
    # print(f"Estimated Weight: {estimated_weight}\nEstimated Bias: {estimated_bias}")

    # # Making predictions using estimated parameters
    # Y_pred = estimated_weight*X + estimated_bias

    # # Plotting the regression line
    # plt.figure(figsize = (8,6))
    # plt.scatter(X, Y, marker='o', color='red')
    # plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='blue',markerfacecolor='red',
    #         markersize=10,linestyle='dashed')
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.show()

	
if __name__=="__main__":
	main()
