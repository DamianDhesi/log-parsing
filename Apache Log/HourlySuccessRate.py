
def HourlySuccessRate(log_file : str):
    hourly_success : dict[str, list[int]] = {}

    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()
            status_code : int = int(entry_vals[8])
            time : str = entry_vals[3]
            
            # get time in format of day/month/year:hour
            time_vals : list[str] = time.split(":")
            hour_time : str = time_vals[0][1:] + ":" + time_vals[1]

            # increment the count according to status code
            hourly_count : list[int] = hourly_success.get(hour_time, [0] * 2)
            if (status_code == 200):
                hourly_count[0] += 1
            
            hourly_count[1] += 1
            hourly_success[hour_time] = hourly_count

    for item in hourly_success.items():
        print("{0:.0f}% success rate at {1}".format(item[1][0]/item[1][1] * 100, item[0]))

if __name__ == "__main__":
    HourlySuccessRate("./apache_log.txt")