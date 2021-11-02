#oluşturulan iki fonkiyonda da height değişkenine göre blok yazdırılır.

def mario_iterative(height):
    for i in range(height):
        print("#"*(i+1))


def mario_recursive(height):
    if height == 0:
        return

    mario_recursive(height -1)
    print("#" * height)
    

height = int(input("Height of the block: "))

print(" ")

print("Iterative implementation: ")
mario_iterative(height)

print(" ")

print("Recursive implementation: ")
mario_recursive(height)