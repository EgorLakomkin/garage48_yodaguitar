/*
var dataTemp = JSON.stringify( { "data" :[ 
					{"id" : 1 , "timeshift" : 0.1 , "string" : 1 , "position" : 4 },
					{"id" : 2 , "timeshift" : 0.2 , "string" : 2 , "position" : 3 },
					{"id" : 3 , "timeshift" : 0.4 , "string" : 3 , "position" : 5 },
					{"id" : 4 , "timeshift" : 0.5 , "string" : 3 , "position" : 2 },
					{"id" : 5 , "timeshift" : 0.7 , "string" : 4 , "position" : 3 },
					{"id" : 6 , "timeshift" : 0.8 , "string" : 3 , "position" : 5 },
					{"id" : 7 , "timeshift" : 0.9 , "string" : 2 , "position" : 7 },
					{"id" : 8 , "timeshift" : 1.2 , "string" : 3 , "position" : 4 },
					{"id" : 9 , "timeshift" : 1.3 , "string" : 4 , "position" : 5 },

					]});
					*/
var dataTemp = JSON.stringify( 
				{ "data" :[
{"id" : "1" , "info" : {"note" : "A", "octave" : "2", "string":"1", "position": "5" } , "timeshift":"2.0" , "type":"note"  },
{"id" : "2" , "info" : {"note" : "Bb", "octave" : "2", "string":"1", "position": "6" } , "timeshift":"2.5" , "type":"note"  },
{"id" : "3" , "info" : {"note" : "B", "octave" : "2", "string":"1", "position": "7" } , "timeshift": "3.0" , "type":"note"  },
{"id" : "4" , "info" : {"note" : "C", "octave" : "3", "string":"1", "position": "8" }, "timeshift":"3.5" , "type":"note"  },
{"id" : "5" , "type" : "endbar" , "timeshift" : "3.75"},
{"id" : "6" , "info" : {"note" : "E", "octave" : "2", "string":"2", "position": "5" } , "timeshift":"4.0" , "type":"note"  },
{"id" : "7" , "info" : {"note" : "F", "octave" : "2", "string":"2", "position": "6" }, "timeshift":"4.5" , "type":"note"  },
{"id" : "8" , "info" : {"note" : "Gb", "octave" : "2", "string":"2", "position": "7"}, "timeshift":"5.0" , "type":"note"  },
{"id" : "9" , "info" : {"note" : "G", "octave" : "2", "string":"2", "position": "8"}, "timeshift":"5.5" , "type":"note"  },
{"id" : "10", "type":"endbar","timeshift" : "5.75"}] } );
			

var tabsData = parseData(dataTemp);
var currentTimeShift = 0;
					
function drawNextFrame() {
	currentFrame++;
	draw();
}
var currentFrame = 0;
function draw(canvas) {
	drawGrid(canvas);
	
	drawNotes(canvas);
	
	/*
	if(stop) {
		return;
	}
	if(currentFrame > dataTabs.length) {
		stop = 1;
		return;
	}
	*/
	drawTab(canvas);								
}

