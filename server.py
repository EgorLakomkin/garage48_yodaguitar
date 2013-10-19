#!-*-coding:utf-8-*-
from flask import Flask, render_template, jsonify, request
from werkzeug import secure_filename
import os
import subprocess
from liba_process import get_notes_from_file
import uuid 
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

root_dirname, root_filename = os.path.split(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'wav_data')
app = Flask('flaskwp1')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

test_json = [
    {
        "id": "1",
        "info": {
            "notes": [
                {
                    "note": "A",
                    "octave": "2",
                    "string": "1",
                    "position": "5"
                }
            ],
            "type": "note",
            "timeshift": "2.0"
        }
},
        {
            "id": "2",
            "info": {
                "notes": [
                    {
                        "note": "AS",
                        "octave": "2",
                        "string": "1",
                        "position": "6"
                    }
                ],
                "type": "note",
                "timeshift": "2.5"
            }
},
            {
                "id": "3",
                "info": {
                    "notes": [
                        {
                            "note": "B",
                            "octave": "2",
                            "string": "1",
                            "position": "7"
                        }
                    ],
                    "type": "note",
                    "timeshift": "3.0"
                }
},
                {
                    "id": "4",
                    "info": {
                        "notes": [
                            {
                                "note": "C",
                                "octave": "3",
                                "string": "1",
                                "position": "8"
                            }
                        ],
                        "type": "note",
                        "timeshift": "3.5"
                    
}},
                    {
                        "id": "6",
                        "info": {
                            "notes": [
                                {
                                    "note": "E",
                                    "octave": "2",
                                    "string": "2",
                                    "position": "5"
                                }
                            ]
                        },
                        "type": "note",
                        "timeshift": "4.0"
                    }
,
                    {
                        "id": "7",
                        "info": {
                            "notes": [
                                {
                                    "note": "F",
                                    "octave": "2",
                                    "string": "2",
                                    "position": "6"
                                }
                            ],
                            "type": "note",
                            "timeshift": "4.5"
                        }
},
                        {
                            "id": "8",
                            "info": {
                                "notes": [
                                    {
                                        "note": "FS",
                                        "octave": "2",
                                        "string": "2",
                                        "position": "7"
                                    }
                                ],
                                "type": "note",
                                "timeshift": "5.0"
                            }
},
                            {
                                "id": "9",
                                "info": {
                                    "notes": [
                                        {
                                            "note": "G",
                                            "octave": "2",
                                            "string": "2",
                                            "position": "8"
                                        }
                                    ],
                                    "timeshift": "5.5",
                                    "type": "note"
                                }
                            }
                        ]

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@crossdomain(origin='*') 
@app.route('/')
def webprint():
    return render_template('index.html') 

@crossdomain(origin='*') 
@app.route('/analyze', methods=['GET','POST'])
def analyze():
  print request.method
  if request.method == "POST":
    for file_id in  request.files:
      file =  request.files[file_id]
      form_filename = request.form['fname']
      target_file = os.path.join(app.config['UPLOAD_FOLDER'],form_filename)
      
      
      #filename = secure_filename(target_file)
      #print "Saved wav", filename
      #file.save(filename)
      
      #run script
      #filename_result = str(uuid.uuid4()) + "_result.txt"
      #print filename_result
      #logfile = open(filename_result, 'w+')
      #full_filename = os.path.join(root_dirname, filename)
      #print "Save fullname", full_filename
      #p = subprocess.Popen("aubiopitch -i " + full_filename, shell=True, stdout = logfile)
      #ret_code = p.wait()
      #logfile.flush()
      #logfile.close()
      #notes = get_notes_from_file( os.path.join(root_dirname, filename_result) )
      #print notes
      #return jsonify(result={"notes": notes})
      return jsonify(result=test_json)
	    
@crossdomain(origin='*') 
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
