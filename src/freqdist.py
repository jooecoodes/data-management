import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42156)  
data = np.random.randint(50, 100, size=100)  

# Define class width
class_width = 5
min_value = min(data)
max_value = max(data)
bins = np.arange(min_value, max_value + class_width, class_width) 
print("Bins: ", bins)
print(data)
print("Min value: ", min_value, " Max value: ", max_value)

freq, edges = np.histogram(data, bins=bins)
print("Num of Freq: ", len(freq))
print("Freq: ", freq)
print("Sum of Freq: ", sum(freq))
print("Edges: ", edges)

relative_freq = freq / sum(freq)
cumulative_freq = np.cumsum(freq)
classes = [(edges[i], edges[i + 1] - 1) if i > 0 else (edges[i], edges[i + 1] - 1) for i in range(len(edges) - 1)]
class_marks = [((edges[i] + edges[i + 1]) / 2) - 0.5 for i in range(len(edges) - 1)]
class_boundaries = [(edges[i] - 0.5, edges[i + 1] - 0.5) for i in range(len(edges) - 1)]
# horizontal_axis_val = [class_boundary[0] for class_boundary in class_boundaries]
horizontal_axis_val = []
for idx, class_boundary in enumerate(class_boundaries):
    if idx == len(class_boundaries) - 1:
        print(f"Last index reached: {class_boundary}")
        horizontal_axis_val.append(class_boundary[0])
        horizontal_axis_val.append(class_boundary[1])
    else:
        print(f"Index {idx}: {class_boundary[0]}")
        horizontal_axis_val.append(class_boundary[0])

freq_with_decoy = np.append(freq, 0)

print("H axis val: ", horizontal_axis_val)
print("Num of H axis val: ", len(horizontal_axis_val))
print("Len of Class Mark: ", len(class_marks))
print("Len of Class Boundaries: ", len(class_boundaries))
print("Class Mark", class_marks)
print("Class Boundaries: ", class_boundaries)
print("Classes: ", classes)

df = pd.DataFrame({
    "Classes": classes,
    "Class Boundaries": class_boundaries,
    "Class Mark": class_marks,
    "Frequency": freq,
    "Cumulative Frequency": cumulative_freq,
    "Relative Frequency": relative_freq
})

print(df)

plt.figure(figsize=(10, 6))

plt.bar(horizontal_axis_val, freq_with_decoy, width=class_width, edgecolor="black", alpha=0.7, align='edge')

plt.xticks(horizontal_axis_val)

plt.xlabel("Class Mark")
plt.ylabel("Frequency")
plt.title("Frequency Distribution")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
