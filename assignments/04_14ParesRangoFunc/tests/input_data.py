# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["3", "8"],
        # Outputs
        ["Valor 1: ", "Valor 2: ","4", "6", "8"],
        # Message in case of failure
        "Revisa los limites pares"
    ),
    # Test case 2
    (
        # Inputs
        ["3", "3"],
        # Outputs
        ["Valor 1: ", "Valor 2: ","No hay pares"],
        # Message in case of failure
        "Revisa que pasa cuando no hay pares"
    ),
    # Test case 3
    (
        # Inputs
        ["9", "2"],
        # Outputs
        ["Valor 1: ", "Valor 2: ", "2", "4", "6", "8"],
        # Message in case of failure
        "Revisa el orden de los inputs"
    ),
    # Test case 4
    (
        # Inputs
        ["9", "1"],
        # Outputs
        ["Valor 1: ", "Valor 2: ", "2", "4", "6", "8"],
        # Message in case of failure
        "Revisa el orden de los inputs"
    ),
]
