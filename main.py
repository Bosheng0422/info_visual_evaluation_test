from matplotlib import pyplot as plt
import numpy as np
import random
import time


def create_data():
    number_list = []
    for i in range(1, 21):
        number_list.append(i)
    number_list.append(None)
    data_list = [[number_list[random.randint(0, 20)] for j in range(1, 11)] for i in range(1, 21)]
    return data_list


def save_data_as_csv():
    pass


def create_line_chart(data):
    x = range(len(data))
    plt.plot(x, data, linestyle='-')

    answer, response_time = answer_question(data)

    plt.clf()
    plt.pause(1)

    return answer, response_time


def create_plot_chart(data):
    x = range(len(data))
    plt.scatter(x, data)

    answer, response_time = answer_question(data)

    plt.clf()
    plt.pause(1)

    return answer, response_time


def create_graph(data_list):
    plt.ion()
    data_indexes = []
    for i in range(0, 20):
        data_indexes.append(i)
    random.shuffle(data_indexes)

    record_list = []
    for index in data_indexes:
        single_record = []
        if index > 9:
            answer, response_time = create_line_chart(data_list[index])
            single_record.append("line chart")
        else:
            answer, response_time = create_plot_chart(data_list[index])
            single_record.append("plot chart")
        single_record.append(answer)
        single_record.append(response_time)
        record_list.append(single_record)
    plt.close()
    plt.ioff()
    plt.show()

    return record_list


def answer_question(data):
    start_time = time.time()
    number = input("How many missing value in this chart:")
    response_time = time.time() - start_time
    correct_number = 0
    answer = False
    for y_data in data:
        if y_data is None:
            correct_number += 1
    if int(number) == correct_number:
        answer = True

    return answer, response_time


if __name__ == '__main__':
    username = input("Input your user name: ")
    data_list = create_data()
    record_list = create_graph(data_list)
    print(record_list)


