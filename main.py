from matplotlib import pyplot as plt
import numpy as np
import random
import time


def create_data():
    number_list = []
    for i in range(1, 21):
        number_list.append(i)
    number_list.append(None)
    data_list = [[number_list[random.randint(0, 20)] for j in range(1, 11)] for i in range(1, 11)]
    return data_list


def save_data_as_csv():
    pass


def create_line_chart(data_list):
    for data in data_list:
        x = range(len(data))

        plt.plot(x, data, linestyle='-')
        starttime = time.time()
        a = input("input:")
        print(time.time() - starttime)
        plt.clf()
        plt.pause(1)


def create_plot_chart(data_list):
    for data in data_list:
        x = range(len(data))

        plt.scatter(x, data)
        starttime = time.time()
        a = input("input:")
        print(time.time() - starttime)
        plt.clf()
        plt.pause(1)


def answer_question():
    pass


if __name__ == '__main__':
    data_list = create_data()
    plt.ion()
    create_line_chart(data_list)
    create_plot_chart(data_list)
    plt.close()
    plt.ioff()
    plt.show()
