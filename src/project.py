from input_project import input_project
from process_project import process_project
from output_project import output_project

matritsa, k = input_project()

output_project(matritsa, "Исходная матрица:")

matritsa = process_project(matritsa, k)

output_project(matritsa, "Матрица после удаления:")

input("")