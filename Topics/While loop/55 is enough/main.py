count = 0
input_ = int(input())
sum_ = 0

while input_ != 55:
    sum_ += input_
    count += 1
    input_ = int(input())

print(count, sum_, round(sum_ / count), sep="\n")
