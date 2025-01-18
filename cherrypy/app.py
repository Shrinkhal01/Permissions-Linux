import cherrypy
import json
import os

def convert_input(input_text):
    # Ensure input is a valid Linux permission string with 9 characters (rwxrwxrwx)
    if len(input_text) != 9:
        return "Invalid permission format. Please enter 9 characters (e.g., rwxr-xr--)."

    octal_value = ''

    for i in range(0, 9, 3):
        permissions = input_text[i:i+3]
        octal_digit = 0

        if permissions[0] == 'r':
            octal_digit += 4
        if permissions[1] == 'w':
            octal_digit += 2
        if permissions[2] == 'x':
            octal_digit += 1

        octal_value += str(octal_digit)

    return octal_value

class ConverterApp:
    @cherrypy.expose
    def index(self):
        html_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
        with open(html_path, "r", encoding="utf-8") as file:
            return file.read()

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def convert(self):
        input_data = cherrypy.request.json
        input_text = input_data.get('input', '')
        output_text = convert_input(input_text)
        return {'output': output_text}

if __name__ == '__main__':
    cherrypy.quickstart(ConverterApp(), '/')
