import random

def generate_random_data(size=10):
    """Generate a list of random integers."""
    return [random.randint(1, 100) for _ in range(size)]

def calculate_average(data):
    """Calculate the average of a list of numbers."""
    if not data:
        return 0.0
    return sum(data) / len(data)

def main():
    data = generate_random_data()
    average = calculate_average(data)
    print(f"Generated Data: {data}")
    print(f"Average Value: {average:.2f}")

if __name__ == "__main__":
    main()