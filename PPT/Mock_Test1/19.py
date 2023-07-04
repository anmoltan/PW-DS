def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data = [43,76,56,885,934,364,85,49]
mean_value = calculate_mean(data)
print("Mean:", mean_value)
