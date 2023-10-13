def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    '''
    BMI = weight(kg) / height(m)^2
    zip is to combine two lists into one list of tuples
    '''
    bmi_list = []
    try:
        if not isinstance(height, list):
            raise AssertionError("The 'height' parameter must be a list.")
        if not isinstance(weight, list):
            raise AssertionError("The 'weight' parameter must be a list.")
        if len(height) != len(weight):
            raise AssertionError(
                "The 'height' and 'weight'"
                + "parameters must be the same length.")
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)):
                raise AssertionError(
                    "The 'height' parameter must be a list of numbers.")
            if not isinstance(w, (int, float)):
                raise AssertionError(
                    "The 'weight' parameter must be a list of numbers.")
            h_meters = h
            bmi = w / (h_meters ** 2)
            bmi_list.append(bmi)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    Returns a list of True/False values based on
    whether each bmi value is greater than the limit.
    '''
    try:
        if bmi is None:
            raise AssertionError("The 'bmi' parameter must not be None.")
        if not isinstance(bmi, list):
            raise AssertionError("The 'bmi' parameter must be a list.")
        if not isinstance(limit, int):
            raise AssertionError("The 'limit' parameter must be an integer.")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None
    return [value > limit for value in bmi]


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
