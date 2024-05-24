from math import *


def GROUPED():
    print("\nGROUPED DATA")

    j = 0
    k = 10  # only change this to adjust the number of elements per row
    r = 2  # change this to adjust the rounded places
    s = " "  # change this to adjust the input splitter


    def display_stats1():
        print()
        print("n =", n)
        print("R =", _range)
        print("K =", K)
        print("C =", C)
        print("Lower Limit:", lower_limit)
        print("Upper Limit:", upper_limit)

    def display_stats2():
        print("\nCENTRAL TENDENCY")
        print(f"Mean:  XG = {X_g}")
        print("\ttΣFiXi =", FiXi_total)
        print("\tn =", n)
        print(f"\nMedian:  MdG = {Md_g}")
        print(f"\tMedian Class: {first_interval[mc]}-{second_interval[mc]}")
        print("\tLCB_md =", LCB[mc])
        print("\tC =", C)
        print("\t<CF_b =", lower_CF[mc - 1])
        print("\tF_md =", frequency[mc])
        print("\tn =", n)
        print(f"\nMode:  MoG = {Mo_g}")
        print(f"\tModal Class: {first_interval[moc]}-{second_interval[moc]}")
        print("\tLCB_mo =", LCB[moc])
        print("\tC =", C)
        print("\tF_mo =", frequency[moc])
        print("\tF_b =", Fb)
        print("\tF_a =", Fa)

    def display_stats3():
        print("\nDISPERSION")
        print("RG =", R_g)
        print("SG^2 =", S_g_2)
        print("SG =", S_g)
        print("CV =", CV)


    while True:
        try:
            #data_input = "144 112 156 122 168 172 141 159 127 154 156 145 134 137 123 149 144 160 136 139 142 138 159 151 147 150 126 152 147 136 135 132 146 133 150 122 139 149 152 129 131 155 116 140 145 135 160 125 172 163".split()
            data_input = input("\nPlease input data set: ").split()
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

        except:
            continue

        else:
            n = len(data_set)
            _range = R = int(max(data_set) - min(data_set))
            no_class_K = K = ceil(1 + 3.322 * log(n, 10))  ####
            class_size_C = C = round(R / K)  ####
            lower_limit = min(data_set)
            upper_limit = max(data_set)

            display_stats1()


            # Class Intervals
            first_interval = []
            second_interval = []
            i = lower_limit
            i_2 = lower_limit + (C - 1)
            for _ in range(K):
                first_interval.append(i)
                i += C
            for _ in range(K):
                second_interval.append(i_2)
                i_2 += C
            intervals = list(zip(first_interval, second_interval))
            # print(intervals)

            # Frequency
            z = 0
            frequency = []
            while z < K:
                f = 0
                for val in data_set:
                    if intervals[z][0] <= val <= intervals[z][1]:
                        f += 1
                frequency.append(f)
                z += 1
            # print(frequency)
            Mod_frequency = []
            for frq in frequency:
                if 0 <= frq < 10:
                    Mod_frequency.append("0" + str(frq))
                else:
                    Mod_frequency.append(str(frq))

            # Class Mark
            z = 0
            classmark = []
            while z < K:
                C_mark = (intervals[z][0] + intervals[z][1]) / 2
                classmark.append(C_mark)
                z += 1
            # print(classmark)

            # Class Boundary
            LCB = []
            UCB = []
            for lcb in first_interval:
                lcb -= 0.5
                LCB.append(lcb)
            for ucb in second_interval:
                ucb += 0.5
                UCB.append(ucb)
            class_boundary = list(zip(LCB, UCB))
            # print(class_boundary)


            # Relative Frequency
            rel_frequency = []
            for freq in frequency:
                rel_freq = round(((freq / n) * 100), 2)
                rel_frequency.append(rel_freq)
            # print(rel_frequency)

            # <CF
            CF = 0
            lower_CF = []
            for cf in frequency:
                CF += cf
                lower_CF.append(CF)
            # print(lower_CF)

            # <CF
            CF = 0
            upper_CF = []
            for cf in reversed(frequency):
                CF += cf
                upper_CF.append(CF)
            upper_CF.reverse()
            # print(upper_CF)

            # FiXi
            FiXi = [frequency[y] * classmark[y] for y in range(K)]
            FiXi_total = sum(FiXi)
            # print(FiXi, FiXi_total)

            # Xi^2
            Xi_sqr = [Xi ** 2 for Xi in classmark]

            # Fi(Xi)^2
            z = 0
            Fi_Xi_sqr = []
            while z < K:
                apnd = frequency[z] * Xi_sqr[z]
                Fi_Xi_sqr.append(apnd)
                z += 1


            display = list(zip(first_interval, second_interval, Mod_frequency, classmark,
                               LCB, UCB, rel_frequency, lower_CF, upper_CF))
            print(f"\nIntrvls | F  | C_Mrk | C_Boundary  |R_F% |<CF |>CF")
            for D in display:
                print(f"{D[0]}-{D[1]} | {D[2]} | {D[3]} | {D[4]}-{D[5]} | {D[6]} | {D[7]} | {D[8]}")

            print("-------------------------------------------------------")

            display_2 = list(zip(first_interval, second_interval, Mod_frequency,
                               classmark, FiXi, LCB, UCB, lower_CF))
            print(f"\nIntrvls | Fi |  Xi   | FiXi  | C_Boundary  | <CF")
            for D in display_2:
                print(f"{D[0]}-{D[1]} | {D[2]} | {D[3]} | {D[4]} | {D[5]}-{D[6]} | {D[7]}")


            # For finding Median Class
            for lcf in lower_CF:
                if lcf > (n / 2):
                    MC = lower_CF.index(lcf)
                    break
            mc = MC

            # For finding the Modal Class
            moc = frequency.index(max(frequency))


            X_g = round(FiXi_total / n, r)
            MC = f"{intervals[mc][0]}-{intervals[mc][1]}"
            Md_g = round(LCB[mc] + C * (((n/2) - lower_CF[mc - 1]) / frequency[mc]), r)
            MoC = f"{intervals[moc][0]}-{intervals[moc][1]}"
            try:
                Fb = frequency[moc - 1]
            except:
                Fb = 0
            try:
                Fa = frequency[moc + 1]
            except:
                Fa = 0
            Mo_g = round(LCB[moc] + C * ((frequency[moc] - Fb) / ((2 * frequency[moc]) - Fa - Fb)), r)

            display_stats2()

            print("-------------------------------------------------------")

            display_2 = list(zip(first_interval, second_interval, Mod_frequency,
                               classmark, FiXi, Xi_sqr, Fi_Xi_sqr))
            print(f"\nIntrvls | Fi |  Xi   | FiXi  |  Xi^2   | FiXi^2")
            for D in display_2:
                print(f"{D[0]}-{D[1]} | {D[2]} | {D[3]} | {D[4]} | {D[5]} | {D[6]}")

            FiXi_sqr_total = sum(Fi_Xi_sqr)
            R_g = second_interval[-1] - first_interval[0]
            S_g_2 = round((n * FiXi_sqr_total - FiXi_total ** 2) / (n * (n - 1)), r)
            S_g = round(sqrt(S_g_2), r)
            CV = f"{round(((S_g / X_g) * 100), r)}%"

            display_stats3()
            break