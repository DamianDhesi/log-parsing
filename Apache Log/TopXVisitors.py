import argparse

def TopXPercentVisitors(log_file : str, x : int):
    visit_dict : dict[str, int] = {}
    visitors_count : int = 0

    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()
            ip : str = entry_vals[0]
            
            # increment visit count for ip
            val : int = visit_dict.get(ip, 0)
            visit_dict[ip] = val + 1
            if (val == 0):
                visitors_count += 1

    visit_list : list[tuple] = list(visit_dict.items())
    visit_list.sort(key=lambda tup:tup[1], reverse=True)    # sort is typically O(nlog(n))

    # get number for visitors based off given percent
    num_of_visitors : int = int(x/100 * visitors_count)
    for i in range(0, num_of_visitors):
        print("ip {0} visited {1} times".format(visit_list[i][0], visit_list[i][1]))



def TopXVisitors(log_file : str, x : int):
    visit_dict : dict[str, int] = {}
    visitors_count : int = 0

    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()
            ip : str = entry_vals[0]

            # increment visit count for ip
            val : int = visit_dict.get(ip, 0)
            visit_dict[ip] = val + 1
            if (val == 0):
                visitors_count += 1

    visit_list : list[tuple] = list(visit_dict.items())
    visit_list.sort(key=lambda tup:tup[1], reverse=True)

    # get number for visitors based off given percent
    num_of_visitors : int = min(x, visitors_count)
    for i in range(0, num_of_visitors):
        print("ip {0} visited {1} times".format(visit_list[i][0], visit_list[i][1]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find top visitors in log file")
    parser.add_argument("TopX", type=int, help="Get top X number of visitors")
    parser.add_argument("TopXPercent", type=int, help="Get top X%% of visitors")
    args = parser.parse_args()

    TopXVisitors("./apache_log.txt", args.TopX)
    print("-" * 30)
    TopXPercentVisitors("./apache_log.txt", args.TopXPercent)

