import math

def entropy(string):

    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    entropy = 0
    for c in freq:
        p = freq[c] / len(string)
        entropy -= p * math.log2(p)

    return entropy

def main():
    input_string = input("Enter a string: ")
    print(entropy(input_string))

if __name__ == "__main__":
    main()