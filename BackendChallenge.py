"""
In Python file write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER.
Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.
"""
import requests

def count_ederly_items():
    # make a GET request
    url = 'https://coderbyte.com/api/challenges/json/age-counting'
    response = requests.get(url)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
        # get the response body
        data = response.json()
        # Extract the items from the data
        items = data.get('data', '').split(', ')

        #count items with age greater than or equal to 50
        count_50_and_above = sum(1 for item in items \
                                 if 'age=' in item and int(item.split('=')[-1]) >= 50)
        # print the final count
        print(count_50_and_above)
    else:
        print(f"Error: {response.status_code} - {response.text}")

#call the function to perform the task
if __name__ == '__main__':
    print(count_ederly_items())

# Comment
"""
The status code of the response is checked. if it's 200, which means the request was successful, the functions proceeds to process the response.
Otherwise, it prints an error message and exits.
The response body is converted to a Python dictionary using `response.json()`. 
The 'data' field of the dictionary is extracted using data.get('data', ''). This field is expected to be a string of items separated by ', '. The string is split into a list of items using .split(', ').

The function then iterates over each item in the list. If the item contains 'age=' and the number following 'age=' is greater than or equal to 50, it's counted as an "elderly" item. The total number of "elderly" items is calculated using sum(1 for item in items if 'age=' in item and int(item.split('=')[-1]) >= 50).

The total count of "elderly" items is printed to the console.

If the script is run directly (not imported as a module), the if __name__ == '__main__': block is executed, which calls count_elderly_items().

The time complexity of this function is O(n), where n is the number of items in the 'data' field of the response.
This is because each item is processed once to check if it's an "elderly" item. The space complexity is also O(n), as the items are stored in a list.
"""