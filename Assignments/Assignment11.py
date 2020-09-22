#Matthew Umana msu245

import turtle

def reverse_string(s):
    s_new = ""
    if len(s) <= 1:
        return s
    else:
        s_new = reverse_string(s[1:]) + s[0]
        return s_new

def binary_search(key, lst):
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = (low+high)//2
        if lst[mid] == key:
            return True
        elif key > lst[mid]:
            low = mid+1
        elif key < lst[mid]:
            high = mid-1
            
    return False

def h_tree(order, center, size):
    if order < 0:
        return

    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.left(90)

    h_tree(order - 1, None, size/2)
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)

    h_tree(order - 1, None, size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size/2)
    turtle.right(90)

    h_tree(order - 1, None, size/2)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

    h_tree(order - 1, None, size/2)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.left(90)
    turtle.forward(size/2)
    

def main():
    print(reverse_string("desserts"))
    print(reverse_string("flow"))
    print(reverse_string("abcdefg"))
    
    print(binary_search(3, [1,3,5,7,9]))
    print(binary_search(3, [2,4,6,8,10]))
    print(binary_search(0, [1,2, 3, 4, 5]))

    turtle.speed(0)
    turtle.hideturtle()
    h_tree(2, [0, 0], 300)
    turtle.done()

    
if __name__ == '__main__':
    main()
