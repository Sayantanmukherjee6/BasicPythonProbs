"""
 Given a set of tuples (x1, x2) that represent segments on the number line, 
 write a method to reduce the number of tuples, while representing the same line.

Examples:
---------
    * (1,4)(5,10)(8,12)===> (1,4) (5,12)
    * (1,20)(2,4)===> (1,20)
    * (1,10)(15,20)===> (1,10) (15,20)

Assumptions:
------------
    
    * Within each tuple first number is always less than the second. For example: 
        - (1,4)===> 1 < 4
        - (8,12)===> 8 < 12

    * (1,4)(4,1)===> Won't work

    * Tuples should be inside a list. 
    
Logic:
------

    * Sample input: [(1,4),(5,10),(8,12),(13,16),(2,7)]
    * Global val: min= 0,
                  max= 0,
                  output_list= []
    * Iterations :
        
        - 1st iteration:
                input= (1,4)
                output_list= []
                min= 0
                max= 0
                Process:
                    min= input(0)
                    max= input(1)
                    Update output_list if max and min is 0.
                output_list= [(1,4)]

        - 2nd iteration:
                input= (5,10)
                output_list= [(1,4)]
                min= 1
                max= 4
                Process:
                    if 1 < 5 and 4 < 10:
                        Update max: max= input(1)
                        if (4-5)== -1:
                            Update output_list  
                output= [(1,4),(5,10)]

        - 3rd iteration:
                input= (8,12)
                output_list= [(1,4),(5,10)]
                min= 1
                max= 10
                Process:
                    if 1 < 8 and 10 < 12:
                        Update max: max= input(1)
                        if (4-5)!= -1 and 8 isin range(min,max) and 8 isin range(5,10) and 5 < 8 and 10 < 12:
                            Update output_list==> output_list.append((5,max(input))) 
                            delete (5,10) from output list
                output= [(1,4),(5,12)]

        - 4th iteration:
                input= (13,16)
                output_list= [(1,4),(5,12)]
                min= 1
                max= 12
                Process:
                    if 1 < 13 and 12 < 16:
                        Update max: max= input(1)
                        if (12-13)== -1:
                            Update output_list
                output= [(1,4),(5,12),(13,16)]

        - 5th iteration:
                input= (2,7)
                output_list= [(1,4),(5,12),(13,16)]
                min= 1
                max= 16
                Process:
                    Since 2 and 7 does fall in range of min,max, so reject this input
                output= [(1,4),(5,12),(13,16)]

    * Final output: [(1,4),(5,12),(13,16)]

To run the code:
----------------

    * Modify input_list in main and run this file in terminal: python assignment.py 
    * Import this module in a separate file and call reduce_list
"""


max_no=0
min_no=0

def reduce_list(a,s=list()):

    global max_no,min_no
    if min_no == 0 and max_no == 0:
        min_no= a[0]
        max_no= a[1]
        s.append(a)
    elif min_no < a[0] and max_no < a[1]:
        max_no= a[1]
        if s[len(s)-1][1]-a[0] == -1:
            s.append(a)
        else:
            if set(range(min_no,max_no)).intersection(a) and s[len(s)-1][0] < a[0] and s[len(s)-1][1] < a[1]:
                if set(range(s[len(s)-1][0],s[len(s)-1][1])).intersection(a):
                    s.append((s[len(s)-1][0],max_no))
                    del s[len(s)-2]
                else:
                    s.append(a)
            elif set(range(min_no,max_no)).intersection(a) and s[len(s)-1][0] > a[0] and s[len(s)-1][1] < a[1]:
                s.append((s[len(s)-1][0],max_no))
                del s[len(s)-2]
    elif min_no > a[0] and max_no > a[1] and s[len(s)-1][1]-a[0] != -1:
        min_no= a[0]
        s.append((min_no,s[len(s)-1][1]))
        del s[len(s)-2]
    else:
        pass
    return s

if __name__=="__main__":

    input_list= [(1,4),(5,10),(8,12),(13,16),(2,7)]
    output= map(reduce_list,input_list)[1]
    print (output)