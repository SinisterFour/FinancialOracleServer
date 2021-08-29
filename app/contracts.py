# Input
{
    "train": [
        ["Columna1", "Columna2", "Columna3", "..."],
        [1, 1, 2000, 48.80116016],
        [2, 1, 2000, 49.1371793],
        [1, 2, 2000, 49.41320941],
        # 504 filas representando quincenas del 2000 al 2020
    ],
    "test": [
        ["Columna1", "Columna2", "Columna3", "..."],
        [1, 1, 2000, 48.80116016],
        [2, 1, 2000, 49.1371793],
        [1, 2, 2000, 49.41320941],
        # 15 filas
    ],
    "train_inpc": [0, 1, 2, 3, 2],  # 504 valores
    "test_inpc": [0, 1, 2, 3, 2],  # 15 valores
}

# Output
{
    "forecast": [
        1,
        2,
        3,
        4,
        # 15 valores
    ],
    "mean_squared_error": 123,
}
