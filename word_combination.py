"""
Given a string. Find all possible combinations in that string.
Total number of combination = factorial(len(input_string))

Examples:
---------
    * "ABC"===> ['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']

Assumptions:
------------
    
    * No repetition inside combination. For example: 
        - AAA,AAB,ABA,ABB etc not allowed

    * No filtering of repetitive words. For example:
        - ABC!=BAC!=CAB!=BCA!=ACB!=CBA. They are all unique.

Solution:
--------

This can be solved by iterative and recursive method. Since I 
started solving it in an iterative process, I din't use recusrsion.
Complexity is a bit high.

Logic:
------

    * Sample input: input_string= "ABC"
    * Initialize an empty global list "l"
    * If length of input_string is less than 1, return input_string
    * s_list= Break the input string into individual letters in a list.
    * Remove and store last element of input_string inside the global list l. 
    * New length of s_list is len(s_list)-1
    * Main Loop starts : Checking whether length of s_list is 0 or not.
    * Remove and store second last element of input_string inside m. 
    * New length of s_list is len(s_list)-2
    * Initialize a local list sub_output for updating l.
    * Iterate through l
    * Iterate through the individual items of l.
    * Update sub_output for different combination of start,mid,end positions.
    * Update l.

Loop Execution Flow:
--------------------

    Input= ABC

    * Main loop::s_list= [AB]
    * Main loop::len(s_list)= 2
    * Global list::l= [C]
    * Main loop after 2nd pop::s_list= [A]
    * Main loop after 2nd pop::len(s_list)= 1
    * Main loop after 2nd pop::m= B

        > First for loop::individual items in l(each)= C
            - Nested for loop::j= 0
            - Nested for loop::each[:j]= 
            - Nested for loop::m= B
            - Nested for loop::each[j:]= C
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= BC
            - Nested for end

            - Nested for loop::j= 1
            - Nested for loop::each[:j]= C
            - Nested for loop::m= B
            - Nested for loop::each[j:]= 
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= CB
            - Nested for end
        > First for loop end
    * Main loop end

    * Main loop::s_list= [A]
    * Main loop::len(s_list)= 1
    * Global list::l= [BC,CB]
    * Main loop after 2nd pop::s_list= [] 
    * Main loop after 2nd pop::len(s_list)= 0
    * Main loop after 2nd pop::m= A

        > First for loop::individual items in l(each)= BC
            - Nested for loop::j= 0
            - Nested for loop::each[:j]= 
            - Nested for loop::m= A
            - Nested for loop::each[j:]= BC
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= ABC
            - Nested for end

            - Nested for loop::j= 1
            - Nested for loop::each[:j]= B
            - Nested for loop::m= A
            - Nested for loop::each[j:]= C
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= BAC
            - Nested for end

            - Nested for loop::j= 2
            - Nested for loop::each[:j]= BC
            - Nested for loop::m= A
            - Nested for loop::each[j:]= 
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= BCA
            - Nested for end
        > First for loop end

        > First for loop::individual items in l(each)= CB
            - Nested for loop::j= 0
            - Nested for loop::each[:j]= 
            - Nested for loop::m= A
            - Nested for loop::each[j:]= CB
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= ACB
            - Nested for end

            - Nested for loop::j= 1
            - Nested for loop::each[:j]= C
            - Nested for loop::m= A
            - Nested for loop::each[j:]= B
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= CAB
            - Nested for end

            - Nested for loop::j= 2
            - Nested for loop::each[:j]= CB
            - Nested for loop::m= A
            - Nested for loop::each[j:]= 
            - Nested for loop::Update sub_output::each[:j] + m + each[j:]= CBA
            - Nested for end
        > First for loop end        
    * Main loop end
    
To run the code:
----------------

    * Modify input_string in main and run this file in terminal: python word_combination.py 
    * Import this module in a separate file and call combination.
"""


def combination(s,l=None):

    if l==None:
        l=[]
    if len(s)<1:
        yield s

    s_list = list(s)    
    l = [s_list.pop()]    

    while len(s_list) != 0:
        m = s_list.pop()
        sub_output = []
        for each in l:
            for j in range(len(each)+1):
                sub_output.append(each[:j] + m + each[j:])
        l = sub_output

    yield l

if __name__=="__main__":

    input_string="ABCD"

    output=combination(input_string)
    for word in output:
        print (word)
