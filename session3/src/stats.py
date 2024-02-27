def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(list):
    mean = calculate_mean(list)
    return sum([(x - mean) ** 2 for x in list]) / len(list)

def calculate_std(list):
    return calculate_variance(list)**0.5

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:
        median = numbers[mid]
    return median

def compute_stat(data, kind=calculate_mean):
    return kind(data)

def test():
    print("Hello")
