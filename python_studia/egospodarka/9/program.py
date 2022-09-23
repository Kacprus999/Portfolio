from benfordslaw import benfordslaw
import numpy as np

def digit_percent (digit_count):
    digit_perc = [0,0,0,0,0,0,0,0,0]
    digit_sum = sum(digit_count)
    for i, digit in enumerate(digit_count):
        digit_perc[i] = digit/digit_sum*100
    return digit_perc

def compare_benford (digit_percent):
    benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    deviation = 0
    for i, digit in enumerate(digit_percent):
        deviation += abs(benford[i] - digit)
    deviation = deviation / 8
    return deviation

bl = benfordslaw()
for i in range(1, 30):

    num = str(i)
    array = np.zeros(101) 
    if (i < 10):
        num = "0"+num
    f = open("0" + num + ".txt", "r")
    
    lines = f.readlines()
    digit_count = [0,0,0,0,0,0,0,0,0]
    j = 0
    for line in lines:
        array[j] = int(line)

        digit = int(str(line)[:1])
        if (digit == 0):
            # digit = 1
            2+2
        else:
            digit_count[digit-1] = digit_count[digit-1] + 1
        j+=1
    print("wynik pliku: " + "0" + num + ".txt")
    results = bl.fit(array)

    # print(array)
    # print(digit_percent(digit_count))
    # print(compare_benford(digit_percent(digit_count)))


# # Initialize


# # Load elections example
# df = bl.import_example(data='USA')

# # Extract election information.
# X = df['votes'].loc[df['candidate']=='Donald Trump'].values

# # Print
# print(X)
# # array([ 5387, 23618,  1710, ...,    16,    21,     0], dtype=int64)
# print(array)
# # Make fit

# # Plot
# bl.plot()