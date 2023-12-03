from ArrChallenge import FindIntersection

def test_FindIntersection():
    # Test case 1: Intersection exists
    input1 = "1, 2, 3, 4, 5, 6"
    input2 = "4, 5, 6, 7, 8, 9"
    assert FindIntersection(input1 + "," + input2) == "4,5,6"

    # Test case 2: No intersection
    input1 = "1, 2, 3"
    input2 = "4, 5, 6"
    assert FindIntersection(input1 + "," + input2) == "false"

    # Test case 3: Intersection with negative numbers
    input1 = "-1, 0, 1, 2, 3"
    input2 = "0, 1, 2, 3, 4"
    assert FindIntersection(input1 + "," + input2) == "0,1,2,3"

    # Test case 4: Intersection with duplicate numbers
    input1 = "1, 2, 2, 3, 4"
    input2 = "2, 3, 4, 4, 5"
    assert FindIntersection(input1 + "," + input2) == "2,3,4"

    # Test case 5: Intersection with empty input
    input1 = ""
    input2 = "1, 2, 3"
    assert FindIntersection(input1 + "," + input2) == "false"

    # Test case 6: Intersection with single element
    input1 = "1"
    input2 = "1"
    assert FindIntersection(input1 + "," + input2) == "1"

    # Test case 7: Intersection with large numbers
    input1 = "1000000, 2000000, 3000000"
    input2 = "2000000, 3000000, 4000000"
    assert FindIntersection(input1 + "," + input2) == "2000000,3000000"

    # Test case 8: Intersection with floating point numbers
    input1 = "1.5, 2.5, 3.5"
    input2 = "2.5, 3.5, 4.5"
    assert FindIntersection(input1 + "," + input2) == "2.5,3.5"