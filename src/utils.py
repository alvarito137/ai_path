def analyze_numbers(numbers):
    if not numbers:
        return None
    
    return {
        "total": total,
        "average": total / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
    }