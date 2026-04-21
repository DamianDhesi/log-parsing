
def VisitsPerHour(log_file : str):
    visits_dict : dict[str, int] = {}

    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()
            time : str = entry_vals[3]
            
            # get time in format of day/month/year:hour
            time_vals : list[str] = time.split(":")
            hour_time : str = time_vals[0][1:] + ":" + time_vals[1]

            # increment visit count for that hour
            visits_dict[hour_time] = visits_dict.get(hour_time, 0) + 1

    for tup in visits_dict.items():
        print("{0} visits at {1}".format(tup[1], tup[0]))

def UniqueVisitsPerHour(log_file : str):
    visits_dict : dict[str, int] = {}
    visitors_dict : dict[str, list[str]] = {}

    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()
            time : str = entry_vals[3]
            
            # get time in format of day/month/year:hour
            time_vals : list[str] = time.split(":")
            hour_time : str = time_vals[0][1:] + ":" + time_vals[1]

            # increment unique visit count for that hour, accordingly
            if (hour_time not in visits_dict.keys()):
                visits_dict[hour_time] = 1
                # track visitor ip
                visitors_dict[hour_time] = [entry_vals[0]]
            else:
                # only increment visit count for unique ips in that hour
                if (entry_vals[0] not in visitors_dict[hour_time]):
                    visits_dict[hour_time] += 1
                    visitors_dict[hour_time].append(entry_vals[0])

    for tup in visits_dict.items():
        print("{0} unique visits at {1}".format(tup[1], tup[0]))


if __name__ == "__main__":
    VisitsPerHour("./apache_log.txt")
    print("-" * 30)
    UniqueVisitsPerHour("./apache_log.txt")