#!-*-coding:utf-8-*-
import sys
import numpy

MAX_FREQ = 880

FREQ = 44100
TEMPO = 90

NUMBER_ZEROS = 6
NUMBER_REGIONS_THRESHOLD = 30

def freq_to_round(f2hz):
  if f2hz <16.835 and f2hz >15.865: return 0.0
  if f2hz <17.835 and f2hz >16.805: return 0.0
  if f2hz <18.9 and f2hz >17.8: return 0.0
  if f2hz <20.025 and f2hz >18.875: return 0.0
  if f2hz <21.215 and f2hz >19.985: return 0.0
  if f2hz <22.475 and f2hz >21.185: return 0.0
  if f2hz <23.81 and f2hz >22.43: return 0.0
  if f2hz <25.23 and f2hz >23.77: return 0.0
  if f2hz <26.73 and f2hz >25.19: return 0.0
  if f2hz <28.32 and f2hz >26.68: return 0.0
  if f2hz <30.005 and f2hz >28.275: return 0.0
  if f2hz <31.785 and f2hz >29.955: return 0.0
  if f2hz <33.675 and f2hz >31.725: return 0.0
  if f2hz <35.68 and f2hz >33.62: return 0.0
  if f2hz <37.8 and f2hz >35.62: return 0.0
  if f2hz <40.045 and f2hz >37.735: return 0.0
  if f2hz <42.425 and f2hz >39.975: return 0.0
  if f2hz <44.95 and f2hz >42.35: return 0.0
  if f2hz <47.625 and f2hz >44.875: return 0.0
  if f2hz <50.455 and f2hz >47.545: return 0.0
  if f2hz <53.455 and f2hz >50.365: return 0.0
  if f2hz <56.635 and f2hz >53.365: return 0.0
  if f2hz <60.005 and f2hz >56.535: return 0.0
  if f2hz <63.575 and f2hz >59.905: return 0.0
  if f2hz <67.355 and f2hz >63.465: return 0.0
  if f2hz <71.36 and f2hz >67.24: return 0.0
  if f2hz <75.6 and f2hz >71.24: return 0.0
  if f2hz <80.095 and f2hz >75.465: return  0.0
  if f2hz <84.86 and f2hz >79.96: return 0.0
  if f2hz <89.905 and f2hz >84.715: return 0.0
  if f2hz <95.25 and f2hz >89.75: return 0.0
  if f2hz <100.915 and f2hz >95.085: return 0.0
  if f2hz <106.915 and f2hz >100.745: return 0.0
  if f2hz <113.27 and f2hz >106.73: return 0.0
  if f2hz <120.005 and f2hz >113.075: return 0.0
  if f2hz <127.14 and f2hz >119.8: return 0.0
  if f2hz <134.7 and f2hz >126.92: return 0.0
  if f2hz <142.71 and f2hz >134.47: return 0.0
  if f2hz <151.195 and f2hz >142.465: return 0.0
  if f2hz <160.185 and f2hz >150.935: return 0.0
  if f2hz <169.71 and f2hz >159.91: return 0.0
  if f2hz <179.805 and f2hz >169.415: return 0.0#(179.80 + 169.415)/ 2
  if f2hz <190.5 and f2hz >179.5: return 0.0#(190.5 + 179.5 ) / 2
  if f2hz <201.825 and f2hz >190.175: return (201.825 + 190.175 ) / 2
  if f2hz <213.825 and f2hz >201.475: return ( 213.825 + 201.475 ) / 2
  if f2hz <226.54 and f2hz >213.46: return (226.54 + 213.46) / 2
  if f2hz <240.01 and f2hz >226.15: return (240.01 + 226.15) / 2
  if f2hz <254.285 and f2hz >239.595: return (254.285 + 239.595) /2
  if f2hz <269.405 and f2hz >253.855: return (269.405 + 253.855 ) / 2
  if f2hz <285.42 and f2hz >268.94: return(285.42 + 268.94) / 2
  if f2hz <302.395 and f2hz >284.925: return (302.395 + 284.925) /2
  if f2hz <320.38 and f2hz >301.88: return (320.38 + 301.88 ) / 2
  if f2hz <339.43 and f2hz >319.83: return (339.43 + 319.83) /2
  if f2hz <359.61 and f2hz >338.85: return (359.61 + 338.85) /2
  if f2hz <380.995 and f2hz >358.985: return (380.995 + 358.985) / 2
  if f2hz <403.65 and f2hz >380.35: return (403.65 + 380.35) / 2
  if f2hz <427.65 and f2hz >402.95: return (427.65 + 402.95) / 2
  if f2hz <453.08 and f2hz >426.92: return (453.08 + 426.92 ) / 2
  if f2hz <480.02 and f2hz >452.3: return (480.02 + 452.3) / 2
  if f2hz <508.565 and f2hz >479.195: return (508.565 + 479.195) / 2
  if f2hz <538.81 and f2hz >507.69: return (538.81 + 507.69) / 2
  if f2hz <570.85 and f2hz >537.89: return (570.85 + 537.89)/ 2
  if f2hz <604.79 and f2hz >569.87: return (604.79 + 569.87) / 2
  if f2hz <640.755 and f2hz >603.745: return (640.755 + 603.745) / 2
  if f2hz <678.86 and f2hz >639.66: return (678.86 + 639.66) / 2
  if f2hz <719.225 and f2hz >677.695: return (719.225 + 677.695) / 2
  if f2hz <761.99 and f2hz >717.99: return (761.99 + 717.99) / 2
  if f2hz <807.3 and f2hz >760.68: return (807.3 + 760.68) /2
  if f2hz <855.305 and f2hz >805.915: return (855.305 + 805.915) / 2
  if f2hz <906.165 and f2hz >853.835: return (853.835 + 906.165) / 2
  if f2hz <960.05 and f2hz >904.61: return (960.05 + 904.61) / 2
  if f2hz <1017.135 and f2hz >958.405: return (1017.135 + 958.405) / 2
  if f2hz <1077.615 and f2hz >1015.385: return (1077.615 + 1015.385 )  /2
  if f2hz <1141.695 and f2hz >1075.765: return (1141.695 + 1075.765) / 2
  if f2hz <1209.585 and f2hz >1139.735: return (1209.585 + 1139.735 ) /2
  if f2hz <1281.51 and f2hz >1207.51: return (1281.51 + 1207.51 ) /2
  if f2hz <1357.71 and f2hz >1279.31: return (1357.71 + 1279.31) /2
  if f2hz <1438.445 and f2hz >1355.375: return (1438.445 + 1355.375 ) /2
  if f2hz <1523.98 and f2hz >1435.98: return (1523.98 + 1435.98) / 2
  if f2hz <1614.6 and f2hz >1521.36: return (1614.6 + 1521.36) / 2
  if f2hz <1710.61 and f2hz >1611.83: return (1710.61 + 1611.83) /2
  if f2hz <1812.33 and f2hz >1707.67: return (1812.33 + 1707.67) /2
  if f2hz <1920.095 and f2hz >1809.225: return (1920.095 + 1809.225 ) /2
  if f2hz <2034.265 and f2hz >1916.795: return (2034.265 + 1916.795) /2
  if f2hz <2155.23 and f2hz >2030.77: return (2155.23 + 2030.77) /2
  if f2hz <2283.39 and f2hz >2151.53: return (2283.39 + 2151.53 ) /2
  if f2hz <2419.17 and f2hz >2279.47: return (2419.17 + 2279.47) /2
  if f2hz <2563.02 and f2hz >2415.02: return (2563.02 + 2415.02) /2
  if f2hz <2715.425 and f2hz >2558.615: return (2715.425 + 2558.615) /2
  if f2hz <2876.895 and f2hz >2710.765: return 0.0
  if f2hz <3047.96 and f2hz >2871.96: return 0.0
  if f2hz <3229.2 and f2hz >3042.72: return 0.0
  if f2hz <3421.22 and f2hz >3223.66: return 0.0
  if f2hz <3624.655 and f2hz >3415.345: return 0.0
  if f2hz <3840.19 and f2hz >3618.43: return 0.0
  if f2hz <4068.54 and f2hz >3833.6: return 0.0
  if f2hz <4310.465 and f2hz >4061.555: return 0.0
  if f2hz <4566.78 and f2hz >4303.06: return 0.0
  if f2hz <4838.335 and f2hz >4558.945: return 0.0
  if f2hz <2489.015 and f2hz >7467.045: return 0.0
  return 0.0

