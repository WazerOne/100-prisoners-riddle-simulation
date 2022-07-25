import numpy as np

# 100 prisoners riddle


# shuffling numbers in boxes
def generate():
    boxes = np.arange(0, 100, 1)
    np.random.shuffle(boxes)
    return boxes


# prisoner checks boxes in particular strategy
# this strategy implies that prisoner is checking first box with his number and if he doesn't find his number
# in this box then he checks the box with found number in previous box
# prisoner is allowed to check 50 boxes, otherwise all the prisoners are sentenced to death :(
def prisoner_checks(pr_num, boxes):
    n = 0
    next = pr_num
    while n < 50:
        if pr_num == boxes[next]:
            return True
        else:
            next = boxes[next]
        n += 1
    return False


# checking outcome for all prisoners
def check_whole(arr):
    for i in arr:
        if not i:
            return False
    return True


# each prisoner have his own number that doesn't change throughout the experiment
prisoner_num = np.arange(0, 100, 1)
arr = np.empty(100)  # array with searching results of each prisoner
k = 0                # counter of positive outcomes in simulation
for i in range(10000):
    cells = generate()
    # filling array with searching results
    for j in range(100):
        arr[j] = prisoner_checks(prisoner_num[j], cells)
    # checking outcome for all prisoners and counting positive outcomes
    if check_whole(arr):
        k += 1
# calculating percentage of positive outcomes (i+1 because iterator stops at n-1 of total iterations)
print(k/(i+1))
