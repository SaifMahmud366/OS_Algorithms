# Number of frames
n = int(input("Enter the number of frames: "))

# Input page reference string
page_string = input("Enter the page reference string (separated by spaces): ")
pages = list(map(int, page_string.split()))

# Initialize frame array
frames = []

# Initialize dictionary to store the most recent index of each page in frames
page_index = {}

# Initialize page fault and page hit counters
page_faults = 0
page_hits = 0

# Iterate over each page in the reference string
for i, page in enumerate(pages):
    # If page not in frames, it's a page fault
    if page not in frames:
        # If frames are not full, add the page to frames
        if len(frames) < n:
            frames.append(page)
            page_index[page] = i
        # If frames are full, find the least recently used page and replace it
        else:
            lru_page = min(frames, key=lambda x: page_index[x])
            frames.remove(lru_page)
            del page_index[lru_page]
            frames.append(page)
            page_index[page] = i
        page_faults += 1
    # If page is already in frames, it's a page hit
    else:
        page_hits += 1
        page_index[page] = i

# Display the total number of page faults and page hits
print("Total Page Faults:", page_faults)
print("Total Page Hits:", page_hits)
