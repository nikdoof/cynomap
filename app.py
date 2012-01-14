from flask import Flask, Response
from map import CynoMap

app = Flask(__name__)

@app.route('/cynos.svg')
def cynos():
	map = CynoMap(jumprange=13, keyid=525316, vcode="8jIZ4pjpLQOKQsUPY4cSpIy0Rtd4AcBh6HzOOzDC4qFlI0UO7dtJUVSkh7G7NhST").svg.standalone_xml()
	return Response(mimetype='image/svg+xml', response=map)
	
	
if __name__ == '__main__':
	app.run()