def freq_to_note(f2hz):
  note = None
  if f2hz <16.835 and f2hz >15.865: note = {}
  if f2hz <17.835 and f2hz >16.805: note = {}
  if f2hz <18.9 and f2hz >17.8: note = {}
  if f2hz <20.025 and f2hz >18.875: note = {}
  if f2hz <21.215 and f2hz >19.985: note = {}
  if f2hz <22.475 and f2hz >21.185: note = {}
  if f2hz <23.81 and f2hz >22.43: note = {}
  if f2hz <25.23 and f2hz >23.77: note = {}
  if f2hz <26.73 and f2hz >25.19: note = {}
  if f2hz <28.32 and f2hz >26.68: note = {}
  if f2hz <30.005 and f2hz >28.275: note = {}
  if f2hz <31.785 and f2hz >29.955: note = {}
  if f2hz <33.675 and f2hz >31.725: note = {}
  if f2hz <35.68 and f2hz >33.62: note = {}
  if f2hz <37.8 and f2hz >35.62: note = {}
  if f2hz <40.045 and f2hz >37.735: note = {}
  if f2hz <42.425 and f2hz >39.975: note = {}
  if f2hz <44.95 and f2hz >42.35: note = {}
  if f2hz <47.625 and f2hz >44.875: note = {}
  if f2hz <50.455 and f2hz >47.545: note = {}
  if f2hz <53.455 and f2hz >50.365: note = {}
  if f2hz <56.635 and f2hz >53.365: note = {}
  if f2hz <60.005 and f2hz >56.535: note = {}
  if f2hz <63.575 and f2hz >59.905: note = {}
  if f2hz <67.355 and f2hz >63.465: note = {}
  if f2hz <71.36 and f2hz >67.24: note = {}
  if f2hz <75.6 and f2hz >71.24: note = {}
  if f2hz <80.095 and f2hz >75.465: note = {}
  if f2hz <84.86 and f2hz >79.96: note = {}
  if f2hz <89.905 and f2hz >84.715: note = {}
  if f2hz <95.25 and f2hz >89.75: note = {}
  if f2hz <100.915 and f2hz >95.085: note = {}
  if f2hz <106.915 and f2hz >100.745: note = {}
  if f2hz <113.27 and f2hz >106.73: note = {}
  if f2hz <120.005 and f2hz >113.075: note = {}
  if f2hz <127.14 and f2hz >119.8: note = {}
  if f2hz <134.7 and f2hz >126.92: note = {}
  if f2hz <142.71 and f2hz >134.47: note = {}
  if f2hz <151.195 and f2hz >142.465: note = {}
  if f2hz <160.185 and f2hz >150.935: note = {}
  if f2hz <169.71 and f2hz >159.91: note = {}
  if f2hz <179.805 and f2hz >169.415: note = {'notes' : [{ 'octave' :'3', 'note' : 'F', 'string' : '4', 'position' : '3'}, { 'octave' :'3', 'note' : 'F', 'string' : '5', 'position' : '8'}] }
  if f2hz <190.5 and f2hz >179.5: note ={'notes' : [{ 'octave' :'3', 'note' : 'FS', 'string' : '4', 'position' : '4'}, { 'octave' :'3', 'note' : 'FS', 'string' : '5', 'position' : '9'}] }
  if f2hz <201.825 and f2hz >190.175: note = {'notes' : [{ 'octave' :'3', 'note' : 'G', 'string' : '4', 'position' : '5'}, { 'octave' :'3', 'note' : 'G', 'string' : '5', 'position' : '10'}] }
  if f2hz <213.825 and f2hz >201.475: note = {'notes' : [{ 'octave' :'3', 'note' : 'GS', 'string' : '4', 'position' : '6'}, { 'octave' :'3', 'note' : 'GS', 'string' : '5', 'position' : '11'}] }
  if f2hz <226.54 and f2hz >213.46: note = {'notes' : [{ 'octave' :'3', 'note' : 'A', 'string' : '4', 'position' : '7'}, { 'octave' :'3', 'note' : 'A', 'string' : '5', 'position' : '12'}] }
  if f2hz <240.01 and f2hz >226.15: note = {'notes' : [{ 'octave' :'3', 'note' : 'Bb', 'string' : '4', 'position' : '8'}, { 'octave' :'3', 'note' : 'Bb', 'string' : '5', 'position' : '13'}] }
  if f2hz <254.285 and f2hz >239.595: note = {'notes' : [{ 'octave' :'4', 'note' : 'B', 'string' : '2', 'position' : '0'},{ 'octave' :'4', 'note' : 'B', 'string' : '3', 'position' : '4'}] }
  if f2hz <269.405 and f2hz >253.855: note = {'notes' : [{ 'octave' :'4', 'note' : 'C', 'string' : '2', 'position' : '1'},{ 'octave' :'4', 'note' : 'C', 'string' : '3', 'position' : '5'}] }
  if f2hz <285.42 and f2hz >268.94: note = {'notes' : [{ 'octave' :'4', 'note' : 'CS', 'string' : '2', 'position' : '2'}, { 'octave' :'4', 'note' : 'CS', 'string' : '3', 'position' : '6'}] }
  if f2hz <302.395 and f2hz >284.925: note = {'notes' : [{ 'octave' :'4', 'note' : 'D', 'string' : '2', 'position' : '3'},{ 'octave' :'4', 'note' : 'D', 'string' : '3', 'position' : '7'}] }
  if f2hz <320.38 and f2hz >301.88: note = {'notes' : [{ 'octave' :'4', 'note' : 'DS', 'string' : '2', 'position' : '4'},{ 'octave' :'4', 'note' : 'DS', 'string' : '3', 'position' : '8'}] }
  if f2hz <339.43 and f2hz >319.83: note = {'notes' : [{ 'octave' :'4', 'note' : 'E', 'string' : '2', 'position' : '5'},{ 'octave' :'4', 'note' : 'E', 'string' : '3', 'position' : '9'}] }
  if f2hz <359.61 and f2hz >338.85: note = {'notes' : [{ 'octave' :'4', 'note' : 'F', 'string' : '2', 'position' : '6'}, { 'octave' :'4', 'note' : 'F', 'string' : '3', 'position' : '10'}] }
  if f2hz <380.995 and f2hz >358.985: note = {'notes' : [{ 'octave' :'4', 'note' : 'FS', 'string' : '2', 'position' : '7'}, { 'octave' :'4', 'note' : 'FS', 'string' : '3', 'position' : '11'}] }
  if f2hz <403.65 and f2hz >380.35: note = {'notes' : [{ 'octave' :'4', 'note' : 'G', 'string' : '2', 'position' : '8'}, { 'octave' :'4', 'note' : 'G', 'string' : '3', 'position' : '12'}] }
  if f2hz <427.65 and f2hz >402.95: note = {'notes' : [{ 'octave' :'4', 'note' : 'GS', 'string' : '2', 'position' : '9'}, { 'octave' :'4', 'note' : 'GS', 'string' : '3', 'position' : '13'}] }
  if f2hz <453.08 and f2hz >426.92: note = {'notes' : [{ 'octave' :'4', 'note' : 'A', 'string' : '1', 'position' : '5'}, { 'octave' :'4', 'note' : 'A', 'string' : '3', 'position' : '14'}] }
  if f2hz <480.02 and f2hz >452.3: note = {'notes' : [{ 'octave' :'4', 'note' : 'Bb', 'string' : '1', 'position' : '6'}, { 'octave' :'4', 'note' : 'Bb', 'string' : '3', 'position' : '15'}] }
  if f2hz <508.565 and f2hz >479.195: note = {'notes' : [{ 'octave' :'4', 'note' : 'B', 'string' : '1', 'position' : '7'}, { 'octave' :'4', 'note' : 'B', 'string' : '3', 'position' : '16'}] }
  if f2hz <538.81 and f2hz >507.69: note = {'notes' : [{ 'octave' :'4', 'note' : 'C', 'string' : '1', 'position' : '8'}, { 'octave' :'4', 'note' : 'C', 'string' : '3', 'position' : '17'}] }
  if f2hz <570.85 and f2hz >537.89: note = {'notes' : [{ 'octave' :'5', 'note' : 'CS', 'string' : '1', 'position' : '9'},{ 'octave' :'4', 'note' : 'CS', 'string' : '3', 'position' : '18'} ] }
  if f2hz <604.79 and f2hz >569.87: note = {'notes' : [{ 'octave' :'5', 'note' : 'D', 'string' : '1', 'position' : '10'},{ 'octave' :'4', 'note' : 'D', 'string' : '2', 'position' : '15'} ,{ 'octave' :'4', 'note' : 'D', 'string' : '3', 'position' : '19'} ] }
  if f2hz <640.755 and f2hz >603.745: note ={'notes' : [{ 'octave' :'5', 'note' : 'DS', 'string' : '1', 'position' : '11'},{ 'octave' :'4', 'note' : 'DS', 'string' : '2', 'position' : '16'} ,{ 'octave' :'4', 'note' : 'DS', 'string' : '3', 'position' : '20'} ] }
  if f2hz <678.86 and f2hz >639.66: note = {'notes' : [{ 'octave' :'5', 'note' : 'E', 'string' : '1', 'position' : '12'},{ 'octave' :'4', 'note' : 'E', 'string' : '2', 'position' : '17'},{ 'octave' :'4', 'note' : 'E', 'string' : '3', 'position' : '21'} ] }
  if f2hz <719.225 and f2hz >677.695: note = {'notes' : [{ 'octave' :'5', 'note' : 'F', 'string' : '1', 'position' : '13'},{ 'octave' :'4', 'note' : 'F', 'string' : '2', 'position' : '18'} ,{ 'octave' :'4', 'note' : 'F', 'string' : '3', 'position' : '22'} ] }
  if f2hz <761.99 and f2hz >717.99: note = {'notes' : [{ 'octave' :'5', 'note' : 'FS', 'string' : '1', 'position' : '14'},{ 'octave' :'4', 'note' : 'FS', 'string' : '2', 'position' : '19'} ,{ 'octave' :'4', 'note' : 'FS', 'string' : '3', 'position' : '23'} ] }
  if f2hz <807.3 and f2hz >760.68: note = {'notes' : [{ 'octave' :'5', 'note' : 'G', 'string' : '1', 'position' : '15'},{ 'octave' :'4', 'note' : 'G', 'string' : '2', 'position' : '20'} ,{ 'octave' :'4', 'note' : 'G', 'string' : '3', 'position' : '24'} ] }
  if f2hz <855.305 and f2hz >805.915: note = {'notes' : [{ 'octave' :'5', 'note' : 'GS', 'string' : '1', 'position' : '16'},{ 'octave' :'4', 'note' : 'GS', 'string' : '2', 'position' : '21'} ,{ 'octave' :'4', 'note' : 'GS', 'string' : '3', 'position' : '25'} ] }
  if f2hz <906.165 and f2hz >853.835: note = {'notes' : [{ 'octave' :'5', 'note' : 'A', 'string' : '1', 'position' : '17'},{ 'octave' :'4', 'note' : 'A', 'string' : '2', 'position' : '22'} ,{ 'octave' :'4', 'note' : 'A', 'string' : '3', 'position' : '26'} ] }
  if f2hz <960.05 and f2hz >904.61: note = {'notes' : [{ 'octave' :'5', 'note' : 'Bb', 'string' : '1', 'position' : '18'},{ 'octave' :'4', 'note' : 'Bb', 'string' : '2', 'position' : '23'} ,{ 'octave' :'4', 'note' : 'Bb', 'string' : '3', 'position' : '27'} ] }
  if f2hz <1017.135 and f2hz >958.405: note = {'notes' : [{ 'octave' :'5', 'note' : 'B', 'string' : '1', 'position' : '19'},{ 'octave' :'4', 'note' : 'B', 'string' : '2', 'position' : '24'}]}
  if f2hz <1077.615 and f2hz >1015.385: note = {'notes' : [{ 'octave' :'5', 'note' : 'C', 'string' : '1', 'position' : '20'},{ 'octave' :'4', 'note' : 'C', 'string' : '2', 'position' : '25'}]}
  if f2hz <1141.695 and f2hz >1075.765: note = {'notes' : [{ 'octave' :'5', 'note' : 'CS', 'string' : '1', 'position' : '21'}]}
  if f2hz <1209.585 and f2hz >1139.735: note =  {'notes' : [{ 'octave' :'5', 'note' : 'D', 'string' : '1', 'position' : '22'}]}
  if f2hz <1281.51 and f2hz >1207.51: note = {'notes' : [{ 'octave' :'5', 'note' : 'DS', 'string' : '1', 'position' : '23'}]}
  if f2hz <1357.71 and f2hz >1279.31: note = {'notes' : [{ 'octave' :'5', 'note' : 'E', 'string' : '1', 'position' : '24'}]}
  if f2hz <1438.445 and f2hz >1355.375: note =  {'notes' : [{ 'octave' :'5', 'note' : 'F', 'string' : '1', 'position' : '25'}]}
  if f2hz <1523.98 and f2hz >1435.98: note = {'notes' : [{ 'octave' :'5', 'note' : 'FS', 'string' : '1', 'position' : '26'}]}
  if f2hz <1614.6 and f2hz >1521.36: note = {'notes' : [{ 'octave' :'5', 'note' : 'G', 'string' : '1', 'position' : '27'}]}
  if f2hz <1710.61 and f2hz >1611.83: note = {'notes' : [{ 'octave' :'5', 'note' : 'GS', 'string' : '1', 'position' : '28'}]}
  if f2hz <1812.33 and f2hz >1707.67: note = {'notes' : [{ 'octave' :'5', 'note' : 'A', 'string' : '1', 'position' : '29'}]}
  if f2hz <1920.095 and f2hz >1809.225: note = {'notes' : [{ 'octave' :'5', 'note' : 'AS', 'string' : '1', 'position' : '30'}]}
  if f2hz <2034.265 and f2hz >1916.795: note = {'notes' : [{ 'octave' :'5', 'note' : 'B', 'string' : '1', 'position' : '31'}]}
  if f2hz <2155.23 and f2hz >2030.77: note = {'notes' : [{ 'octave' :'5', 'note' : 'C', 'string' : '1', 'position' : '32'}]}
  if f2hz <2283.39 and f2hz >2151.53: note = {'notes' : [{ 'octave' :'5', 'note' : 'CS', 'string' : '1', 'position' : '33'}]}
  if f2hz <2419.17 and f2hz >2279.47: note = {'notes' : [{ 'octave' :'5', 'note' : 'D', 'string' : '1', 'position' : '34'}]}
  if f2hz <2563.02 and f2hz >2415.02: note = {'notes' : [{ 'octave' :'5', 'note' : 'DS', 'string' : '1', 'position' : '35'}]}
  if f2hz <2715.425 and f2hz >2558.615: note = {'notes' : [{ 'octave' :'5', 'note' : 'E', 'string' : '1', 'position' : '36'}]}
  if f2hz <2876.895 and f2hz >2710.765: note = {'notes' : [{ 'octave' :'5', 'note' : 'F', 'string' : '1', 'position' : '37'}]}
  if f2hz <3047.96 and f2hz >2871.96: note = {'notes' : [{ 'octave' :'5', 'note' : 'FS', 'string' : '1', 'position' : '38'}]}
  if f2hz <3229.2 and f2hz >3042.72: note = {'notes' : [{ 'octave' :'5', 'note' : 'G', 'string' : '1', 'position' : '39'}]}
  if f2hz <3421.22 and f2hz >3223.66: note = {'notes' : [{ 'octave' :'5', 'note' : 'GS', 'string' : '1', 'position' : '40'}]}
  if f2hz <3624.655 and f2hz >3415.345: note = {'notes' : [{ 'octave' :'5', 'note' : 'A', 'string' : '1', 'position' : '41'}]}
  if f2hz <3840.19 and f2hz >3618.43: note = {'notes' : [{ 'octave' :'5', 'note' : 'AS', 'string' : '1', 'position' : '42'}]}
  if f2hz <4068.54 and f2hz >3833.6: note = {'notes' : [{ 'octave' :'5', 'note' : 'B', 'string' : '1', 'position' : '43'}]}
  if f2hz <4310.465 and f2hz >4061.555: note = {'notes' : [{ 'octave' :'5', 'note' : 'C', 'string' : '1', 'position' : '44'}]}
  if f2hz <4566.78 and f2hz >4303.06: note = {'notes' : [{ 'octave' :'5', 'note' : 'CS', 'string' : '1', 'position' : '45'}]}
  if f2hz <4838.335 and f2hz >4558.945: note = {'notes' : [{ 'octave' :'5', 'note' : 'D', 'string' : '1', 'position' : '46'}]}
  if f2hz <2489.015 and f2hz >7467.045: note = {'notes' : [{ 'octave' :'5', 'note' : 'DS', 'string' : '1', 'position' : '47'}]}
  return note

