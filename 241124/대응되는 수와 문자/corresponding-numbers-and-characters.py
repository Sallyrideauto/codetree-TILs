def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Parsing the first line for n and m
    n, m = map(int, data[0].split())
    
    # Creating dictionaries for fast lookup
    num_to_string = {}
    string_to_num = {}
    
    # Reading the n strings
    for i in range(1, n + 1):
        string = data[i]
        num_to_string[i] = string
        string_to_num[string] = i
    
    # Reading the m queries and processing them
    result = []
    for i in range(n + 1, n + m + 1):
        query = data[i]
        if query.isdigit():  # If the query is a number
            result.append(num_to_string[int(query)])
        else:  # If the query is a string
            result.append(str(string_to_num[query]))
    
    # Printing all results at once
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()