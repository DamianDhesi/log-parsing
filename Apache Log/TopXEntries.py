import argparse
import heapq

def TopXEntriesFast(log_file : str, x : int):
    heap : list[tuple] = []
    entry_count : int = 0

    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()
            latency_str : str = entry_vals[9]

            if (latency_str == "-"):
                latency_str = "0"

            # make latency negative to get max heap functionality before 3.14
            item : tuple[int, str] = (-int(latency_str), line)
            heapq.heappush(heap, item)

            entry_count += 1

    num_of_entries : int = int(x/100 * entry_count)
    for _ in range(0, num_of_entries):
        print(heapq.heappop(heap)[1])

def TopXEntriesMemEfficent(log_file : str, x : int):
    heap : list[tuple] = []
    entry_count : int = 0

    with open(log_file, "r") as file:
        for line in file:
            entry_count += 1

    num_of_entries : int = int(x/100 * entry_count)
    with open(log_file, "r") as file:
        for line in file:
            entry : str = line.strip()
            entry_vals : list[str] = entry.split()
            latency_str : str = entry_vals[9]

            if (latency_str == "-"):
                latency_str = "0"

            # make latency negative to get max heap functionality before 3.14
            item : tuple[int, str] = (int(latency_str), line)

            if (len(heap) < num_of_entries):
                heapq.heappush(heap, item)
            else:
                if (item[0] > heap[0][0]):
                    heapq.heapreplace(heap, item)

    for item in heapq.nlargest(num_of_entries, heap):
        print(item[1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find top X%% of entries with highest latency")
    parser.add_argument("X", type=int, help="Percent of entries to return")
    args = parser.parse_args()

    print("O(X) average time complexity:")
    TopXEntriesFast("./apache_log.txt", args.X)
    print("-" * 30)
    print("O(Nlog(N)) complexity:")
    TopXEntriesMemEfficent("./apache_log.txt", args.X)