def filter_silence(data):
  if data[1] > 0:
    return True
  return False

def filter_short_regions(region):
  if len(region) > NUMBER_REGIONS_THRESHOLD:
    return True
  return False

def find_continuous_regions(data):
  result = []
  start_seq = None 
  
  #for i, element in enumerate(data):    
  #  if element[1] > 0:      
  i = 0;
  
  while i < (len(data)):
    current_element_freq = data[i][1]
    
    if current_element_freq > 0:
      new_note_list = []
      while i < len(data) - NUMBER_ZEROS:
	isBreak = [data[j][1] for j in xrange( i, i + NUMBER_ZEROS) ] == [0.0] * NUMBER_ZEROS
	if isBreak:
	  result.append(new_note_list)
	  break;
	else:
	  new_note_list.append( data[i] )
	  i = i + 1
    i = i + 1
  return result
  
def region_to_note(region):
  region_frequency = numpy.median( [freq_to_round(reg_data[1]) for reg_data in region] )
  note = freq_to_note( region_frequency )
  if note is not None:
    if 'notes' in note:
      note['info'] = note['notes'][0]
      del note['notes']
      note['type'] = 'note'
      #note = note[0]
      timestamp = [reg_data[0] for reg_data in region][5]
      note['timeshift'] = timestamp
      return note
  
  
def get_notes_from_file(filename):
  fdata = [map(float,line.split(' ')) for line in open(filename).readlines()]
  #fdata = filter( filter_silence, fdata )
  filtered_freq = []
  for d in fdata:
    filtered_freq.append( (d[0], freq_to_round(d[1])) )
  
  regions = find_continuous_regions(filtered_freq)
  regions = filter( filter_short_regions, regions)  
  for region in regions:
    print len(region)
    print region[:20]
    print "================="
  notes = [ region_to_note(region) for region in regions ]
  notes = [note for note in notes if note is not None]
  return notes
  
if __name__ == "__main__":
  fname = sys.argv[1]
  
  print get_notes_from_file( fname )

  