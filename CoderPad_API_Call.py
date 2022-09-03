import requests
import sys

# Function provided by exercise.
def solution(url):

    # Set global variables.
    return_string = 'No Image Found!'
    final_list = []
    input_url = url

    # Make API request.
    response = requests.get(input_url)

    # Parse API return, create list separted on comma.
    content = str(response.content)
    content_list = content.split(",")

    # Loop through content list searching for .png files, then the tag
    # that identifies the badge on the website.
    for item in content_list:
        if item.__contains__('.png'):
            if item.__contains__('clubBadgeFallback'):

                # Further cut down the lsit to isolate the link only.
                shortlist = item.split('"')
                for shortlist_item in shortlist:

                    # Add only the link to the .png file to the final list.
                    if shortlist_item.__contains__('.png'):
                        final_list.append(shortlist_item)

    # Check to see if any images were found, if not, dont update variable and
    # return 'No images found'.
    if len(final_list) >= 1:
        # Add https: to the start of the link and return the link as a string.
        return_string = 'https:' + str(final_list[0])

    # Return the required string.
    return return_string

# Main function to run code.
def main():
    # Take command line arguments.
    argument_list = sys.argv
    argument_length = len(sys.argv)

    # Check a url has been provided if not, provide usage info.
    if argument_length < 2:
        print('Please add a url to scan.')
        print(('Usage: {0} [Url]'.format(sys.argv[0])))

    # With url being provided, pass into solution function.
    else:
        url_input = argument_list[1]
        solution_string = solution(url_input)
        print(solution_string)

# Main function to run from.
if __name__ == '__main__':

    # Run main method.
    main()
