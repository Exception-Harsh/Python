import argparse

print("Experiment 1")
parser = argparse.ArgumentParser(
    description='Calculation of two given numbers')
parser.add_argument("n1", type=float, help='Input first number')
parser.add_argument("n2", type=float, help='Input second number')
args = parser.parse_args()
result = float(10) + float(10)
print(result)
