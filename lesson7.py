import random
import math

def tesadufu_ededler_ve_kvadrat_cut_ededler():
    tesadufu_ededler = [random.randint(20,50) for _ in range(5)] 
    print(f"araliq bes eded:{tesadufu_ededler}")
    
    kvadrat_cut_ededler=[math.pow(num,2) if num % 2 == 0 else num for num in tesadufu_ededler]
    
    return kvadrat_cut_ededler

netice=tesadufu_ededler_ve_kvadrat_cut_ededler()
print(f"kvadrat cut ededler:{netice}")
