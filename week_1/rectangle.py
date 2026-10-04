#Goal
#Practice numeric values and arithmetic operators.
#Imagine you are building a small construction tool.
#Ask the user for:
#Length
#Width
#Calculate:
#Area
#Perimeter
#Then display the results.
#Example
#Length: 10
#Width: 5
#
#Area: 50 m²
#Perimeter: 30 m
#
#Concepts
#Numbers • arithmetic operators • input conversion
#

line = "=================================================================="
length = float(input("Length: "))
width = float(input("Width: "))
area  = length * width 
perimeter =  2 * (length + width)
output = f"""
    {line}
    The rectangle infomration: Length = {length}, Width = {width}

    {line}
    Area = {area}
    Perimeter = {perimeter}
    {line}


        """
print(output)

