from utils import analyze_numbers

def main():
    data = [3, 7, 2, 9, 4]
    result = analyze_numbers(data)

    if result is None:
        print("No data provided")
        return
    
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()        