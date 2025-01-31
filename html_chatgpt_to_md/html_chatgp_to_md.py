# -*- coding: utf-8 -*-
"""
Created on Tue Jan 7 17:36:52 2025
@author: PoetzlM
"""

import sys
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def find_all(a_str, sub):
    """Yield all start positions of the substring 'sub' in 'a_str'."""
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

def correct_code_blocks(text):
    # Initialize the positions for the search
    start_index = text.find("# ")
    while start_index != -1:  # As long as a "# " is found
        end_index = text.find("\n#", start_index + 1)

        if end_index == -1:  # If no further "# " is found
            # Work with the text from the first "# " to the end
            check_text = text[start_index:]
        else:
            # Work with the text between the two "# "
            check_text = text[start_index:end_index]
        
        # Count the occurrences of "```"
        triple_ticks_count = check_text.count("```")
        
        # Check if the number of "```" is odd
        if triple_ticks_count % 2 != 0:
            if end_index == -1:
                # Add "\n```\n" at the end before the text ends
                text = text[:start_index] + check_text + "\n```\n"
            else:
                # Insert "\n```\n" before the second "# "
                text = text[:end_index] + "\n```\n" + text[end_index:]
        
        # Update the start_index for the next search
        start_index = text.find("# ", end_index if end_index != -1 else len(text))
    
    return text

def modify_string(input_string, replacements):
    """Modify the input_string by inserting replacements in between code block backticks."""
    
    # remove preamble of webinterface
    input_string = input_string[input_string.find('#####'):]
    
    # repair code blocks with language information
    
    positions = list(find_all(input_string, '```'))

    pos = 0
    for i in range(len(positions)):
        pos += input_string[pos:].find('```')
        pos += 3
        if i % 2 == 0:
            
            #not pretty error handling, if the chatGPT markdown output fails.
            try:
                replace_str = " " + replacements[i//2]
            except IndexError:
                replace_str = " " + replacements[-1]
                
                
            input_string = input_string[:pos] + replace_str + input_string[pos:]
            pos += len(replace_str)
        else:
            newline_index = input_string.rfind('\n', 0, pos)
            input_string = input_string[:newline_index] + '```\n' + input_string[pos:]

    #add additional carrier return 
    input_string = input_string.replace("######", "\n######")
    
    # correct stoped code generation
    input_string = correct_code_blocks(input_string)
    
    return input_string

def html_to_markdown(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unnecessary elements from HTML
    for ele in soup.find_all('div', class_="gizmo-bot-avatar flex h-8 w-8 items-center justify-center overflow-hidden rounded-full"):
        ele.decompose()

    # Extract and remove certain elements, store types for later modifications
    script_types = []
    for ele in soup.find_all('div', class_="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none"):
        script_types.extend([str(t) for t in ele])
        ele.decompose()

    # Remove buttons and scripts
    for button in soup.find_all('button'):
        button.decompose()
    for script in soup(["script", "style"]):
        script.decompose()

    # Convert to Markdown
    markdown_text = md(str(soup), heading_style="ATX")
    modified_markdown = modify_string(markdown_text, script_types)

    return soup, modified_markdown


def html_file_to_markdown_file(input_file, output_file):
    """Convert HTML content from input_file to markdown format and save it to output_file."""
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup, modified_markdown = html_to_markdown(html_content)
    
    # Write the modified markdown to the output file
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(modified_markdown)

    print(f"Markdown file has been successfully created and saved to {output_file}.")
    return soup, modified_markdown

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert HTML file to Markdown")
    parser.add_argument('-i', '--input', help="Input HTML file path", required=True)
    parser.add_argument('-o', '--output', help="Output Markdown file path", required=True)
    args = parser.parse_args()

    # Run conversion
    html_file_to_markdown_file(args.input, args.output)
