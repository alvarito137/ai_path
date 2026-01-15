def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return {
        "total":total,
        "avergae": average,
        "max": max(numbers),
        "min":min(numbers),
}

data = [3,7,2,9,4]
result = analyze_numbers(data)

for key, value in result.items(): print(f"{key}:{value}")

