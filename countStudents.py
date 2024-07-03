def countStudents(self, students, sandwiches):
    """
    :type students: List[int]
    :type sandwiches: List[int]
    :rtype: int
    """
    i = j = 0
    for student in students:
        if student == 0:
            i += 1
        else:
            j += 1
    for sandwich in sandwiches:
        if sandwich == 0:
            if i > 0:
                i -= 1
            else:
                break
        else:
            if j > 0:
                j -= 1
            else:
                break
    return i + j