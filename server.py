from flask import Flask, render_template, jsonify, request
from werkzeug import secure_filename
import os
import subprocess

UPLOAD_FOLDER = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'wav_data')
app = Flask('flaskwp1')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def webprint():
    return render_template('index.html') 

@app.route('/analyze', methods=['GET','POST'])
def analyze():
  print request.method
  if request.method == "POST":
      file =  request.files[file_id]
      form_filename = request.form['fname']
      target_file = os.path.join(app.config['UPLOAD_FOLDER'],form_filename)
      filename = secure_filename(target_file)
      file.save(filename)
      
      #run script
      subprocess.Popen("aubiopitch -i " + target_file + " > results.txt", shell=True)
      notes = get_notes_from_file('./results.txt')
      return jsonify(result={"notes": notes})
	    
    
@app.route('/upload_wav', methods=['GET','POST'])
def uploadwav():
	print request.method
	if request.method == "POST":
		try:
			print request.files
			for file_id in  request.files:
				file =  request.files[file_id]
				form_filename = request.form['fname']
				username_id = secure_filename(request.form['username_id'])
				username_dir = os.path.join(app.config['UPLOAD_FOLDER'],username_id)
				print 'username dir', username_dir
				if not os.path.exists(username_dir):
					print "make dir", username_dir
					os.makedirs(username_dir)
				filename = secure_filename(form_filename)
				filename = os.path.join(username_dir, filename )
				file.save(filename)
			return jsonify(result={"status": 200})
		except Exception as e:
			print "exception", e
    
	
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000, debug=True)