import statistics as stat
from math import *


def UNGROUPED():
    print("\nUNGROUPED DATA")

    j = 0
    k = 10  # only change this to adjust the number of elements per row
    r = 2  # change this to adjust the rounded places
    s = " "  # change this to adjust the input splitter


    def display_stats():
        print()
        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)
        print("Range:", _range)
        print("Sample Variance:", S_var)
        print("Sample St.Deviation:", S_stdev)
        print("Sample CV: " + str(S_CV) + "%")
        print("Population Variance:", P_var)
        print("Population St.Deviation:", P_stdev)
        print("Population CV: " + str(P_CV) + "%")
        # print("\nBased from lesson P_St.Dev: " + str(P_stdev_lesson))


    while True:
        try:
            data_input = input("\nPlease input data set: ").split(s)
            data_set = [int(a) for a in data_input]
            d_index = ceil(len(data_set) / k)
            data_rows = [[] for _ in range(d_index)]
            data_set.sort()
            divided_data = []

            for b in data_rows:
                for c in data_set[j:k]:
                    b.append(c)
                divided_data.append(b)
                j = k
                k += 10  # change this also as you change the value of k (they should bbe equal)

            print("\n\nData Set:")
            for d in divided_data:
                rows = [str(c) for c in d]
                display = " ".join(rows)
                print(f"\t{display}")

            print(f"\nn = {len(data_set)}")

        except:
            continue

        else:
            mean = round(stat.mean(data_set), r)
            median = stat.median(data_set)
            mode = stat.mode(data_set)
            # mode = sp.mode(data_set)
            _range = max(data_set) - min(data_set)
            S_var = round(stat.variance(data_set), r)
            S_stdev = round(stat.stdev(data_set), r)
            P_var = round(stat.pvariance(data_set), r)
            P_stdev = round(stat.pstdev(data_set), r)
            P_CV = round(((P_stdev / mean) * 100), r)
            S_CV = round(((S_stdev / mean) * 100), r)

            display_stats()
            break