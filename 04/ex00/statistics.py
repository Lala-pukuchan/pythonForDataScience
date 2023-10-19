def ft_statistics(*args: any, **kwargs: any) -> None:
    """This function takes a list of numbers and return the mean, median,
    and quartile of the list."""
    error = False
    if (len(args) == 0):
        error = True

    numbers = sorted(args)

    def mean(nums):
        return sum(nums) / len(nums)

    def median(nums):
        n = len(nums)
        if n % 2 == 0:
            return (nums[n//2 - 1] + nums[n//2]) / 2
        else:
            return nums[n//2]

    def quartile(nums):
        n = len(nums)
        Q1 = nums[n//4]
        Q3 = nums[n//4 * 3]
        return f"quartile : [{Q1:.1f}, {Q3:.1f}]"

    def standard_deviation(nums):
        return variance(nums) ** 0.5

    def variance(nums):
        return sum((x - mean(nums))**2 for x in nums) / len(nums)

    for kward in kwargs:
        if error is True:
            print("Error")
        elif kwargs[kward] == "mean":
            print("Mean:", mean(numbers))
        elif kwargs[kward] == "median":
            print("Median:", median(numbers))
        elif kwargs[kward] == "quartile":
            print("Quartile:", quartile(numbers))
        elif kwargs[kward] == "std":
            print("Standard deviation:", standard_deviation(numbers))
        elif kwargs[kward] == "var":
            print("Variance:", variance(numbers))
        else:
            pass


def main():
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
