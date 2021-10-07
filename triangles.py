"""
classifies triangles
"""
def classify_triangle(a_a, b_b, c_c):
    '''Classifies parameters as triangle or not'''

    tri_name = ""
    if a_a == b_b == c_c:
        tri_name = tri_name + 'Equilateral'
    elif a_a == b_b or a_a == c_c or b_b == c_c:
        tri_name = tri_name + 'Isosceles'
    elif a_a == 0 or b_b == 0 or c_c == 0:
        tri_name = tri_name + 'NotATriangle'
    elif pow(a_a,2) + pow(b_b,2) == pow(c_c,2):
        tri_name = tri_name + 'Right'
    elif pow(c_c,2) + pow(b_b,2) == pow(a_a,2):
        tri_name = tri_name + 'Right'
    elif pow(a_a,2) + pow(c_c,2) == pow(b_b,2):
        tri_name = tri_name + 'Right'
    else:
        tri_name = tri_name + 'Scalene'
    return tri_name

def run_classify_triangle(a_a, b_b, c_c):
    """Shows off classify triangle"""

    print('classifyTriangle(',a_a, ',', b_b, ',', c_c, ')=',classify_triangle(a_a,b_b,c_c),sep="")
if __name__ == '__main__':

    classify_triangle(1,2,3)
    run_classify_triangle(1,2,3)
    run_classify_triangle(1,1,1)
