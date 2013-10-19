#!-*- coding:utf-8 -*-
import wave,pyaudio,sys
def detect():
    #because of formal = 0, arr's first array is trash
    formal = 0
    switch = 0
    switch2 = 0
    correct = 0
    target = wave.open('target.wav')
    framelength = target.getnframes()
    framerate = target.getframerate()
    #assume that target.wav is mono
    data = target.readframes(framelength)
    arr = []
    for i in range(0, framelength):
        twobyte = [ord(j) for j in data[i:i+2]]
        if twobyte[0]==0x10 and twobyte[1]==0x0:
            if switch == 0:
                firstzf = i
                switch = 1
            latter = i
            distance = latter - formal
            formal = latter
            arr.append(distance)
            #no tolerance.
            if switch2 == 1:
                if distance == arr[1+correct]:
                    wholef = latter - firstzf - distance
                    correct = correct +1
                else:
                    correct = 0
            else:
                switch2 = 1
            if correct == 2:
                #would it be ok to set correct to 0 ?
                correct = 0
                switch2 = 0
                switch = 0
                arr = []
                formal = 0
                latter = 0
                f2hz = framerate/wholef
                note = "none"
                if f2hz <16.835 and f2hz >15.865: note = 'C0'
                if f2hz <17.835 and f2hz >16.805: note = 'CS0orDb0'
                if f2hz <18.9 and f2hz >17.8: note = 'D0'
                if f2hz <20.025 and f2hz >18.875: note = 'DS0orEb0'
                if f2hz <21.215 and f2hz >19.985: note = 'E0'
                if f2hz <22.475 and f2hz >21.185: note = 'F0'
                if f2hz <23.81 and f2hz >22.43: note = 'FS0orGb0'
                if f2hz <25.23 and f2hz >23.77: note = 'G0'
                if f2hz <26.73 and f2hz >25.19: note = 'GS0orAb0'
                if f2hz <28.32 and f2hz >26.68: note = 'A0'
                if f2hz <30.005 and f2hz >28.275: note = 'AS0orBb0'
                if f2hz <31.785 and f2hz >29.955: note = 'B0'
                if f2hz <33.675 and f2hz >31.725: note = 'C1'
                if f2hz <35.68 and f2hz >33.62: note = 'CS1orDb1'
                if f2hz <37.8 and f2hz >35.62: note = 'D1'
                if f2hz <40.045 and f2hz >37.735: note = 'DS1orEb1'
                if f2hz <42.425 and f2hz >39.975: note = 'E1'
                if f2hz <44.95 and f2hz >42.35: note = 'F1'
                if f2hz <47.625 and f2hz >44.875: note = 'FS1orGb1'
                if f2hz <50.455 and f2hz >47.545: note = 'G1'
                if f2hz <53.455 and f2hz >50.365: note = 'GS1orAb1'
                if f2hz <56.635 and f2hz >53.365: note = 'A1'
                if f2hz <60.005 and f2hz >56.535: note = 'AS1orBb1'
                if f2hz <63.575 and f2hz >59.905: note = 'B1'
                if f2hz <67.355 and f2hz >63.465: note = 'C2'
                if f2hz <71.36 and f2hz >67.24: note = 'CS2orDb2'
                if f2hz <75.6 and f2hz >71.24: note = 'D2'
                if f2hz <80.095 and f2hz >75.465: note = 'DS2orEb2'
                if f2hz <84.86 and f2hz >79.96: note = 'E2'
                if f2hz <89.905 and f2hz >84.715: note = 'F2'
                if f2hz <95.25 and f2hz >89.75: note = 'FS2orGb2'
                if f2hz <100.915 and f2hz >95.085: note = 'G2'
                if f2hz <106.915 and f2hz >100.745: note = 'GS2orAb2'
                if f2hz <113.27 and f2hz >106.73: note = 'A2'
                if f2hz <120.005 and f2hz >113.075: note = 'AS2orBb2'
                if f2hz <127.14 and f2hz >119.8: note = 'B2'
                if f2hz <134.7 and f2hz >126.92: note = 'C3'
                if f2hz <142.71 and f2hz >134.47: note = 'CS3orDb3'
                if f2hz <151.195 and f2hz >142.465: note = 'D3'
                if f2hz <160.185 and f2hz >150.935: note = 'DS3orEb3'
                if f2hz <169.71 and f2hz >159.91: note = 'E3'
                if f2hz <179.805 and f2hz >169.415: note = 'F3'
                if f2hz <190.5 and f2hz >179.5: note = 'FS3orGb3'
                if f2hz <201.825 and f2hz >190.175: note = 'G3'
                if f2hz <213.825 and f2hz >201.475: note = 'GS3orAb3'
                if f2hz <226.54 and f2hz >213.46: note = 'A3'
                if f2hz <240.01 and f2hz >226.15: note = 'AS3orBb3'
                if f2hz <254.285 and f2hz >239.595: note = 'B3'
                if f2hz <269.405 and f2hz >253.855: note = 'C4'
                if f2hz <285.42 and f2hz >268.94: note = 'CS4orDb4'
                if f2hz <302.395 and f2hz >284.925: note = 'D4'
                if f2hz <320.38 and f2hz >301.88: note = 'DS4orEb4'
                if f2hz <339.43 and f2hz >319.83: note = 'E4'
                if f2hz <359.61 and f2hz >338.85: note = 'F4'
                if f2hz <380.995 and f2hz >358.985: note = 'FS4orGb4'
                if f2hz <403.65 and f2hz >380.35: note = 'G4'
                if f2hz <427.65 and f2hz >402.95: note = 'GS4orAb4'
                if f2hz <453.08 and f2hz >426.92: note = 'A4'
                if f2hz <480.02 and f2hz >452.3: note = 'AS4orBb4'
                if f2hz <508.565 and f2hz >479.195: note = 'B4'
                if f2hz <538.81 and f2hz >507.69: note = 'C5'
                if f2hz <570.85 and f2hz >537.89: note = 'CS5orDb5'
                if f2hz <604.79 and f2hz >569.87: note = 'D5'
                if f2hz <640.755 and f2hz >603.745: note = 'DS5orEb5'
                if f2hz <678.86 and f2hz >639.66: note = 'E5'
                if f2hz <719.225 and f2hz >677.695: note = 'F5'
                if f2hz <761.99 and f2hz >717.99: note = 'FS5orGb5'
                if f2hz <807.3 and f2hz >760.68: note = 'G5'
                if f2hz <855.305 and f2hz >805.915: note = 'GS5orAb5'
                if f2hz <906.165 and f2hz >853.835: note = 'A5'
                if f2hz <960.05 and f2hz >904.61: note = 'AS5orBb5'
                if f2hz <1017.135 and f2hz >958.405: note = 'B5'
                if f2hz <1077.615 and f2hz >1015.385: note = 'C6'
                if f2hz <1141.695 and f2hz >1075.765: note = 'CS6orDb6'
                if f2hz <1209.585 and f2hz >1139.735: note = 'D6'
                if f2hz <1281.51 and f2hz >1207.51: note = 'DS6orEb6'
                if f2hz <1357.71 and f2hz >1279.31: note = 'E6'
                if f2hz <1438.445 and f2hz >1355.375: note = 'F6'
                if f2hz <1523.98 and f2hz >1435.98: note = 'FS6orGb6'
                if f2hz <1614.6 and f2hz >1521.36: note = 'G6'
                if f2hz <1710.61 and f2hz >1611.83: note = 'GS6orAb6'
                if f2hz <1812.33 and f2hz >1707.67: note = 'A6'
                if f2hz <1920.095 and f2hz >1809.225: note = 'AS6orBb6'
                if f2hz <2034.265 and f2hz >1916.795: note = 'B6'
                if f2hz <2155.23 and f2hz >2030.77: note = 'C7'
                if f2hz <2283.39 and f2hz >2151.53: note = 'CS7orDb7'
                if f2hz <2419.17 and f2hz >2279.47: note = 'D7'
                if f2hz <2563.02 and f2hz >2415.02: note = 'DS7orEb7'
                if f2hz <2715.425 and f2hz >2558.615: note = 'E7'
                if f2hz <2876.895 and f2hz >2710.765: note = 'F7'
                if f2hz <3047.96 and f2hz >2871.96: note = 'FS7orGb7'
                if f2hz <3229.2 and f2hz >3042.72: note = 'G7'
                if f2hz <3421.22 and f2hz >3223.66: note = 'GS7orAb7'
                if f2hz <3624.655 and f2hz >3415.345: note = 'A7'
                if f2hz <3840.19 and f2hz >3618.43: note = 'AS7orBb7'
                if f2hz <4068.54 and f2hz >3833.6: note = 'B7'
                if f2hz <4310.465 and f2hz >4061.555: note = 'C8'
                if f2hz <4566.78 and f2hz >4303.06: note = 'CS8orDb8'
                if f2hz <4838.335 and f2hz >4558.945: note = 'D8'
                if f2hz <2489.015 and f2hz >7467.045: note = 'DS8orEb8'
                print note
                print "\n"

def record():
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 1
    WAVE_OUTPUT_FILENAME = "target.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)
    all = []
    for i in range(0, RATE / chunk * RECORD_SECONDS):
        data = stream.read(chunk)
        all.append(data)
    stream.close()
    p.terminate()

    # write data to WAVE file
    data = ''.join(all)
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

print "start recording for 1 sec"
record()
print "done"
detect()