# html_chatgpt_to_md

This repository contains a Python tool for converting HTML content, particularly formatted for chat logs, into Markdown format. This tool can be used both as a standalone program and as an importable library in other Python scripts.

## Installation

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/PoetzlM/html_chatgpt_to_md.git
cd html_chatgpt_to_md
```

Install the package using pip:

```bash
pip install .
```

This will install all required dependencies and make the `html_chatgpt_to_md` tool available on your system.

## Usage as Standalone Program

Once installed, you can run `html_chatgpt_to_md`
as a standalone command-line tool. You will need to specify the input
HTML file and the output Markdown file paths using command line
arguments:

``` bash
html_chatgpt_to_md -i path_to_input.html -o path_to_output.md
```

### Example:

Assuming you have an HTML file named `example.html`, you can convert it to Markdown like this:

``` bash
html_chatgpt_to_md -i example.html -o converted_example.md
```

This will read `example.html`, convert its content to Markdown, and save the result to `converted_example.md`.

## Usage as a Library

You can also import `html_chatgpt_to_md` into your own Python projects and use it programmatically.

### Example:
``` python
from html_chatgpt_to_md.html_chatgpt_to_md import html_to_markdown

# Call the function
soup, modified_markdown = html_to_markdown(html_content)

# or convert from html file to markdown file, and keep markdown sources in buffer
soup, modified_markdown = html_file_to_markdown_file(input_file, output_file)

print("Markdown conversion completed successfully!")
```

In this example, we import the `html_to_markdown` function from the `html_chatgpt_to_md` module, specify the input and output files, and perform the conversion.

## Contributing

Contributions
to this project are welcome! Please fork the repository and submit pull
requests with any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

