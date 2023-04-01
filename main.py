# python3
# Kristaps Skudra 161REB074
def parallel_processing(n, m, data: list):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    other = []
    for s in range(n):
        other.append(0)

    timing = 0
    j = data

    while(j):
        for a,s in enumerate(other):
            other[a]-=1
            if(other[a] <= 0):
                other[a] = j.pop(0)
                output.append((a, timing))
        timing+=1
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split)

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = [list(map(int,input().split()))]

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for job un result:
        print(f"{job[0]} {job[1]}")


if __name__ == "__main__":
    main()