function parseData() {
	var obj = {"data": 0};
	obj.data = JSON.parse(dataTemp );
	obj.maxTimeShift = parseFloat(obj.data.data[obj.data.data.length - 1].timeshift) + 1.0;
	return obj;
}
function drawTab(canvas) {
	var w = canvas.width;
	var h = canvas.height;
	var maxTimeShift = tabsData.maxTimeShift;
	currentTimeShift += 0.01;
	var deltaW = tabsData.maxTimeShift / w;
	var x = currentTimeShift/deltaW;
	var wN = 2;
	var maxH = 320;
	h = h > maxH ? maxH : h;
	var y = 0;

	ctx.beginPath();
	ctx.moveTo(x-wN, y);
	ctx.lineTo(x+wN, y);
	ctx.lineTo(x+wN, y+h);
	ctx.lineTo(x-wN, y+h);
	ctx.closePath();
	ctx.fill();	
	
}
function drawNotes(canvas) {
	var w = canvas.width;
	var h = canvas.height;
	var toDraw = true;
	var deltaW = tabsData.maxTimeShift / w;
	var maxH = 320;
	h = h > maxH ? maxH : h;
	var deltaH = h / 8;
	
	for(var i = 0; i < tabsData.data.data.length; i++) {
		if(toDraw) {
			if(tabsData.data.data[i].type == "note") {
				drawNote(tabsData.data.data[i].timeshift / deltaW , deltaH * parseInt( tabsData.data.data[i].info.string) , tabsData.data.data[i].info.position );
				if(Math.abs(tabsData.data.data[i].timeshift - currentTimeShift) < 0.01) {
					var delay = 0; // play one note every quarter second
					var note = 50; // the MIDI note
					var velocity = 60; // how hard the note hits
					// play the note
					MIDI.setVolume(0, 127);
					//MIDI.noteOn(0, note, velocity, delay);
					//MIDI.noteOff(0, note, delay + 0.05);			
				
					MIDI.noteOnName(0, tabsData.data.data[i].info.note+(parseInt(tabsData.data.data[i].info.octave)+2), velocity, delay);
					MIDI.noteOffName(0, tabsData.data.data[i].info.note+(parseInt(tabsData.data.data[i].info.octave)+2), delay + 0.1);			
				}
			} else if(tabsData.data.data[i].type == "endbar"){
				drawEndBar(tabsData.data.data[i].timeshift / deltaW);
			}
		}
	}
}
function drawEndBar(x) {
	var wN = 1;
	ctx.beginPath();
	var h = canvas.height;
	var maxH = 320;
	h = h > maxH ? maxH : h;

	var y = h / 12 ;
	ctx.moveTo(x-wN, y);
	ctx.lineTo(x+wN, y);
	ctx.lineTo(x+wN, y+9*y);
	ctx.lineTo(x-wN, y+9*y);
	ctx.closePath();
	ctx.fill();	
}
// mark = 0 - none , 1 - good , -1 - bad
function drawNote(x,y,label , mark ) {
	var wN = 10;
	var hN = 10;
	var r = 10;
	y-=(hN/2 + 2);
	if(mark == 0){
		ctx.fillStyle = "#00F";
		drawCircle(x,y,r);		
		ctx.font = "9pt Arial";
		ctx.font = 'bold 14px';
	} else if(mark == 1) {
		ctx.fillStyle = "#0F0";
		drawCircle(x,y,r);
		ctx.font = "9pt Arial";
		ctx.font = 'bold 14px';
	} else {
		ctx.fillStyle = "#F00";
		drawCircle(x,y,r);
		ctx.font = "9pt Arial";
		ctx.font = 'bold 14px';
	}
	/*
	ctx.beginPath();
	
	ctx.moveTo(x-wN, y-hN);
	ctx.lineTo(x+wN, y-hN);
	ctx.lineTo(x+wN, y+hN);
	ctx.lineTo(x-wN, y+hN);
	ctx.closePath();
	ctx.fill();	
	*/
    y += (hN + 3);
	x += wN/2 + 1;
	ctx.strokeText(label, x , y );
	
}
function drawCircle(x,y,r)
{
	ctx.lineWidth = 1;
	ctx.beginPath();
	ctx.arc( x + r, y + r, r, 0, 2*Math.PI, false );
	ctx.stroke();
	ctx.closePath();
	ctx.fill();
}
function drawGrid(canvas) {
	ctx.fillStyle = "#000";

	var w = canvas.width;
	var h = canvas.height;
	ctx.clearRect(0,0,w,h);
	
	//var deltaW = tabs.maxTimeShift / w;
	var maxH = 320;
	h = h > maxH ? maxH : h;
	var deltaH = h / 8;
	
	//ctx.fillRect(-30, -30, 60, 60);
	ctx.globalAlpha = 1.0;
	var lineWidth = 2;
	var deltaLine = 0.5;
	for( var i = 1; i < 7; i++ ) {
		ctx.beginPath();
		ctx.moveTo(0, i*deltaH);
		ctx.lineTo(w, i*deltaH);
		ctx.lineTo(w, i*deltaH + lineWidth);
		ctx.lineTo(0, i*deltaH + lineWidth);
		lineWidth += deltaLine;
		ctx.closePath();
		ctx.fill();
	}
}