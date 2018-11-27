#Problem
#Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position .
print: Print the list.
remove e: Delete the first occurrence of integer e .
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by  lines of n commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.





if __name__ == '__main__':
    N = int(raw_input())
    List = []
    Arr = []
    for i in range(N):
        op = raw_input().split()
        cmd = op[0]
        args = op[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("Arr."+cmd)
        else:
            print Arr
        