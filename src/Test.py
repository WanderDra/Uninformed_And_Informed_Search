from Dijkstra import dijkstra
from Astar import astar
from multiprocessing import Pool


def test():
    right = 0
    count = 0
    d_better = 0
    a_better = 0
    for i in range(1, 200):
        d = dijkstra(0, i)
        a = astar(0, i)
        print(d, '----', a)
        if a == d:
            right += 1
        elif a > d:
            d_better += 1
        elif a < d:
            a_better += 1
        count += 1
    accuracy = right / count
    print(accuracy, '--', a_better, '--', d_better)


if __name__ == '__main__':
    a_result = []
    d_result = []
    test_range = range(1, 1000)
    ap = Pool(len(test_range))
    for i in test_range:
        a_result.append(ap.apply_async(astar, (i, )))
    dp = Pool(len(test_range))
    for i in test_range:
        d_result.append(dp.apply_async(dijkstra, (i, )))

    ap.close()
    ap.join()
    dp.close()
    dp.join()

    af_result = []
    df_result = []
    for res in a_result:
        af_result.append(res.get())
    for res in d_result:
        df_result.append(res.get())

    right = 0
    count = 0
    d_better = 0
    a_better = 0
    for i in range(0, 999):
        if af_result[i] == df_result[i]:
            right += 1
        elif af_result[i] > df_result[i]:
            d_better += 1
            print(count)
        elif af_result[i] < df_result[i]:
            a_better += 1
            print(count)
        count += 1
    accuracy = right / count
    print('----------------------------------------------------------------------------')
    print(accuracy, '--', a_better, '--', d_better)

