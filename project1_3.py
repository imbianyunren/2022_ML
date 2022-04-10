import numpy as np
import matplotlib.pyplot as plt
import random


def rand(m, b, len, rand_points):
    half = int(rand_points/2)
    x_arr, y_arr, labels, mislabels = np.array(
        []), np.array([]), np.array([]), np.array([])
    for i in range(0, rand_points-1, half):
        x = np.random.randint(0, len, half)
        e = np.random.randint(1, len, half)

        if i < half:
            y = m * x + b - e
            labels = np.append(labels, np.ones(half, dtype=int))
            mislabels = np.append(mislabels, np.ones(half-50, dtype=int))
            mislabels = np.append(mislabels, -1*np.ones(50, dtype=int))
        else:
            y = m * x + b + e
            labels = np.append(labels, -1*np.ones(half, dtype=int))
            mislabels = np.append(mislabels, np.ones(50, dtype=int))
            mislabels = np.append(mislabels, -1*np.ones(half-50, dtype=int))
        x_arr = np.append(x_arr, x)
        y_arr = np.append(y_arr, y)
    # print(labels[999],mislabels[999])
    return x_arr, y_arr, labels, mislabels


def sign(z):
    if z > 0:
        return 1
    else:
        return -1

def check_cor(w, wt, x_arr, y_arr, labels):
    mistake_t = 0
    mistake = 0
    for i in range(0, 1999):
        xn = [1., x_arr[i], y_arr[i]]
        yn = labels[i]
        if sign(np.dot(w, xn)) != yn:
            mistake += 1
        if sign(np.dot(wt, xn)) != yn:
            mistake_t += 1
    # print(mistake, mistake_t)
    if mistake > mistake_t:
        return 1
    else:
        return 0


def check_mis(w, wt, x_arr, y_arr, mislabels):
    mistake_t = 0
    mistake = 0
    for i in range(0, 1999):
        xn = [1., x_arr[i], y_arr[i]]
        yn = mislabels[i]
        if sign(np.dot(w, xn)) != yn:
            mistake += 1
        if sign(np.dot(wt, xn)) != yn:
            mistake_t += 1
    # print(mistake, mistake_t)
    if mistake > mistake_t:
        return 1
    else:
        return 0

def accu(x_arr,y_arr,w,labels):
    mistake_f = 0
    for i in range(0, 1999):
        xn = [1., x_arr[i], y_arr[i]]
        yn = labels[i]
        if sign(np.dot(w, xn)) != yn:
            mistake_f += 1
    # print("mislabel: "+str(mistake_f))
    accuracy = 1 - (mistake_f/2000)
    return accuracy, mistake_f

def perceptron_label(x_arr, y_arr,labels):
    print("POCKET CORRECT LABEL START")
    xn = np.array([])
    wtt = np.array([0., 0., 0.])
    yn = 0
    w = np.array([0., 0., 0.])
    error = 1
    loop = 0
    while error != 0 and loop < 1000:
        error = 0
        for i in range(0, 1999) :
            if(loop >= 1000): 
                break
            xn = [1., x_arr[i], y_arr[i]]
            yn = labels[i]
            if sign(np.dot(w, xn)) != yn:
                error += 1
                loop += 1
                # print(i, loop, w)
                wtt = w + yn*np.array(xn)
                c = check_cor(w, wtt, x_arr, y_arr, labels)
                if c == 1:
                    w = wtt

    accuracy,mistake_f = accu(x_arr,y_arr,w,labels)

    print("Correct_label_loop: "+str(loop))
    print("Correct_label_mistakes: "+str(mistake_f))
    print("Correct_label_accuracy: "+str(accuracy))

    x_final = np.linspace(-5, 30)
    y_final = (-w[1]/w[2]) * x_final - (w[0]/w[2])
    print("Correct_label_equation:\n"+"y = " + str(-w[1]/w[2])+"x + "+str(-(w[0]/w[2])))
    # print(labels[999],mislabels[999])
    return w, x_final, y_final

def perceptron_mislabel(x_arr, y_arr, mislabels,labels):
    print("POCKET MISLABEL START")
    xn = np.array([])
    wtt = np.array([0., 0., 0.])
    yn = 0
    w = np.array([0., 0., 0.])
    error = 1
    loop = 0
    while error != 0 and loop < 1000:
        error = 0
        for i in range(0, 1999) :
            if(loop >= 1000): 
                break
            xn = [1., x_arr[i], y_arr[i]]
            yn = mislabels[i]
            if sign(np.dot(w, xn)) != yn:
                error += 1
                loop += 1
                wtt = w + yn*np.array(xn)
                c = check_mis(w, wtt, x_arr, y_arr, mislabels)
                if c == 1:
                    w = wtt

    # print(w)
    accuracy,mistake_f = accu(x_arr,y_arr,w,labels)
    accuracy_1,mistake_f_1 = accu(x_arr,y_arr,w,mislabels)
    print("mislabel_loop: "+str(loop))
    print("label_mistake: "+str(mistake_f))
    print("label_accuracy: "+str(accuracy))
    print("mislabel_mistake: "+str(mistake_f_1))
    print("mislabel_accuracy: "+str(accuracy_1))

    x_final = np.linspace(-5, 30)
    y_final = (-w[1]/w[2]) * x_final - (w[0]/w[2])
    print("mislabel_equation:\n"+"y = " + str(-w[1]/w[2])+"x + "+str(-(w[0]/w[2])))
    # print(labels[999],mislabels[999])
    return w, x_final, y_final


if __name__ == '__main__':
    m, b = 2,5 
    rand_points = 2000
    len = 30
    half = int(rand_points/2)

    x = np.linspace(-5, 30, 1000)   # x = [0, 1,..., rand_param]
    y = m * x + b
    print("original:\ny = "+str(m)+"x + "+str(b))

    x_arr, y_arr, labels, mislabels = rand(m, b, len, rand_points)
    f1 = plt.figure(1)
    plt.plot(x, y, 'g')
    plt.plot(x_arr[:half], y_arr[:half], 'o', color='blue')
    plt.plot(x_arr[half:], y_arr[half:], 'x', color='red')
    plt.xlim(-5, 30)
    f2 = plt.figure(2)
    w, x_final_M, y_final_M = perceptron_mislabel(x_arr, y_arr, mislabels,labels) 
    w, x_final_L, y_final_L = perceptron_label(x_arr, y_arr, labels) 
    plt.plot(x_arr[:half-50], y_arr[:half-50], 'o', color='blue')
    plt.plot(x_arr[half-49:half], y_arr[half-49:half], 'x', color='orange')
    plt.plot(x_arr[half+51:], y_arr[half+51:], 'x', color='red')
    plt.plot(x_arr[half+1:half+50], y_arr[half+1:half+50], 'o', color='green')
    plt.plot(x, y, 'green')
    plt.plot(x_final_M, y_final_M, 'purple')
    plt.plot(x_final_L, y_final_L, 'orange')
    plt.xlim(-5, 30)
    plt.show()
