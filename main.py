from matplotlib import pyplot as plt
import csv
import random
import time
import os

def create_data():
    # 10 group data / 10 value per group
    # range of number of x from 10 to 25
    data_list = [x_random() for i in range(1, 11)]
    data_list = data_list + data_list
    return data_list

def x_random():
    num_x = random.randint(10,26)
    x_list = []
    # randomly arrange the range of x
    for i in range(0,num_x+1):
        x_list.append(random.randint(1,21))
    num_random = random.randint(1,5)
    # randomly give graph data None
    for i in range(1,num_random+1):
        chose_x = random.randint(0,num_x)
        while(x_list[chose_x] is None):
            chose_x = random.randint(0,num_x)
        x_list[chose_x] = None
    return x_list


def save_data_as_csv(record_list):
    with open("info_record.csv", "a+") as csv_file:
        writer = csv.writer(csv_file)

        # 先写入columns_name
        if not os.path.exists('info_record.csv'):
            writer.writerow(["username", "chart_type", "answer", "respose_time"])
        # 写入多行用writerows
        writer.writerows(record_list)


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


def create_graph(username, data_list):
    plt.ion()
    data_indexes = []
    for i in range(0, 20):
        data_indexes.append(i)
    random.shuffle(data_indexes)

    record_list = []
    for index in data_indexes:
        single_record = []
        single_record.append(username)
        if index > 9:
            answer, response_time = create_line_chart(data_list[index])
            single_record.append('line chart')
        else:
            answer, response_time = create_plot_chart(data_list[index])
            single_record.append('plot chart')
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
    response_time = round(response_time, 2)
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
    record_list = create_graph(username, data_list)
    save_data_as_csv(record_list)


