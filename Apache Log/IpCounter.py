
def IpCounter(log_file : str):
    dic : dict[str, int] = {}

    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()

            # increment ip count 
            dic[entry_vals[0]] = dic.get(entry_vals[0], 0) + 1
        
    # arrange ips in descending order of how often they appear
    ip_list : list[tuple] = list(dic.items())
    ip_list.sort(key = lambda tup: tup[1])

    for ip in ip_list:
        print("{0}: {1}".format(ip[0], ip[1]))

if __name__ == "__main__":
    IpCounter("./apache_log.txt")