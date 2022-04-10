import numpy as np
import matplotlib.pyplot as plt
import random


def rand(m, b, len, rand_points):
    half = int(rand_points/2)
    x_arr, y_arr, labels = np.array([]), np.array([]), np.array([])
    for i in range(0, rand_points-1, half):
        x = np.random.randint(0, len, half)
        e = np.random.randint(1, len, half)

        if i < half:
            y = m * x + b - e
            labels = np.append(labels, np.ones(half, dtype=int))
        else:
            y = m * x + b + e
            labels = np.append(labels, -1*np.ones(half, dtype=int))

        # print(x, y)
        x_arr = np.append(x_arr, x)
        y_arr = np.append(y_arr, y)

    return x_arr, y_arr, labels

def sign(z):
    if z>0 :
        return 1
    else:
        return -1

def perceptron(x_arr, y_arr, labels):
    xn= np.array([])
    yn =0
    w = np.array([0.,0.,0.])
    error = 1
    loop = 0
    while(error != 0):
        error = 0
        for i in range(0,29):
            xn = [1.,x_arr[i], y_arr[i]]
            yn = labels[i]
            if sign(np.dot(w,xn)) != yn:
                loop +=1
                error +=1
                w += yn*np.array(xn)
    x_final = np.linspace(-10,50)
    y_final = (-w[1]/w[2]) * x_final - (w[0]/w[2])
    print("iteration: " + str(loop))
    print("y = " + str(-w[1]/w[2])+"x + "+str(-(w[0]/w[2])))
    return w,x_final,y_final


if __name__ == '__main__':
    m, b = 2, 1
    rand_points = 30
    len = 30
    half = int(rand_points/2)

    x = np.linspace(-10, 50, 1000)   # x = [0, 1,..., rand_param]
    y = m * x + b
    print("original:\ny = "+str(m)+"x + "+str(b))
    x_arr, y_arr, labels = rand(m, b, len, rand_points)
    f1 = plt.figure(1)
    plt.plot(x,y,'g')
    plt.plot(x_arr[:half], y_arr[:half], 'o', color='blue')
    plt.plot(x_arr[half:], y_arr[half:], 'x', color='red')
    plt.xlim(-10,50)
    # plt.ylim(-10,150)
    f2 = plt.figure(2)
    w,x_final,y_final = perceptron(x_arr, y_arr, labels)
    plt.plot(x,y,'g')
    plt.plot(x_final,y_final,'r')
    plt.plot(x_arr[:half], y_arr[:half], 'o', color='blue')
    plt.plot(x_arr[half:], y_arr[half:], 'x', color='red')
    plt.xlim(-10,50)
    # plt.ylim(-30,150)
    plt.show()
