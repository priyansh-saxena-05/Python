import webbrowser
import os
import tempfile

def view_html(html_content):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        temp_file.write(html_content.encode('utf-8'))
        temp_file_path = temp_file.name

    # Open the temporary file in the default web browser
    webbrowser.open(f'file://{temp_file_path}')

# Example HTML content
html_content = "<HTML><BODY>HELLO WORLD</BODY></HTML>"
view_html(html_content)
