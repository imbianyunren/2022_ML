import numpy as np
import matplotlib.pyplot as plt
import random
import time

def rand(m, b, len, rand_points):
    half = int(rand_points/2)
    x_arr, y_arr, labels = np.array([], dtype=float), np.array(
        [], dtype=float), np.array([])
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
    if z > 0:
        return 1
    else:
        return -1


def check(w, wt, x_arr, y_arr, labels):
    mistake_t = 0
    mistake = 0
    for i in range(0, 1999):
        xn = [1., x_arr[i], y_arr[i]]
        yn = labels[i]
        if sign(np.dot(w, xn)) != yn:
            mistake += 1
        if sign(np.dot(wt, xn)) != yn:
            mistake_t += 1
    # accu_t = 1 - (mistake_t/2000)
    # accu = 1 - (mistake/2000)
    # print(mistake, mistake_t)
    if mistake > mistake_t:
        return 1
    else:
        return 0

def perceptron_PLA(x_arr, y_arr, labels):
    xn = np.array([])
    yn = 0
    w = np.array([0., 0., 0.])
    error = 1
    loop = 0
    start = time.time()
    while error != 0:
        error = 0
        for i in range(0, 1999):
            xn = [1., x_arr[i], y_arr[i]]
            yn = labels[i]
            if sign(np.dot(w, xn)) != yn:
                error += 1
                loop += 1
                w += yn*np.array(xn)
    end = time.time()        
    print("PLA exe_time: " + str(end-start)+"s")
    x_final = np.linspace(-5, 30)
    y_final = (-w[1]/w[2]) * x_final - (w[0]/w[2])
    # print("PLA equation:\n")
    str_PLA = "y = " + str(-w[1]/w[2])+"x + "+str(-(w[0]/w[2]))
    return w, x_final, y_final,loop,str_PLA

def perceptron_POCKET(x_arr, y_arr, labels):
    xn = np.array([])
    wtt = np.array([0., 0., 0.])
    yn = 0
    w = np.array([0., 0., 0.])
    error = 1
    loop = 0
    start = time.time()
    while error != 0 and loop < 1000:
        error = 0
        for i in range(0, 1999):
            # if(loop >= 1000): 
            #     break
            xn = [1., x_arr[i], y_arr[i]]
            yn = labels[i]
            if sign(np.dot(w, xn)) != yn:
                error += 1
                loop += 1
                # wtt = w + yn*np.array(xn)*0.001
                wtt = w + yn*np.array(xn)
                c = check(w, wtt, x_arr, y_arr, labels)
                if c == 1:
                    w = wtt
    end = time.time()        
    print("POCKET exe_time: " + str(end-start)+"s")
    mistake_f = 0
    for i in range(0, 1999):
        xn = [1., x_arr[i], y_arr[i]]
        yn = labels[i]
        if sign(np.dot(w, xn)) != yn:
            mistake_f += 1
    accu = 1 - (mistake_f/2000)

    # print("iteration: "+str(loop))
    # print("accuracy: "+str(accu))
    x_final = np.linspace(-5, 30)
    y_final = (-w[1]/w[2]) * x_final - (w[0]/w[2])
    str_POCKET = "y = " + str(-w[1]/w[2])+"x + "+str(-(w[0]/w[2]))
    # print("y = " + str(-w[1]/w[2])+"x + "+str(-(w[0]/w[2])))
    return w, x_final, y_final,loop,accu,str_POCKET


if __name__ == '__main__':
    m, b = 2, 1
    rand_points = 2000
    len = 30
    half = int(rand_points/2)

    x = np.linspace(-5, 30, 1000)   # x = [0, 1,..., rand_param]
    y = m * x + b
    print("original:\ny = "+str(m)+"x + "+str(b))

    x_arr, y_arr, labels = rand(m, b, len, rand_points)
    f1 = plt.figure(1)
    plt.plot(x, y, 'g')
    plt.plot(x_arr[:half], y_arr[:half], 'o', color='blue')
    plt.plot(x_arr[half:], y_arr[half:], 'x', color='red')
    plt.xlim(-5, 30)

    f2 = plt.figure(2)
    w, x_final, y_final,loop_PLA,str_PLA = perceptron_PLA(x_arr, y_arr, labels)
    print("PLA_iteration: "+str(loop_PLA))
    print(str_PLA)
    plt.plot(x_arr[:half], y_arr[:half], 'o', color='blue')
    plt.plot(x_arr[half:], y_arr[half:], 'x', color='red')
    plt.plot(x, y, 'g')
    plt.plot(x_final, y_final, 'orange')
    plt.xlim(-5, 30)

    f3 = plt.figure(3)
    w, x_final, y_final,loop_POCKET,accu,str_POCKET = perceptron_POCKET(x_arr, y_arr, labels)
    plt.plot(x_arr[:half], y_arr[:half], 'o', color='blue')
    plt.plot(x_arr[half:], y_arr[half:], 'x', color='red')
    plt.plot(x, y, 'g')
    plt.plot(x_final, y_final, 'orange')
    plt.xlim(-5, 30)

    print("POCKET_iteration: "+str(loop_POCKET))
    print("POCKET_accuracy: "+str(accu))
    print(str_POCKET)
    plt.show()
