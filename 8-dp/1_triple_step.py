# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps
# at a time. Implement a method to count how many possible ways the child can run up the stairs.
# 152, 178, 217, 237, 262, 359
# Approach this from the top down. What is the very last hop the child made?
# If we knew the number of paths to each of the steps before step 100, could we compute the number of steps to 1OO
#   97 to 100 is 4, 98 to 100 is 2, 99 to 100 is 1
# We can compute the number of steps to 100 by the number of steps to 99, 98, and 97. This corresponds to the child hopping 1, 2, or 3 steps at the end. Do we add those or multiply them?That is: Is it f(1000) = f(99) + f(98) + f(97) or f(100) = f(99) * f(98) * f(97)?
# We multiply the values when it's "we do this then this:' We add them when it's "we do this or this

# Ways to run up 0 or 1 step: 1 last hop is 1
# ways to run up 2 steps: 2 (1 + 1 or 2) last hop 1 or 2    f(2) = f(1) + f(0)
# ways to run up 3 steps: 4 (1+1+1 or 1+2 or 2+1 or 3) last hop 1 or 2 or 3 f(3) = f(2) + f(1) + f(0)
# 4 steps: 3 steps + 1 (4), 2 steps + 2 (4)

# this runtime is O(n)
def triple_step(n):
    memo = [1, 1, 2, 4] # 
    for current in range(4, n+1):
        memo.append(memo[current-1] + memo[current-2] + memo[current-3])
    return memo[n]

if __name__ == '__main__':
    for i in range(10):
        print(i, triple_step(i))