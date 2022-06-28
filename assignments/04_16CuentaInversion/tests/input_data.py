# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["1000", "12"],
        # Outputs
        ["Escribe la cantidad de dinero inicial : ", "Escribe el porcentaje de interes anual : ", "1126.83"],
        # Message in case of failure
        "Revisa que estes haciendo bien tu calculo del resultado"
    ),
    # Test case 2
    (
        # Inputs
        ["1000", "-12"],
        # Outputs
        ["Escribe la cantidad de dinero inicial : ", "Escribe el porcentaje de interes anual : ", "Error en los datos"],
        # Message in case of failure
        "Revisa que estes tomando en cuenta todos los casos"
    ),
    # Test case 3
    (
        # Inputs
        ["0", "21"],
        # Outputs
        ["Escribe la cantidad de dinero inicial : ", "Escribe el porcentaje de interes anual : ", "Error en los datos"],
        # Message in case of failure
        "Revisa que estes tomando en cuenta todos los casos"
    ),

]
