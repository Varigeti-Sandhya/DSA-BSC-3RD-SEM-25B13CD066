# Quick	Sort
def	quick_sort(arr):				
    if	len(arr)	<=	1:								
        return	arr				
    pivot	=	arr[len(arr)	//	2]				
    left	=	[x	for	x	in	arr	if	x	<	pivot]		
    middle	=	[x	for	x	in	arr	if	x	==	pivot]			
    right	=	[x	for	x	in	arr	if	x	>	pivot]				
    return	quick_sort(left)	+	quick_sort(middle)	+	quick_sort(right) 
data	=	[38,	27,	43,	3,	9,	82,	10] 
print("Before	sorting:",	data) 
result	=	quick_sort(data) 
print("After	sorting:	",	result)

