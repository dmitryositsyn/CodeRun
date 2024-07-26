#  325. Коля и датацентры

import heapq
import collections


def memorize_items(
    datacenters,
    seen_max_heap,
    seen_min_heap,
    datacenter_idx,
    num_servers,
    min_heap,
    max_heap,
):
    seen_max_heap_item = (
        -datacenters[datacenter_idx][1]
        * (num_servers - len(datacenters[datacenter_idx][0])),
        datacenter_idx,
    )
    if max_heap[0] == seen_max_heap_item:
        heapq.heappop(max_heap)
    else:
        seen_max_heap[seen_max_heap_item] += 1

    seen_min_heap_item = (
        datacenters[datacenter_idx][1]
        * (num_servers - len(datacenters[datacenter_idx][0])),
        datacenter_idx,
    )
    if min_heap[0] == seen_min_heap_item:
        heapq.heappop(min_heap)
    else:
        seen_min_heap[seen_min_heap_item] += 1


def add(datacenters, max_heap, min_heap, datacenter_idx, num_servers):
    heapq.heappush(
        max_heap,
        (
            (
                -datacenters[datacenter_idx][1]
                * (num_servers - len(datacenters[datacenter_idx][0])),
                datacenter_idx,
            )
        ),
    )
    heapq.heappush(
        min_heap,
        (
            (
                datacenters[datacenter_idx][1]
                * (num_servers - len(datacenters[datacenter_idx][0])),
                datacenter_idx,
            )
        ),
    )


num_datacenters, num_servers, num_queries = map(int, input().split())

min_heap = []
max_heap = []
datacenters = [[set(), 0] for _ in range(num_datacenters)]
for idx in range(num_datacenters):
    heapq.heappush(min_heap, (0, idx))
    heapq.heappush(max_heap, (0, idx))

seen_min = collections.Counter()
seen_max = collections.Counter()

for i in range(num_queries):
    command = list(input().split())
    if command[0] == "RESET":
        datacenter_idx = int(command[1]) - 1

        memorize_items(
            datacenters,
            seen_max,
            seen_min,
            datacenter_idx,
            num_servers,
            min_heap,
            max_heap,
        )

        datacenters[datacenter_idx][1] += 1
        datacenters[datacenter_idx][0] = set()

        add(datacenters, max_heap, min_heap, datacenter_idx, num_servers)

    elif command[0] == "DISABLE":
        datacenter_idx = int(command[1]) - 1
        server_idx = int(command[2]) - 1

        memorize_items(
            datacenters,
            seen_max,
            seen_min,
            datacenter_idx,
            num_servers,
            min_heap,
            max_heap,
        )

        datacenters[datacenter_idx][0].add(server_idx)

        add(datacenters, max_heap, min_heap, datacenter_idx, num_servers)

    elif command[0] == "GETMAX":
        while seen_max[max_heap[0]] > 0:
            seen_max[max_heap[0]] -= 1
            if seen_max[max_heap[0]] == 0:
                del seen_max[max_heap[0]]
            heapq.heappop(max_heap)
        print(max_heap[0][1] + 1)

    elif command[0] == "GETMIN":
        while seen_min[min_heap[0]] > 0:
            seen_min[min_heap[0]] -= 1
            if seen_min[min_heap[0]] == 0:
                del seen_min[min_heap[0]]
            heapq.heappop(min_heap)
        print(min_heap[0][1] + 1)