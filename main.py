def filter_file_by_keywords(input_filename, keywords):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    filtered_lines = [line for line in lines if any(keyword in line for keyword in keywords)]

    filtered_string = ''.join(filtered_lines)

    print(f"Filtered lines containing any of the keywords: {keywords}")
    for line in filtered_lines:
        print(line.strip())

    print(f"\nTotal lines containing any of the keywords: {len(filtered_lines)}")

def filter_file_by_keywords_data():
    input_filename = "exam.txt"
    keywords_str = "lol, dis"
    keywords = keywords_str.split(",")
    filter_file_by_keywords("exam.txt", keywords)

def main():
    filter_file_by_keywords_data()


if __name__ == "__main__":
    main()