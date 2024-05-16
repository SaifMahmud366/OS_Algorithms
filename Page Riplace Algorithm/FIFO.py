# Number of frames
n = int(input("Enter the number of frames: "))

# Input page reference string
page_string = input("Enter the page reference string (separated by spaces): ")
pages = list(map(int, page_string.split()))

# Initialize frame array
frames = []

# Initialize page fault counter
page_faults = 0

# Iterate over each page in the reference string
for page in pages:
    # If page not in frames, it's a page fault
    if page not in frames:
        # If frames are not full, add the page to frames
        if len(frames) < n:
            frames.append(page)
        # If frames are full, replace the oldest page (FIFO)
        else:
            frames.pop(0)
            frames.append(page)
        page_faults += 1

# Calculate page hits
page_hits = len(pages) - page_faults

# Display the total number of page faults and page hits
print("Total Page Faults:", page_faults)
print("Total Page Hits:", page_hits)
