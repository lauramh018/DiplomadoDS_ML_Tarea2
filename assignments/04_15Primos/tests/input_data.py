# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["2"],
        # Outputs
        ["Escribe un numero entero : ", "True"],
        # Message in case of failure
        "Revisa que estes haciendo bien tu calculo del resultado"
    ),
    # Test case 2
    (
        # Inputs
        ["244356"],
        # Outputs
        ["Escribe un numero entero : ", "False"],
        # Message in case of failure
        "Revisa que estes haciendo bien tu calculo del resultado"
    ),
    # Test case 3
    (
        # Inputs
        ["113"],
        # Outputs
        ["Escribe un numero entero : ", "True"],
        # Message in case of failure
        "Revisa que estes haciendo bien tu calculo del resultado"
    ),
    # Test case 4
    (
        # Inputs
        ["-5"],
        # Outputs
        ["Escribe un numero entero : ", "False"],
        # Message in case of failure
        "Revisa que estes calculando bien todos los casos"
    ),
]
