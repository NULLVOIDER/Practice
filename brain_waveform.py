from __future__ import print_function

from open_bci_v3 import OpenBCIBoard

import threading
import Queue
import atexit

import os
import csv
import datetime
import time

from argparse import ArgumentParser
import curses

samples = []

packet_labels = []

def label_packet(packet):
	global packet_labels
	try:
		plabel = packet_labels.pop()
	except IndexError as e:
		plabel = None
	#print("Imma packet")
	if plabel != None:
		samples.append([plabel, packet.channel_data])
	else:
		samples.append([" - ", packet.channel_data])

def write_packets():
	dtnow = datetime.datetime.now()
	tsvf = os.path.join(dirpath, dtnow.strftime("%F_%H%M%S.tsv"))
	i=0.0
	if len(samples) == 0: return
	print("Writing to", tsvf)
	with open(tsvf, 'w') as f:
		w = csv.writer(f, delimiter='\t')
		w.writerow(["mood", args.c0, args.c1, args.c2, args.c3, args.c4, args.c5, args.c6, args.c7])
		for smpl in samples:
			flattened_row = []
			flattened_row.append(smpl[0])
			flattened_row.append(i*sampletime)
			i+=1.0
			flattened_row.extend(['{:.16f}'.format(ss) for ss in smpl[1]])
			w.writerow(flattened_row)

def curses_ui():
	stdscr = curses.initscr()
	curses.cbreak()
	stdscr.keypad(1)

	stdscr.addstr(0, 10, "Hit 'q' to quit")
	stdscr.addstr(1, 0, "Hit 'a' for angry, 's' for sad, 'f' for fearful, ")
	stdscr.addstr(2, 0, "'d' for distracted, 'c' for calm, 'o' for focused, and 'b' for happy")
	stdscr.refresh()

	key = ''
	while key != ord('q'):
		key = stdscr.getch()
		stdscr.addch(20,25,key)
		stdscr.refresh()
		if key == ord('a'): 
			packet_labels.append("angry")
		elif key == ord('s'): 
			packet_labels.append("sad")
		elif key == ord('f'):
			packet_labels.append("fearful")
		elif key == ord('o'):
			packet_labels.append("focused")
		elif key == ord('d'):
			packet_labels.append("distracted")
		elif key == ord('c'):
			packet_labels.append("calm")
		elif key == ord('b'):
			packet_labels.append("happy")

	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()

aparser = ArgumentParser()
aparser.add_argument('dongle_device')
aparser.add_argument('-c0', type=str, default="Channel 0")
aparser.add_argument('-c1', type=str, default="Channel 1")
aparser.add_argument('-c2', type=str, default="Channel 2")
aparser.add_argument('-c3', type=str, default="Channel 3")
aparser.add_argument('-c4', type=str, default="Channel 4")
aparser.add_argument('-c5', type=str, default="Channel 5")
aparser.add_argument('-c6', type=str, default="Channel 6")
aparser.add_argument('-c7', type=str, default="Channel 7")
args = aparser.parse_args()

board = OpenBCIBoard(port=args.dongle_device)
for c in 'svcd':
	board.ser.write(c)
	time.sleep(0.100)
time.sleep(0.100)

sampletime = 1.0/board.getSampleRate()
dirpath = os.path.dirname(os.path.realpath(__file__))

atexit.register(write_packets)
atexit.register(board.disconnect)
boardthread = threading.Thread(target=board.start_streaming, args=(label_packet, -1))
#board.start_streaming([label_packet], -1)
boardthread.daemon = True
boardthread.start()

curses_ui()
