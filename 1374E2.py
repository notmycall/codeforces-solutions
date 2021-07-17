from operator import itemgetter
import uuid


'''
# Returns True is alice and bob has enough preferred books, else returns none and their values
def aliceAndBobLikes(books, k):
    a, b = 0, 0
    for book in range(books):
        if book[2] == 1:
            a += 1
        if book[3] == 1:
            b += 1
    if a >= k and b >= k:
        return list(True)
    else:
        return list(False, a, b)
'''

def uuid_in_book(uuid, books):
    for b in range(len(books)):
        if uuid == books[b][4]:
            return True
    return False




# Accept the input of the problem
n, m, k = [int(x) for x in input().split()] # n = books, m = books required k = preferred books required for both Alice and Bob
books = []
for i in range(n):
    books.append([int(x) for x in input().split()])
    books[i].append(i) # Appends the original index location
    books[i].append(str(uuid.uuid4())) # Appends a unique identifier used later to prevent duplicate books.


# Dividing the first index (length) in two if index 1 and 2 are both 1 (True)
for b in range(len(books)):
    if books[b][1] == 1 and  books[b][2] == 1:
        books[b][0] = books[b][0] / 2


# Sort the lists within the list from shortest to read to largest
books = sorted(books, key=itemgetter(0))

# Get the first k number of books that satisfies Alice. 
aliceChosenBooks = []
a_k = 0
for o in range(n):
    if a_k == k:
        break
    if books[o][1] == 1:
        aliceChosenBooks.append(books[o])
        a_k += 1

# Get the first k number of books that satisfies Bob. 
bobChosenBooks = []
b_k = 0
for o in range(n):
    if b_k == k:
        break
    if books[o][2] == 1:
        bobChosenBooks.append(books[o])
        b_k += 1

# If length of aliceChosenBooks or length of bobChosenBooks is less than k, then return -1 and quit.
if len(aliceChosenBooks) < k or len(bobChosenBooks) < k:
    print(-1)
    quit()

# Merge the chosen books together, not including any of the duplicates. 

chosenBooks = []
chosenBooks = aliceChosenBooks[:]

for i in range(len(bobChosenBooks)):
    if bobChosenBooks[i][1] == 1 and aliceChosenBooks[i][2] == 1:
        if uuid_in_book(bobChosenBooks[i][4], chosenBooks):
            continue
        else:
            chosenBooks.append(bobChosenBooks[i])

# If list is greater than n, return -1 and quit. 
if len(chosenBooks) > n:
    print(-1)
    quit()

# If the list is less than n, get highest value index then append i+1 from books
if len(chosenBooks) < n:
    v = len(chosenBooks) - n
    pass

    
        
    if books[b][4] not in chosenBooks:
        chosenBooks.append(books[b])
        v -= 1

    


# Return values with 1 in index 1 and 2 back to its original value by multipying it by 2 and converting it into an int 

# Finally, return the total of the sum of the k's, and the index positions of the books in the list.


# https://codeforces.com/problemset/problem/1374/E2






'''
alice = 1 2 3 4 5 6 7 8 9

bob = 1 2 3 4 5 6 7 8 9

1. Accept the input. Add the original index of each list at the end as a forth value. 
2. Iterate through the books
3. If i value (reading time) in books supports both a and b's preferences, then half the value.
4. Sort the values from lowest reading time to longest reading time
5. Create two lists. One with the best and K books for Alice, and with the best and K books for Bob
6. Take the two lists, 





'''





