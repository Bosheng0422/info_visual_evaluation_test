from matplotlib import pyplot as plt
import numpy as np
import random
import time


def create_data():

    # 10 group data / 10 value per group
    # range of number of x from 10 to 25
    data_list = [x_random() for i in range(1, 11)]
    return data_list

def x_random():
    num_x = random.randint(10,20)
    x_list = []
    # randomly arrange the range of x
    for i in range(0,num_x+1):
        x_list.append(random.randint(1,20));
    num_random = random.randint(1,5)
    # randomly give graph data None
    for i in range(1,num_random+1):
        chose_x = random.randint(0,num_x)
        while(x_list[chose_x] is None):
            chose_x = random.randint(0,num_x)
        x_list[chose_x] = None
    return x_list


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

# get the answer from the participants and
def answer_question(answer):

    pass


if __name__ == '__main__':
    data_list = create_data()
    print(data_list)
    plt.ion()
    create_line_chart(data_list)
    create_plot_chart(data_list)
    plt.close()
    plt.ioff()
    plt.show()
