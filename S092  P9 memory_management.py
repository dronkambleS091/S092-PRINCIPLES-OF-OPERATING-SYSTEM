# Memory Management Techniques
# FIFO and LRU Page Replacement

def fifo_page_replacement(pages, frames):
    memory = []
    hits = 0
    faults = 0

    print("\n--- FIFO Page Replacement ---")
    print("Page\tFrames\t\tResult")

    for page in pages:
        if page in memory:
            hits += 1
            result = "Hit"
        else:
            faults += 1
            result = "Miss"

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print(f"{page}\t{memory}\t\t{result}")

    return hits, faults


def lru_page_replacement(pages, frames):
    memory = []
    hits = 0
    faults = 0

    print("\n--- LRU Page Replacement ---")
    print("Page\tFrames\t\tResult")

    for page in pages:
        if page in memory:
            hits += 1
            result = "Hit"

            # Move recently used page to the end
            memory.remove(page)
            memory.append(page)

        else:
            faults += 1
            result = "Miss"

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print(f"{page}\t{memory}\t\t{result}")

    return hits, faults


# Main Program
print("===== Memory Management Techniques =====")

# Page reference string
pages = list(map(int, input(
    "Enter page reference string (space separated): "
).split()))

# Number of frames
frames = int(input("Enter number of frames: "))

# FIFO
fifo_hits, fifo_faults = fifo_page_replacement(pages, frames)

# LRU
lru_hits, lru_faults = lru_page_replacement(pages, frames)

# Calculate ratios
total_pages = len(pages)

fifo_hit_ratio = fifo_hits / total_pages
fifo_miss_ratio = fifo_faults / total_pages

lru_hit_ratio = lru_hits / total_pages
lru_miss_ratio = lru_faults / total_pages

# Display results
print("\n===== Final Results =====")

print("\nFIFO:")
print("Page Hits   :", fifo_hits)
print("Page Faults :", fifo_faults)
print("Hit Ratio   :", round(fifo_hit_ratio, 2))
print("Miss Ratio  :", round(fifo_miss_ratio, 2))

print("\nLRU:")
print("Page Hits   :", lru_hits)
print("Page Faults :", lru_faults)
print("Hit Ratio   :", round(lru_hit_ratio, 2))
print("Miss Ratio  :", round(lru_miss_ratio, 2))
