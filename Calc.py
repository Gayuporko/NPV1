import subprocess
# Open the calculator
subprocess.Popen('calc.exe')
# Perform the calculation
calculation_result = 2 + 2
# Save the result to a file
with open('result.txt', 'w') as file:
    file.write(str(calculation_result))