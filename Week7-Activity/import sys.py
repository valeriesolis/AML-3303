import sys
print("Python executable:", sys.executable)

try:
    import evidently
    print("Evidently version:", evidently.__version__)
    print("Evidently location:", evidently.__file__)
except ModuleNotFoundError as e:
    print("Evidently is NOT installed in this environment:", e)
