def validate(n):
    # function to ensure that the number used to call the fibonacci functions is valid
    if not(isinstance(n, int) and n >= 0):
        raise ValueError(f'Expected positive integer, instead got "{n}"')