import time


def display_progress_bar(length, percentage):
    bar_length = int(length * (percentage / 100))
    progress_bar = "|" + "=" * bar_length + "-" * (length - bar_length) + "|"

    label = f"{percentage}%"
    padding = max(0, length - len(label) - 3)
    label = " " * (padding // 2) + label + " " * (padding // 2)

    print(progress_bar, label)


total_length = 50
for percent in range(101):
    display_progress_bar(total_length, percent)
    time.sleep(0.1)
