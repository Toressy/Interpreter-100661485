from flask import Flask, request, render_template
from basic import run
import io
import sys
import tempfile
from contextlib import redirect_stdout

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    code = ""
    if request.method == "POST":
        code = request.form["code"]

        f = io.StringIO()
        with redirect_stdout(f):
            # Write the submitted code to a temporary file
            with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as temp:
                temp.write(code)
                temp.flush()

                # Read back file contents to pass to the interpreter
                with open(temp.name, "r") as tf:
                    file_content = tf.read()

                # Call your interpreter with filename and code
                result, error = run(temp.name, file_content)

        printed_output = f.getvalue()
        if error:
            output = error.as_string()
        else:
            output = printed_output.strip() or str(result)

    return render_template("index.html", code=code, output=output)

if __name__ == "__main__":
    app.run(debug=True)
