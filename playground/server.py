from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def start():
    return "go to /play to do things"

@app.route('/play')
def boxy():
    return render_template("box.html")


@app.route('/play/<num_boxes>')
def numBoxes(num_boxes):
    num=int(num_boxes)
    return render_template("box_num.html", num=num,)

@app.route('/play/<num_boxes>/<box_color>')
def colorBoxes(num_boxes,box_color):
    num=int(num_boxes)
    box_color=box_color
    return render_template("box_color.html", num=num,box_color=box_color)


if __name__=="__main__":
    app.run(debug=True)
