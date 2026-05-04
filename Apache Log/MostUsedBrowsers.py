
browser_count : dict[str, int] = {}

with open("./apache_log.txt", "r") as file:
    for line in file:
        entry : str = line.strip()
        entry_vals : list[str] = line.split()
        browser : str = entry_vals[-1].split("/")[0]
        # browser postion is not consistent so ouput will be paritally messed up
        
        if (not browser[0].isalpha()):
            #not well formed
            continue

        browser_count[browser] = browser_count.get(browser, 0) + 1

    browser_list = list(browser_count.items())
    browser_list.sort(key= lambda tup: tup[1], reverse=True)

    for item in browser_list:
        print("{0}: {1}".format(item[0], item[1]))