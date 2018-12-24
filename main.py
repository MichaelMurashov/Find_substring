# This Python file uses the following encoding: utf-8

import naive
import random
import matplotlib.pyplot as plt
import time

plt.style.use('ggplot')


def print_results(rand_res, text_res):
    lens, res_kmp, res_naive, res_rk = [], [], [], []

    for i in rand_res:
        lens.append(i[0])
        res_kmp.append(i[1])
        res_rk.append(i[2])
        res_naive.append(i[3])

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    ax1.plot(lens, res_kmp, 'green', label='kmp')
    ax1.plot(lens, res_naive, 'red', label='naive')
    ax1.plot(lens, res_rk, 'blue', label='rabin_karp')
    ax1.legend()
    ax1.set_xlabel('len')
    ax1.set_ylabel('time')
    ax1.set_title('random')

    lens, res_kmp, res_naive, res_rk = [], [], [], []

    for i in text_res:
        lens.append(i[0])
        res_kmp.append(i[1])
        res_rk.append(i[2])
        res_naive.append(i[3])

    ax2.plot(lens, res_kmp, 'green', label='kmp')
    ax2.plot(lens, res_naive, 'red', label='naive')
    ax2.plot(lens, res_rk, 'blue', label='rabin_karp')
    ax2.legend()
    ax2.set_xlabel('len')
    ax2.set_ylabel('time')
    ax2.set_title('text')

    plt.show()


def main(is_text, max_len):
    text = ''
    if is_text:
        text = open('book.txt', encoding='utf-8').read(max_len)
        # pattern = 'Анна Павловна'
    else:
        items = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        random.seed(time.time())
        for i in range(max_len):
            text += random.choice(items)

    start = random.randint(0, int(len(text)/5))
    pattern = text[start:int(len(text)/5)]

    print(len(pattern))
    res_kmp, time_kmp = naive.kmp(text, pattern)
    print('kmp          ', res_kmp, time_kmp)
    #
    res_rk, time_rk = naive.rabin_karp(text, pattern, d=10, q=(pow(2, 31) - 1))
    print('rabin_karp   ', res_rk, time_rk)
    #
    res_naive, time_naive = naive.naive(text, pattern)
    print('naive        ', res_naive, time_naive)

    print()

    return len(text)+len(pattern), time_kmp, time_rk, time_naive, res_kmp, res_rk, res_naive
    # return 0


if __name__ == '__main__':
    count = 5
    random_results, text_results = [], []
    for j in range(1, count + 1):
        print(' ===== ', j, ' ===== ')
        random_results.append(main(is_text=False, max_len=(j * 100000)))
        text_results.append(main(is_text=True, max_len=(j * 100000)))

    print_results(random_results, text_results)
