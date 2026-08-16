class VersionPF:
	number = "3.09"
	date = '16 Aug 26'
	text = 'Esc levels fix no skip'

"""
Copyright Phillip Forrestal 2020-2026 Got sick in 2022, came back home in 2024
Program name: april two
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

::Version
3.08 29 Jul 26 add delay if failure
3.07 25 Jul 26 Skip delay 
3.06 24 Jul 26 Editor
3.05 6 Jul 2026 Color
3.04 29 Jun 2026 1 Jul 26 skip maps which a to hard or easy 
3.03 25 Jun - 28 Jun 2026 options
3.02 27 May 2026 - 24 Jun 26 Show
3.01 - 4 Jan 2026 Name'
3.00 - 9 Dec 2025 Start Edit
2.99a - 18 Dec 25 score delete
2.99 16 Dec 2025 fix score
2.98 9  Dec 2025 new type of score
2.97 22 Nov 2025 new score
2.96 18 Arp 24 switch my ini to configparser  == fail
2.95 4 Apr 2024 score == low is low score
2.94 26 Feb 2024 = score new at top
2.93 26 Feb 2024 longer start time and add score is reset
2.92 1 Feb 2024 keep top 12 level played
2.91 28 Jan 2024 Remove things not use, fix things
2.90 24 Jan 2024 Fixes ? in name
2.89 22 Jan 2024 Fix other window box
if abort key press ^ over  10 sec then stuck use fail display
2.88 21 Jan 2024 New end display and fix the margins
2.87 20 Jan 2024 (won/lost, Sort time) lowest, (wheel new & extra) highest
2.86 19 Jan 2024 board time out (on/off) in menu and ini
2.85 18 Jan 2024 New output. Time Wheels/total wheels did, empty, game fail code
2.84 15 Jan 2024 Continue will by the same level in random. random any time
2.83 14 Jan 2024 add Random flag - continue to the same level == failed
2.82 27 Dec 2023 add level timeout, gameloop
2.81 23 Dec 2023 abort - Restart, quit, continue - change popup
2.80 18 Dec 2023 Aline and center text
2.79 16 Dec 2023 Clean up list , add date & time
2.78 15 Dec 2023 Display list of scores
2.77 14 Dec 2023 Add data ver
2.76 11 Dec 2023 Score last complete 10 part 1 done
2.75 29 Nov 2023 Title changed to April To moving balls
2.75 24 Nov 2023 get key menu to work
2.74 22 Non 2023 Work again
2.73 29 Nov 2023 Found the problem 'is' vs ==
2.72 19 Nov 2023 refresh
sick, better but only one hand

2.71 31 Jan 2021 Check effect in ini off to on fails, Ini save 1/0 as string
2.70 30 Jan 2021 Score: wheel cleared
2.69 29 Jan 2021 Score: create Level complete value
2.68 24 Jan 2021 Score: change time to count up from 0 show tenths
2.67 20 Jan 2021 Save Music & Effect sounds
2.66 18 Jan 2021 Save background sound & fix Ini
2.65 23 Dec 2020 Save Last Level
2.64 24 Nov 2020 Start editor - Remove it - start again
2.63 18 Oct 2020 Add Menu Game backgound music & sound off/on
2.62 17 Oct 2020 Menu_Mouse.py 1.06 Add Music to menu
2.61 14 Oct 2020 Bug: Game exits between levels
2.60 8 Oct 2020 Random max level
2.59 5 Oct 2020 Set level (Have to think about this)
2.58 3 Oct 2020 Endless time
2.57 2 Oct 2020 Fixed wild card marbles in wheel
2.56 1 Oct 2020 cleanup3
2.55 30 Oct 2020 cleanup2
2.54 30 Sep 2020 cleanup1
2.53 30 Sep 2020 mouse_menu 1.01 Add double click to activate 1/2 second
2.52 29 Sep 2020 Remove None in ImageLoad. -2 = colorkey not used, -1 = colorkey at (0,0)
2.51 29 Sep 2020 Remove None, change to (0, 0) if center not used
2.50 28 Sep 2020 Import menu_mouse.py
2.49 18 Sep 2020 Clean up - Menu
2.48 16 Sep 2020 All levels work
2.47 15 Sep 2020 First 3 levels play
2.46 14 Sep 2020 Varibles Name change, work to main menu
2.45 14 Sep 2020 MainMenu init

	Start again

2.41 11 Sep 2020 Sound try 2 -- Stop
2.40 8 Sep 2020 class Music for both works in game
2.39 7 Sep 2020 next class Music
2.38 5 Sep 2020 Put Options in Class
2.37 3 Sep 2020 Center game
2.36 3 Sep 2020 Change Constants to UPPER case
2.35 2 Sep 2020 Runs but not the way I want
2.34 1 Sep 2020 Score
2.33 31 Aug 2020 Change class Popup, remove now in class

2.32 31 Aug 2020 message popup as Class
2.31 28 Aug 2020 plays but not
2.30 28 Aug 2020 introcreen command out
2.29 26 Aug 2020 Clean up menu
2.28 24 Aug 2020 Revert to 2.25 start again
2.25 11 Aug 2020 Menu: Start Game
2.24 31 Jul 2020 Main Menu - My Scroll Text and Ver
2.23 29 Jul 2020 Main Menu or start game
2.22 26 Jul 2020 Main Menu - text - select
2.21 23 Jul 2020 Main Menu - add backgroud
2.20 16 Jul 2020 def Main()

2.12 12 Jul 2020 def Main()  Failed.  Revert to 2.11

Use 2.11 if you want to run the game.
2.11 9 Jul 2020 General - Last version before I start changeing code.
I like to add new code at the end. Program doesn't get to end
2.11 9 Jul 2020 General
2.10 7 Jul 2020 Random level after level order
2.09 7 Jul 2020 Numbers in level done box are float
2.08 5 Jul 2020 Numbers in on bar are float  Score & time left
2.07 4 Jul 2020 Error when wheel is full which same colorh
2.06 4 Jul 2020 Errors are gone, but it doesn't mouse click. My error add int wrong def click(self, pos):
2.05 4 Jul 2020 Next Group (next thing python should do is assign var with type Int A)( Keep all divide an int)
2.04 3 Jul 2020 Start game errors.
2.03 3 Jul 2020 All problems v2 to V3 to menu cleared. the intro.xm will not play. Change background.xm to intro.xm
2.02 2 Jul 2020 Fix 934 Create two_dimensional_lists_arrays (can't believe Python has no Array varible type.)
2.01 25 Jun 2020 Find errors durning debug
2,00 25 Jun 2020 Start

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
Copyright (c) 2020
Program created and copyrighted  by Phillip Forrestal 2020

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Copyright (C) 2003  John-Paul Gignac

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

# Import Modules

import os
import pygame
from pygame.locals import *
from dataclasses import replace

import sys
import time
from datetime import datetime
from datetime import timedelta
import math
import random
import configparser
from menu_mouse import MainMenu

os.environ['SDL_VIDEO_CENTERED'] = '1'


class CONS:  # Data constants
	ScVer = "1.0"
	DaVer = '1.2'  # ini data file


# Game constants
WHEEL_STEPS = 9
FRAMES_PER_SEC = 100
TIMER_WIDTH = 36
TIMER_MARGIN = 4
INFO_HEIGHT = 20

# Volume levels
INTRO_MUSIC_VOLUME = 0.6
INGAME_MUSIC_VOLUME = 0.9
SOUND_EFFECTS_VOLUME = 0.6

# Changing these may affect the playability of levels
DEFAULT_COLORS = '2346'  # Blue, Green, Yellow, Red
DEFAULT_STOPLIGHT = '643'  # Red, Yellow, Green
DEFAULT_LAUNCH_TIMER = 6  # 6 passes
DEFAULT_BOARD_TIMER = 30  # 30 seconds per wheel
MARBLE_SPEED = 2  # Marble speed in pixels/frame (must be 1, 2 or 4)
TRIGGER_TIME = 30  # 30 seconds
REPLICATOR_DELAY = 35  # 35 frames

# Don't change these constants unless you
# redo all the levels
HORIZ_TILES = 8
VERT_TILES = 6

# Don't change these constants unless you
# update the graphics files correspondingly.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARBLE_SIZE: int = 28
TILE_SIZE = 92
WHEEL_MARGIN = 4
STOPLIGHT_MARBLE_SIZE = 28
LIFE_MARBLE_SIZE = 16

# The positions of the holes in the wheels in
# each of the three rotational positions
HOLECENTER_RADIUS = int((TILE_SIZE - MARBLE_SIZE) / 2) - WHEEL_MARGIN
HOLECENTERS = []
for whst in range(WHEEL_STEPS):
	theta = (math.pi * whst / (2 * WHEEL_STEPS))
	c = math.floor(0.5 + math.cos(theta) * HOLECENTER_RADIUS)
	s = math.floor(0.5 + math.sin(theta) * HOLECENTER_RADIUS)
	HOLECENTERS.append((
		(int(TILE_SIZE / 2 + s), int(TILE_SIZE / 2 - c)),
		(int(TILE_SIZE / 2 + c), int(TILE_SIZE / 2 + s)),
		(int(TILE_SIZE / 2 - s), int(TILE_SIZE / 2 + c)),
		(int(TILE_SIZE / 2 - c), int(TILE_SIZE / 2 - s))))

# Direction references
DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))

# More global variables
# BOARD_WIDTH = HORIZ_TILES * TILE_SIZE  not use
# BOARD_HEIGHT = VERT_TILES * TILE_SIZE  used only in TIMER_HEIGHT
LAUNCH_TIMER_POS = (0, INFO_HEIGHT)
BOARD_POS = (TIMER_WIDTH, INFO_HEIGHT + MARBLE_SIZE)
TIMER_HEIGHT = VERT_TILES * TILE_SIZE + MARBLE_SIZE


class BS:
	ex = configparser.ConfigParser()
	circuit = configparser.ConfigParser()
	new = configparser.ConfigParser()
	score = configparser.ConfigParser()
	section1 = ''

	def __init__(self):
		self.type = 0
		self.ex_file = 'ex.txt'
		self.circuitspath = 0
		# path not exist or sys
		while 1:
			if not os.path.exists(self.ex_file):  # check score data file exist
				BS.ex.add_section('sys')
				BS.ex.set('sys', 'version', CONS.ScVer)
				with open(self.ex_file, 'w') as configfile:
					self.ex.write(configfile, False)
			BS.ex.read(self.ex_file)
			a = BS.ex.get('sys', 'version', fallback='')
			if a == CONS.ScVer:
				break
			os.remove(self.ex_file)
			BS.ex = configparser.ConfigParser()

		BS.circuitspath = os.path.join('circuits')
		BS.circuit.read(os.path.join(BS.circuitspath, 'levels'))
		BS.new.read(os.path.join(BS.circuitspath, 'new_levels'))

		self.std_list = BS.circuit.sections()
		list = BS.new.sections()
		self.std_list.extend(list)
		self.std_list.append('-')
		self.std_level = self.ex.getint('sys', 'stdlevel', fallback=0)

		items = self.ex.get('sys', 'ranlist', fallback='-')
		self.ran_list = str.split(items, ',')
		self.ran_level = self.ex.getint('sys', 'ranlevel', fallback=0)

		# score
		os.makedirs("score", exist_ok=True)  # succeeds even if directory exist.
		self.scorefile = os.path.join('score', 'scores.txt')

		while 1:
			if not os.path.exists(self.scorefile):  # check score data file exist
				BS.score.add_section('sys')
				BS.score.set('sys', 'version', CONS.DaVer)
				with open(self.scorefile, 'w') as configfile:
					BS.score.write(configfile, False)
			BS.score.read(self.scorefile)
			a = BS.score.get('sys', 'version', fallback='')
			if a == CONS.DaVer:
				break
			os.remove(self.scorefile)
			BS.score = configparser.ConfigParser()

	def lev(self, lev=0, type1=-1):
		if type1 == -1:
			type1 = self.type
		else:
			self.type = type1
		a = None
		if type1 == 0:
			if self.std_list[self.std_level + lev] == '-':
				self.std_level = 0
			else:
				self.std_level += lev
			self.ex.set('sys', 'stdlevel', str(self.std_level))
			a = self.std_list[self.std_level]

		elif type1 == 1:
			# type =  1
			a = self.ran_level + lev
			bad = False # if level does not exist remove outside loop
			while 1:
				if bad or self.ran_list[a] == '-':
					bad = False
					self.ran_list = self.std_list  # self.circuit.sections()
					self.ran_list.remove('-')
					random.shuffle(self.ran_list)
					self.ran_list.append('-')
					self.ran_level = 0
					a = ",".join(map(str, self.ran_list))
					self.ex.set('sys', 'ranlist', a)
				else:
					self.ran_level += lev

				self.ex.set('sys', 'ranlevel', str(self.ran_level))
				a = self.ran_list[self.ran_level]

				if a in self.std_list:
					break
				else:
					bad = True

		elif type1 == 2:
			ed_list = self.circuit.sections()
			a = ed_list[0]

		return a

	def save(self):
		with open(self.ex_file, 'w') as configfile:
			self.ex.write(configfile, False)

	def save1(self):
		with open(self.scorefile, 'w') as configfile:
			BS.score.write(configfile)

	def read1(self):
		BS.score.read(self.scorefile)


# 24 Apr 24 Score


staf = BS()

def wait_one_sec():
	time.sleep(1)
	pygame.event.get()  # Clear the event queue

def Message(mess, no=0):
	mes = mess
	pop = PopWindow(base.screen)
	if no == 3:
		mes = mes + ' Yes  No/mouse'
	mes = mes + '\n\n'
	pop.popup(mes)
	f = pop.popwait(4)
	pop.popdown()
	return f

class base:
	lkl = 0
	lkb = 0
	lk = 0
	set_launch_timer_ex = 0
	set_board_timer_ex = 0
	atime = 0
	check = False  # editor
	stoplight = False
	ccc = []
	skip = 0
	skipoff = 1
	transfer = None
	edit_act = False
	edit_play = False
	gameloop = 0  # 27Dec23
	gamelooptext = ""  # 27Dec23
	save = 0  # level for continue
	sv = -1
	sort1 = '0'  # base sort
	sortcur = ""  # today1.strftime('%y%j%H%M%S')
	scorecur = ""  # 17Jan24
	numwheels = 0
	# 19Jan24
	board_time_sw = True  # False  # true on false off
	write_highscores = None
	extra_life = None
	intromusic = None
	gamemusic = None
	furelise = None
	background = None
	background2 = None  # use in edit
	sr = 0
	menu_scroll = None
	background_on = None
	sound_on = None
	cbext = None
	music_on = None
	popup_font = None
	die = None
	levelfinish = None
	screenshot = None
	info_font = None
	backdrop = None
	launch_timer_font = None
	Trigger_image = None
	trigger_setup = None
	teleport = None
	replicator = None
	switch = None
	shredder = None
	direct_marble = None
	Director_images = None
	filter_admit = None
	Filter_images = None
	change_color = None
	Painter_images = None
	Buffer_top = None
	Tile_tunnels = None
	Buffer_bottom = None
	wheel_completed = None
	ping = None
	incorrect = None
	wheel_turn = None
	Wheel_images = None
	Wheel_moving_holes = None
	Wheel_blank_images = None
	Tile_plains = None
	marble_release = None
	marble_images = None
	set_level = 0
	level = None
	level_cmp = -1

	# Score 14 Dec 23
	scfilename = None
	screen = None
	# 15Dec23
	total_holes = 0
	empty_holes = 0

	wheelnew = 0
	wheeldid = 0


# Load the fonts for various parts of the game
class Font:
	def __init__(self):
		base.launch_timer_font = pygame.font.SysFont('arial', TIMER_WIDTH - 2 * TIMER_MARGIN)
		base.active_marbles_font = pygame.font.SysFont('arial', MARBLE_SIZE)
		base.popup_font = pygame.font.SysFont('arial', 20)
		base.info_font = pygame.font.SysFont('arial', INFO_HEIGHT)


class Images:
	def __init__(self):
		base.background = ImageLoad('intro2.png', -2, (SCREEN_WIDTH, SCREEN_HEIGHT))
		base.backdrop = ImageLoad('backdrop.jpg', -2, (SCREEN_WIDTH, SCREEN_HEIGHT))

		base.marble_images = []  # Marble.images
		for i in range(9):
			base.marble_images.append(ImageLoad('marble-' + repr(i) + base.cbext, -1, (MARBLE_SIZE, MARBLE_SIZE)))

		base.Tile_tunnels = []  # Tile.tunnels
		base.Tile_plains = []  # Tile.plain_tiles

		for i in range(16):
			tile = ImageLoad('tile.png', (206, 53, 53), (TILE_SIZE, TILE_SIZE))
			path = ImageLoad('path-' + repr(i) + '.png', -1, (TILE_SIZE, TILE_SIZE))
			tile.blit(path, (0, 0))
			base.Tile_plains.append(tile)
			base.Tile_tunnels.append(ImageLoad('tunnel-' + repr(i) + '.png', -1, (TILE_SIZE, TILE_SIZE)))
		#  Wheel.images
		base.Wheel_images = (
			ImageLoad('wheel.png', -1, (TILE_SIZE, TILE_SIZE)),
			ImageLoad('wheel-dark.png', -1, (TILE_SIZE, TILE_SIZE)),
		)
		base.Wheel_blank_images = (
			ImageLoad('blank-wheel.png', -1, (TILE_SIZE, TILE_SIZE)),
			ImageLoad('blank-wheel-dark.png', -1, (TILE_SIZE, TILE_SIZE)),
		)
		base.Wheel_moving_holes = (
			ImageLoad('moving-hole.png', -1, (MARBLE_SIZE, MARBLE_SIZE)),
			ImageLoad('moving-hole-dark.png', -1, (MARBLE_SIZE, MARBLE_SIZE)),
		)

		base.Buffer_bottom = ImageLoad('buffer.png', -1, (TILE_SIZE, TILE_SIZE))
		base.Buffer_top = ImageLoad('buffer-top.png', -1, (TILE_SIZE, TILE_SIZE))

		base.Painter_images = []
		for i in range(8):
			base.Painter_images.append(ImageLoad('painter-' + repr(i) + base.cbext, -1, (TILE_SIZE, TILE_SIZE)))

		base.Filter_images = []
		for i in range(8):
			base.Filter_images.append(ImageLoad('filter-' + repr(i) + base.cbext, -1, (TILE_SIZE, TILE_SIZE)))

		base.Director_images = (
			ImageLoad('director-0.png', -1, (TILE_SIZE, TILE_SIZE)),
			ImageLoad('director-1.png', -1, (TILE_SIZE, TILE_SIZE)),
			ImageLoad('director-2.png', -1, (TILE_SIZE, TILE_SIZE)),
			ImageLoad('director-3.png', -1, (TILE_SIZE, TILE_SIZE)),
		)

		Shredder.image = ImageLoad('shredder.png', -1, (TILE_SIZE, TILE_SIZE))

		Switch.images = []
		for i in range(4):
			Switch.images.append([])
			for j in range(4):
				if i == j:
					Switch.images[i].append(None)
				else:
					Switch.images[i].append(
						ImageLoad('switch-' + repr(i) + repr(j) + '.png', -1, (TILE_SIZE, TILE_SIZE)))

		Replicator.image = ImageLoad('replicator.png', -1, (TILE_SIZE, TILE_SIZE))

		Teleporter.image_h = ImageLoad('teleporter-h.png', -1, (TILE_SIZE, TILE_SIZE))
		Teleporter.image_v = ImageLoad('teleporter-v.png', -1, (TILE_SIZE, TILE_SIZE))

		base.Trigger_image = ImageLoad('trigger.png', -1, (TILE_SIZE, TILE_SIZE))

		Stoplight.image = ImageLoad('stoplight.png', -1, (TILE_SIZE, TILE_SIZE))
		Stoplight.smallmarbles = []
		for im in base.marble_images:
			Stoplight.smallmarbles.append(pygame.transform.scale(im, (STOPLIGHT_MARBLE_SIZE, STOPLIGHT_MARBLE_SIZE)))


# Classes for our game objects


class Marble:
	def __init__(self, color1, center, direction):
		self.color = color1
		self.rect = pygame.Rect((0, 0, MARBLE_SIZE, MARBLE_SIZE))
		self.rect.center = center
		self.direction = direction

	#  self.images

	def update(self, board):
		self.rect.move_ip(
			MARBLE_SPEED * DIRS[self.direction][0],
			MARBLE_SPEED * DIRS[self.direction][1])

		board.affect_marble(self)

	def undraw(self, screen, background):
		screen.set_clip(self.rect)
		screen.blit(background, (0, 0))
		screen.set_clip()

	def draw(self, screen):
		screen.blit(base.marble_images[self.color], self.rect.topleft)


class Tile:
	def __init__(self, paths=0, center=(0, 0)):
		self.paths = paths
		self.center = center
		self.rect = pygame.Rect((0, 0, TILE_SIZE, TILE_SIZE))
		self.rect.center = center
		self.drawn = 0

	def draw_back(self, surface):
		if self.drawn:
			return 0
		surface.blit(base.Tile_plains[self.paths], self.rect.topleft)
		self.drawn = 1
		return 1

	def update(self, board):
		pass

	def draw_fore(self, surface):
		return 0

	def click(self, board, posx, posy, tile_x, tile_y):
		pass

	def affect_marble(self, board, marble, rpos):
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			if self.paths & (1 << marble.direction):
				return

			# Figure out the new direction
			t = self.paths - (1 << (marble.direction ^ 2))
			if t == 1:
				marble.direction = 0
			elif t == 2:
				marble.direction = 1
			elif t == 4:
				marble.direction = 2
			elif t == 8:
				marble.direction = 3
			else:
				marble.direction = marble.direction ^ 2


class Wheel(Tile):
	def __init__(self, paths, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer
		self.spinpos = 0
		self.completed = 0
		self.marbles = [-3, -3, -3, -3]

	def draw_back(self, surface):
		if self.drawn:
			return 0

		Tile.draw_back(self, surface)

		if self.spinpos:
			surface.blit(base.Wheel_blank_images[self.completed], self.rect.topleft)
			for i in range(4):
				holecenter = HOLECENTERS[self.spinpos][i]
				surface.blit(base.Wheel_moving_holes[self.completed], (
					holecenter[0] - int(MARBLE_SIZE / 2) + self.rect.left,
					holecenter[1] - int(MARBLE_SIZE / 2) + self.rect.top))
		else:
			surface.blit(base.Wheel_images[self.completed], self.rect.topleft)

		for i in range(4):
			if self.marbles[i] >= 0:
				holecenter = HOLECENTERS[self.spinpos][i]
				surface.blit(base.marble_images[self.marbles[i]], (
					holecenter[0] - int(MARBLE_SIZE / 2) + self.rect.left,
					holecenter[1] - int(MARBLE_SIZE / 2) + self.rect.top))

		return 1

	def update(self, board):
		if self.spinpos > 0:
			self.spinpos -= 1
			self.drawn = 0

	def click(self, board, posx, posy, tile_x, tile_y):
		# Ignore all clicks while rotating
		if self.spinpos:
			return

		b1, b2, b3 = pygame.mouse.get_pressed()
		if b3:
			# First, make sure that no marbles are currently entering
			for i in self.marbles:
				if i == -1 or i == -2:
					return

			# Start the wheel spinning
			self.spinpos = WHEEL_STEPS - 1
			play_sound(base.wheel_turn)

			# Reposition the marbles
			t = self.marbles[0]
			self.marbles[0] = self.marbles[1]
			self.marbles[1] = self.marbles[2]
			self.marbles[2] = self.marbles[3]
			self.marbles[3] = t

			self.drawn = 0

		elif b1:
			# Determine which hole is being clicked
			for i in range(4):
				# If there is no marble here, skip it
				if self.marbles[i] < 0:
					continue

				holecenter = HOLECENTERS[0][i]
				rect = pygame.Rect(0, 0, MARBLE_SIZE, MARBLE_SIZE)
				rect.center = holecenter
				if rect.collidepoint(posx, posy):

					# Determine the neighboring tile
					neighbor = board.tiles[(tile_y + DIRS[i][1]) % VERT_TILES][(tile_x + DIRS[i][0]) % HORIZ_TILES]

					if (
							# Disallow marbles to go off the top of the board
							(tile_y == 0 and i == 0) or

							# If there is no way out here, skip it
							((self.paths & (1 << i)) == 0) or

							# If the neighbor is a wheel that is either turning
							# or has a marble already in the hole, disallow
							# the ejection
							(isinstance(neighbor, Wheel) and (neighbor.spinpos or neighbor.marbles[i ^ 2] != -3))
					):
						play_sound(base.incorrect)
					else:
						# If the neighbor is a wheel, apply a special lock
						if isinstance(neighbor, Wheel):
							neighbor.marbles[i ^ 2] = -2
						elif len(board.marbles) >= board.live_marbles_limit:
							# Impose the live marbles limit
							play_sound(base.incorrect)
							break

						# Eject the marble
						board.marbles.append(
							Marble(self.marbles[i], (holecenter[0] + self.rect.left, holecenter[1] + self.rect.top), i))
						self.marbles[i] = -3
						play_sound(base.marble_release)
						self.drawn = 0
					break

	def affect_marble(self, board, marble, rpos):
		# Watch for marbles entering
		if rpos[0] + MARBLE_SIZE / 2 == WHEEL_MARGIN or rpos[0] - MARBLE_SIZE / 2 == TILE_SIZE - WHEEL_MARGIN or rpos[
			1] + MARBLE_SIZE / 2 == WHEEL_MARGIN or rpos[1] - MARBLE_SIZE / 2 == TILE_SIZE - WHEEL_MARGIN:
			if self.spinpos or self.marbles[marble.direction ^ 2] >= -1:
				# Reject the marble
				marble.direction = marble.direction ^ 2
				play_sound(base.ping)
			else:
				self.marbles[marble.direction ^ 2] = -1

		for holecenter in HOLECENTERS[0]:
			if rpos == holecenter:
				# Accept the marble
				board.marbles.remove(marble)
				self.marbles[marble.direction ^ 2] = marble.color

				self.drawn = 0

				break

	def complete(self, board):
		# Complete the wheel
		for i in range(4):
			self.marbles[i] = -3

		if self.completed:
			base.wheeldid += 1

		else:
			base.wheelnew += 1

		self.completed = 1
		play_sound(base.wheel_completed)
		self.drawn = 0

	def maybe_complete(self, board):
		if self.spinpos > 0:
			return 0

		# Is there a trigger?
		if (board.trigger is not None) and (board.trigger.marbles is not None):
			# Compare against the trigger
			for i in range(4):
				if self.marbles[i] != board.trigger.marbles[i] and self.marbles[i] != 8:
					return 0
			self.complete(board)
			board.trigger.complete(board)
			return 1

		# Do we have four the same color?
		first_color = 8  # wildcard color

		for colorinhole in self.marbles:  # 8 = Wildcard

			if colorinhole < 0:  # empty
				return 0
			if first_color == 8:
				first_color = colorinhole  # fill with first color found
			elif colorinhole == 8:  # if wild card then fill with first color
				colorinhole = first_color
			elif colorinhole != first_color:  # this hole not the same as first hole
				return 0

		# Is there a stoplight?
		if (board.stoplight is not None) and (board.stoplight.current < 3):
			# Compare against the stoplight
			if first_color != 99 and first_color != board.stoplight.marbles[board.stoplight.current]:
				return 0
			else:
				board.stoplight.complete(board)

		self.complete(board)
		return 1


class Buffer(Tile):
	def __init__(self, paths, in_color=-1):
		Tile.__init__(self, paths)  # Call base class intializer
		self.marble = in_color
		self.entering = None

	def draw_back(self, surface):
		if self.drawn:
			return 0

		Tile.draw_back(self, surface)

		hole_color = self.marble
		if hole_color >= 0:
			holecenter = self.rect.center
			surface.blit(base.marble_images[hole_color],
			             (holecenter[0] - int(MARBLE_SIZE / 2), holecenter[1] - int(MARBLE_SIZE / 2)))
		else:
			surface.blit(base.Buffer_bottom, self.rect.topleft)

		return 1

	def draw_fore(self, surface):
		surface.blit(base.Tile_tunnels[self.paths], self.rect.topleft)
		surface.blit(base.Buffer_top, self.rect.topleft)
		return 0

	def affect_marble(self, board, marble, rpos):
		# Watch for marbles entering
		if (rpos[0] + MARBLE_SIZE == TILE_SIZE / 2 and marble.direction == 1) or (
				rpos[0] - MARBLE_SIZE == TILE_SIZE / 2 and marble.direction == 3) or \
				(rpos[1] + MARBLE_SIZE == TILE_SIZE / 2 and marble.direction == 2) or (
				rpos[1] - MARBLE_SIZE == TILE_SIZE / 2 and marble.direction == 0):

			if self.entering is not None:
				# Bump the marble that is currently entering
				newmarble = self.entering
				newmarble.rect.center = self.rect.center
				newmarble.direction = marble.direction

				play_sound(base.ping)

				# Let the base class affect the marble
				Tile.affect_marble(self, board, newmarble, (TILE_SIZE / 2, TILE_SIZE / 2))
			elif self.marble >= 0:
				# Bump the marble that is currently caught
				newmarble = Marble(self.marble, self.rect.center, marble.direction)

				board.marbles.append(newmarble)

				play_sound(base.ping)

				# Let the base class affect the marble
				Tile.affect_marble(self, board, newmarble, (TILE_SIZE / 2, TILE_SIZE / 2))

				self.marble = -1
				self.drawn = 0

			# Remember which marble is on its way in
			self.entering = marble

		elif rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			# Catch this marble
			self.marble = marble.color
			board.marbles.remove(marble)
			self.entering = None
			self.drawn = 0


class Painter(Tile):
	def __init__(self, paths, in_color, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer
		self.color = in_color

	def draw_fore(self, surface):
		surface.blit(base.Tile_tunnels[self.paths], self.rect.topleft)
		surface.blit(base.Painter_images[self.color], self.rect.topleft)
		return 0

	def affect_marble(self, board, marble, rpos):
		Tile.affect_marble(self, board, marble, rpos)
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			if marble.color != self.color:
				# Change the color
				marble.color = self.color
				play_sound(base.change_color)


class Filter(Tile):
	def __init__(self, paths, in_color, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer
		self.color = in_color

	def draw_fore(self, surface):
		surface.blit(base.Tile_tunnels[self.paths], self.rect.topleft)
		surface.blit(base.Filter_images[self.color], self.rect.topleft)
		return 0

	def affect_marble(self, board, marble, rpos):
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			# If the color is wrong, bounce the marble
			if marble.color != self.color and marble.color != 8:
				marble.direction = marble.direction ^ 2
				play_sound(base.ping)
			else:
				Tile.affect_marble(self, board, marble, rpos)
				play_sound(base.filter_admit)


class Director(Tile):
	def __init__(self, paths, direction, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer
		self.direction = direction

	def draw_fore(self, surface):
		surface.blit(base.Tile_tunnels[self.paths], self.rect.topleft)
		surface.blit(base.Director_images[self.direction], self.rect.topleft)
		return 0

	def affect_marble(self, board, marble, rpos):
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			marble.direction = self.direction
			play_sound(base.direct_marble)


class Shredder(Tile):
	image = None

	def __init__(self, paths, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer

	def draw_fore(self, surface):
		surface.blit(base.Tile_tunnels[self.paths], self.rect.topleft)
		surface.blit(Shredder.image, self.rect.topleft)
		return 0

	def affect_marble(self, board, marble, rpos):
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			board.marbles.remove(marble)
			play_sound(base.shredder)


class Switch(Tile):
	def __init__(self, paths, dir1, dir2, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer
		self.curdir = dir1
		self.otherdir = dir2
		self.switched = 0

	def switch(self):
		t = self.curdir
		self.curdir = self.otherdir
		self.otherdir = t
		self.switched = 1
		play_sound(base.switch)

	def draw_fore(self, surface):
		bb = pygame.Surface.copy(base.Tile_tunnels[self.paths])
		if base.edit_act:
			aa = str(self.otherdir)
			if self.otherdir == 2:
				aa = ' v '
			elif self.otherdir == 3:
				aa = ' < '
			elif self.otherdir == 0:
				aa = ' ^ '
			elif self.otherdir == 1:
				aa = ' > '
			text = base.info_font.render(aa, True, pygame.Color(
				'black'), pygame.Color('green'))
			textRect = text.get_rect()
			bb.blit(text, textRect)

		surface.blit(bb, self.rect.topleft)
		surface.blit(self.images[self.curdir][self.otherdir], self.rect)
		rc = self.switched
		self.switched = 0
		return rc

	def affect_marble(self, board, marble, rpos):
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			marble.direction = self.curdir
			self.switch()


class Replicator(Tile):
	def __init__(self, paths, count, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer
		self.count = count
		self.pending = []

	def draw_fore(self, surface):
		surface.blit(base.Tile_tunnels[self.paths], self.rect.topleft)
		aa = pygame.Surface.copy(self.image)
		if base.edit_act:
			text = base.info_font.render(' ' + str(self.count) + ' ', True, pygame.Color(
				'white'), pygame.Color('blue'))
			textRect = text.get_rect()
			aa.blit(text, textRect)

		surface.blit(aa, self.rect.topleft)
		return 0

	def update(self, board):
		for i in self.pending[:]:
			i[3] -= 1
			if i[3] == 0:
				i[3] = REPLICATOR_DELAY

				# Make sure that the active marble limit isn't exceeded
				if len(board.marbles) >= board.live_marbles_limit:
					# Clear the pending list
					self.pending = []
					return

				# Add the new marble
				board.marbles.append(Marble(i[0], self.rect.center, i[1]))
				play_sound(base.replicator)

				i[2] -= 1
				if i[2] <= 0:
					self.pending.remove(i)

	def affect_marble(self, board, marble, rpos):
		Tile.affect_marble(self, board, marble, rpos)
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			# Add the marble to the pending list
			self.pending.append([marble.color, marble.direction, self.count - 1, REPLICATOR_DELAY])
			play_sound(base.replicator)


class Teleporter(Tile):
	def __init__(self, paths, let, other=None, center=(0, 0)):
		Tile.__init__(self, paths, center)  # Call base class intializer
		self.let = ' ' + let + ' '
		if paths & 5:
			self.image = self.image_v
		else:
			self.image = self.image_h

		self.other = None
		if other is not None:
			self.connect(other)

	def draw_fore(self, surface):
		aa = pygame.Surface.copy(base.Tile_tunnels[self.paths])
		if base.edit_act:
			text = base.info_font.render(self.let, True, pygame.Color(
				'white'), pygame.Color('black'))
			textRect = text.get_rect()
			aa.blit(text, textRect)
		surface.blit(aa, self.rect)
		aa = 0
		surface.blit(self.image, self.rect.topleft)
		return 0

	def connect(self, other):  # connect the OTHER transpot site
		self.other = other
		other.other = self

	def affect_marble(self, board, marble, rpos):
		if rpos == (TILE_SIZE / 2, TILE_SIZE / 2):
			if not self.other is None:
				marble.rect.center = self.other.rect.center
			play_sound(base.teleport)


class Trigger(Tile):
	def __init__(self, colors, center=(0, 0)):
		Tile.__init__(self, 0, center)  # Call base class intializer
		self.marbles = None
		self._setup(colors)
		self.countdown = 0

	def _setup(self, colors):
		self.countdown = 0
		self.marbles = [
			random.choice(colors),
			random.choice(colors),
			random.choice(colors),
			random.choice(colors),
		]
		self.drawn = 0

	def update(self, board):
		if self.countdown > 0:
			self.countdown -= 1
			if self.countdown == 0:
				self._setup(board.colors)
				play_sound(base.trigger_setup)

	def draw_back(self, surface):
		if self.drawn:
			return 0
		Tile.draw_back(self, surface)
		surface.blit(base.Trigger_image, self.rect.topleft)
		if self.marbles is not None:
			for i in range(4):
				surface.blit(base.marble_images[self.marbles[i]],
				             (HOLECENTERS[0][i][0] + int(self.rect.left - MARBLE_SIZE / 2),
				              HOLECENTERS[0][i][1] + int(self.rect.top - MARBLE_SIZE / 2)))
		return 1

	def complete(self, board):
		self.marbles = None
		self.countdown = TRIGGER_TIME * FRAMES_PER_SEC
		self.drawn = 0


class Stoplight(Tile):
	def __init__(self, colors, center=(0, 0)):
		Tile.__init__(self, 0, center)  # Call base class intializer
		# self.smallmarbles = None
		# self.image = None
		base.stoplight = True  # use by Editor
		self.marbles = list(colors)
		self.current = 0

	def draw_back(self, surface):
		if self.drawn:
			return 0
		Tile.draw_back(self, surface)
		surface.blit(self.image, self.rect.topleft)
		for i in range(self.current, 3):
			surface.blit(self.smallmarbles[self.marbles[i]], (self.rect.centerx - 14, self.rect.top + 3 + (29 * i)))
		return 1

	def complete(self, board):
		for i in range(3):
			if self.marbles[i] >= 0:
				self.marbles[i] = -1
				break
		self.current += 1
		self.drawn = 0


class Board:
	def __init__(self, game, pos):
		"""
		param game:
		param pos:
		"""
		self.life_marble = ImageLoad('life-marble.png', -1, (LIFE_MARBLE_SIZE, LIFE_MARBLE_SIZE))
		self.launcher_background = ImageLoad('launcher.png', -2, (HORIZ_TILES * TILE_SIZE, MARBLE_SIZE))
		self.launcher_v = ImageLoad('launcher-v.png', -2, (MARBLE_SIZE, VERT_TILES * TILE_SIZE + MARBLE_SIZE))
		self.launcher_corner = ImageLoad('launcher-corner.png', (255, 0, 0), (int((TILE_SIZE - MARBLE_SIZE)
		                                                                          / 2 + MARBLE_SIZE), MARBLE_SIZE))
		self.launcher_entrance = ImageLoad('entrance.png', -1, (TILE_SIZE, MARBLE_SIZE))
		self.game = game
		self.launch_timer_height = None
		self.pos = pos
		self.marbles = []
		self.screen = game.screen
		self.trigger = None
		self.stoplight = None
		self.launch_queue = []
		self.board_complete = 0
		self.paused = 0
		self.name = "Unnamed"
		self.live_marbles_limit = 10
		self.launch_timeout = -1
		self.board_timeout = -1
		self.colors = DEFAULT_COLORS
		self.launched = 1
		self.pop = PopWindow(self.screen)
		self.wheelnew = 0
		self.wheeldid = 0
		base.wheelnew = 0
		base.wheeldid = 0

		self.set_launch_timer(DEFAULT_LAUNCH_TIMER)
		# self.set_board_timer(DEFAULT_BOARD_TIMER)

		# Create the board array
		self.tiles = []
		self.tiles = [[0] * HORIZ_TILES for i in range(VERT_TILES)]  # Added 2 Jul 2020

		base.level = staf.lev(0, game.type)
		if base.level != base.level_cmp:  #check if level change
			base.level_cmp = base.level
			set_launch_timer_ex = 0
			set_board_timer_ex = 0

		if not BS.score.has_section(base.level):
			BS.score.add_section(base.level)
			aa = ['99999', '1', '99999', '0']
			for i in range(6):
				BS.score.set(base.level, 'ti' + repr(i), ','.join(aa))
				BS.score.set(base.level, 'sc' + repr(i), ','.join(aa))

		self._load(base.level)
		if base.check:  # Setuo game level check for tranfer
			return
		# Create The Background
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.background.fill((200, 200, 200))  # Color of Info Bar

		# Create the launch timer text object
		self.run_time = 0
		self.launch_timer_text = base.launch_timer_font.render(repr(self.launch_timer), 1, (255, 255, 255))
		self.launch_timer_text_rect = self.launch_timer_text.get_rect()
		self.launch_timer_text_rect.centerx = int(LAUNCH_TIMER_POS[0] + TIMER_WIDTH / 2 + 1)
		self.launch_timer_text_rect.bottom = LAUNCH_TIMER_POS[1] + TIMER_HEIGHT - TIMER_MARGIN

		# Fill up the launch queue
		for i in range(int(VERT_TILES * TILE_SIZE / MARBLE_SIZE + 2)):
			self.launch_queue.append(random.choice(self.colors))

		# Draw the backdrop
		# backdrop = load_image('backdrop.jpg', -2, (HORIZ_TILES * TILE_SIZE, VERT_TILES * TILE_SIZE))
		self.background.blit(base.backdrop, BOARD_POS)

		# Draw the launcher
		self.background.blit(self.launcher_background, (BOARD_POS[0], BOARD_POS[1] - MARBLE_SIZE))
		self.background.blit(self.launcher_v, (BOARD_POS[0] + HORIZ_TILES * TILE_SIZE, BOARD_POS[1]))
		for i in range(HORIZ_TILES):
			if self.tiles[0][i].paths & 1:
				self.background.blit(self.launcher_entrance, (BOARD_POS[0] + TILE_SIZE * i, BOARD_POS[1] - MARBLE_SIZE))
		self.background.blit(self.launcher_corner, (
			int(BOARD_POS[0] + HORIZ_TILES * TILE_SIZE - (TILE_SIZE - MARBLE_SIZE) / 2), BOARD_POS[1] - MARBLE_SIZE))

		# Draw the board name
		board_name = self.name + ' - ' + base.scfilename
		text = base.info_font.render(board_name, 1, (0, 0, 0))
		rect = text.get_rect()
		rect.left = 8
		self.background.blit(text, rect)

		# Figure out the score location
		text = "Score: 00000000"
		self.score_pos = SCREEN_WIDTH - 8 - base.info_font.render(text, 1, (0, 0, 0)).get_rect().width

		# Figure out the board timer location
		text = "-0:00:00"

		self.board_timer_pos = self.score_pos - 16 - base.info_font.render(text, 1, (0, 0, 0)).get_rect().width

		# Initialize the screen
		self.screen.blit(self.background, (0, 0))

	def draw_back(self, dirty_rects):
		# Draw the launch timer
		if self.launch_timer_height is None:
			height = TIMER_HEIGHT
			rect = (LAUNCH_TIMER_POS[0], LAUNCH_TIMER_POS[1], TIMER_WIDTH, TIMER_HEIGHT)
			self.screen.fill((0, 0, 0), rect)
			self.screen.fill((0, 40, 255),
			                 (LAUNCH_TIMER_POS[0] + TIMER_MARGIN, LAUNCH_TIMER_POS[1] + TIMER_HEIGHT - height,
			                  TIMER_WIDTH - TIMER_MARGIN * 2, height))
			dirty_rects.append(rect)
		else:
			height = int(TIMER_HEIGHT * self.launch_timeout / self.launch_timeout_start)
			if height < self.launch_timer_height:
				rect = (
					LAUNCH_TIMER_POS[0] + TIMER_MARGIN, LAUNCH_TIMER_POS[1] + TIMER_HEIGHT - self.launch_timer_height,
					TIMER_WIDTH - 2 * TIMER_MARGIN, self.launch_timer_height - height)
				self.screen.fill((0, 0, 0), rect)
				dirty_rects.append(rect)
		self.launch_timer_height = height
		self.screen.blit(self.launch_timer_text, self.launch_timer_text_rect)
		dirty_rects.append(self.launch_timer_text_rect)

		# Clear the info bar
		rect = (0, 0, SCREEN_WIDTH, INFO_HEIGHT)
		self.screen.set_clip(rect)
		self.screen.blit(self.background, (0, 0))
		self.screen.set_clip()
		dirty_rects.append(rect)

		# Draw the board timer
		#  ~~~ time

		temp = int(((self.board_timeout * 1) + FRAMES_PER_SEC - 1) / FRAMES_PER_SEC)
		text = convert1(temp)
		text = base.info_font.render(text, 1, (0, 0, 0))
		rect = text.get_rect()
		rect.left = self.board_timer_pos
		self.screen.blit(text, rect)

		temp = int(base.gameloop * 1 + FRAMES_PER_SEC - 1) / FRAMES_PER_SEC
		base.gamelooptext = temp

		# Draw the lives counter
		# right_edge = self.board_timer_pos - 32
		# for i in range(int(self.game.lives - 1)):
		#	rect = self.life_marble.get_rect()
		#	rect.centery = int(INFO_HEIGHT / 2)
		#	rect.right = right_edge
		#	self.screen.blit(self.life_marble, rect)
		#	right_edge -= rect.width + 4

		# Draw the live marbles
		num_marbles = len(self.marbles)
		if num_marbles > self.live_marbles_limit:
			num_marbles = self.live_marbles_limit
		text = repr(num_marbles) + "/" + repr(self.live_marbles_limit)
		text = base.info_font.render(text, 1, (40, 40, 40))
		rect = text.get_rect()
		rect.left = self.pos[0] + 8
		rect.centery = int(self.pos[1] - MARBLE_SIZE / 2)
		rect.width += 100
		self.screen.set_clip(rect)
		self.screen.blit(self.background, (0, 0))
		self.screen.set_clip()
		self.screen.blit(text, rect)

		dirty_rects.append(rect)

		for row in self.tiles:
			for tile in row:
				if tile.draw_back(self.background):
					self.screen.set_clip(tile.rect)
					self.screen.blit(self.background, (0, 0))
					self.screen.set_clip()
					dirty_rects.append(tile.rect)

		if self.launched:
			for i in range(len(self.launch_queue)):
				self.background.blit(base.marble_images[self.launch_queue[i]],
				                     (self.pos[0] + HORIZ_TILES * TILE_SIZE,
				                      self.pos[1] + i * MARBLE_SIZE - MARBLE_SIZE))
			rect = (self.pos[0] + HORIZ_TILES * TILE_SIZE,
			        self.pos[1] - MARBLE_SIZE, MARBLE_SIZE,
			        MARBLE_SIZE + TILE_SIZE * VERT_TILES)
			self.screen.set_clip(rect)
			self.screen.blit(self.background, (0, 0))
			self.screen.set_clip()
			dirty_rects.append(rect)
			self.launched = 0

	# Python Program to Convert seconds
	# into hours, minutes and seconds

	def draw_fore(self, dirty_rects):
		for row in self.tiles:
			for tile in row:
				if tile.draw_fore(self.screen):
					dirty_rects.append(tile.rect)

	def update(self):
		# Create the list of dirty rectangles
		dirty_rects = []

		# Erase the marbles
		for marble in self.marbles:
			marble.undraw(self.screen, self.background)
			dirty_rects.append(list(marble.rect))

		# Animate the marbles
		for marble in self.marbles[:]:
			marble.update(self)

		# Animate the tiles
		for row in self.tiles:
			for tile in row:
				tile.update(self)
				if tile.drawn == 0:
					dirty_rects.append(tile.rect)

		# Complete any wheels, if appropriate
		try_again = 1
		while try_again:
			try_again = 0
			for row in self.tiles:
				for tile in row:
					if isinstance(tile, Wheel):
						try_again |= tile.maybe_complete(self)

		# Check if the board is complete
		self.board_complete = 1
		for row in self.tiles:
			if self.board_complete == 0:
				break
			for tile in row:
				if isinstance(tile, Wheel):
					if tile.completed == 0:
						self.board_complete = 0
						break

		# Decrement the launch timer
		if self.launch_timeout > 0:
			self.launch_timeout -= 1
			if self.launch_timeout == 0:
				self.board_complete = -1

		# inc time
		self.run_time += 1

		# Decrement the board timer
		# if self.board_timeout > 0:  keep board time out running
		self.board_timeout -= 1
		if base.board_time_sw:
			if self.board_timeout == 0:
				self.board_complete = -2

		# Draw the background
		self.draw_back(dirty_rects)

		# Draw all the marbles
		for marble in self.marbles:
			marble.draw(self.screen)
			dirty_rects.append(marble.rect)

		# Draw the foreground
		self.draw_fore(dirty_rects)

		# Flip the display
		pygame.display.update(dirty_rects)
		pass


	def count_holes(self):
		time.sleep(1)
		base.total_holes = 0
		base.empty_holes = 0
		for row in self.tiles:
			for tile in row:
				if isinstance(tile, Wheel):
					base.total_holes += 4
					if tile.completed == 1:
						for i in tile.marbles:
							if i < 0:
								base.empty_holes += 1

	# a = base.total_holes
	# a = base.empty_holes
	# = 1

	def set_tile(self, x, y, tile):
		self.tiles[y][x] = tile
		tile.rect.left = self.pos[0] + TILE_SIZE * x
		tile.rect.top = self.pos[1] + TILE_SIZE * y

		tile.x = x
		tile.y = y

		# If it's a trigger, keep track of it
		if isinstance(tile, Trigger):
			self.trigger = tile

		# If it's a stoplight, keep track of it
		if isinstance(tile, Stoplight):
			self.stoplight = tile

	def set_launch_timer(self, passes):
		self.launch_timer = passes
		self.launch_timeout_start = (MARBLE_SIZE + (HORIZ_TILES * TILE_SIZE - MARBLE_SIZE) * passes) / MARBLE_SPEED
		self.launch_timer_height = None


	def launch_marble(self):
		self.launch_queue.append(random.choice(self.colors))
		self.marbles.insert(0, Marble(self.launch_queue[0],
		                              (int(self.pos[0] + TILE_SIZE * HORIZ_TILES + MARBLE_SIZE / 2),
		                               int(self.pos[1] - MARBLE_SIZE / 2)), 3))
		del self.launch_queue[0]
		self.launched = 1

		self.launch_timeout = self.launch_timeout_start
		self.launch_timer_height = None

	def affect_marble(self, marble):
		mrc = marble.rect.center
		cx = mrc[0] - self.pos[0]
		cy = mrc[1] - self.pos[1]

		# Bounce marbles off of the top
		if cy == MARBLE_SIZE / 2:
			marble.direction = 2
			return

		if cy < 0:
			if cx == MARBLE_SIZE / 2:
				marble.direction = 1
				return
			if cx == TILE_SIZE * HORIZ_TILES - MARBLE_SIZE / 2 and marble.direction == 1:
				marble.direction = 3
				return

			# The special case of new marbles at the top
			effective_cx = cx
			effective_cy = cy + MARBLE_SIZE
		else:
			effective_cx = int(cx + MARBLE_SIZE / 2 * DIRS[marble.direction][0])
			effective_cy = int(cy + MARBLE_SIZE / 2 * DIRS[marble.direction][1])

		tile_x = int(effective_cx / TILE_SIZE)
		tile_y = int(effective_cy / TILE_SIZE)
		tile_xr = cx - tile_x * TILE_SIZE
		tile_yr = cy - tile_y * TILE_SIZE

		if tile_x >= HORIZ_TILES:
			return

		tile = self.tiles[tile_y][tile_x]

		if cy < 0 and marble.direction != 2:
			# The special case of new marbles at the top
			if tile_xr == TILE_SIZE / 2 and (tile.paths & 1):
				if isinstance(tile, Wheel):
					if tile.spinpos > 0 or tile.marbles[0] != -3:
						return
					tile.marbles[0] = -2
					marble.direction = 2
					self.launch_marble()
				elif len(self.marbles) < self.live_marbles_limit:
					marble.direction = 2
					self.launch_marble()
		else:
			tile.affect_marble(self, marble, (tile_xr, tile_yr))

	def click(self, pos):
		# Determine which tile the pointer is in
		tile_x = int((pos[0] - self.pos[0]) / TILE_SIZE)
		tile_y = int((pos[1] - self.pos[1]) / TILE_SIZE)
		tile_xr = pos[0] - self.pos[0] - tile_x * TILE_SIZE
		tile_yr = pos[1] - self.pos[1] - tile_y * TILE_SIZE
		if 0 <= tile_x < HORIZ_TILES and 0 <= tile_y < VERT_TILES:
			tile = self.tiles[tile_y][tile_x]
			tile.click(self, tile_xr, tile_yr, tile_x, tile_y)

	def _load(self, section1):  # (self, circuit, level):
		# which souce is used
		lv = 0
		if BS.circuit.has_section(section1):
			lv = BS.circuit
		elif BS.new.has_section(section1):
			lv = BS.new
		if lv == 0:
			return False

		# circuit.get(section1, )
		BS.section1 = section1  # editor use in Game
		teleporters = []
		teleporter_names = []
		stoplight = DEFAULT_STOPLIGHT

		base.numwheels = 0
		# boardtimer = -1
		self.name = lv.get(section1, 'name')
		base.scfilename = lv.get(section1, 'score', fallback=section1)
		self.live_marbles_limit = lv.getint(section1, 'maxmarbles', fallback=10)
		set_launch_timer1 = (lv.getint(section1, 'launchtimer', fallback=DEFAULT_LAUNCH_TIMER))
		base.set_launch_timer_ex = base.set_launch_timer_ex + (base.lk * base.lkl)
		base.lkl = 0
		set_launch_timer1 += base.set_launch_timer_ex
		#self.launch_timer = self.set_launch_timer1
		self.set_launch_timer(set_launch_timer1)
		aaa = set_launch_timer1

		boardtimer = lv.getint(section1, 'boardtimer', fallback=-1)
		a = lv.get(section1, 'colors', fallback=DEFAULT_COLORS)
		self.colors = []
		for i in a:  # one char at time
			if '0' <= i <= '7':
				self.colors.append(int(i))
				self.colors.append(int(i))
				self.colors.append(int(i))
			elif i == '8':
				# Crazy marbles are one-third as common
				self.colors.append(8)
		a = lv.get(section1, 'stoplight', fallback=DEFAULT_STOPLIGHT)
		stoplight = []
		for i in a:
			if '0' <= i <= '7':
				stoplight.append(int(i))

		for x in range(1, 7):
			line = lv.get(section1, 'g' + str(x))
			j = x - 1
			for i in range(HORIZ_TILES):

				types = line[i * 4 + 1]
				paths = line[i * 4 + 2]
				if paths == ' ':
					pathsint = 0
				elif paths >= 'a':
					pathsint = ord(paths) - ord('a') + 10
				elif '0' <= paths <= '9':
					pathsint = int(paths)
				else:
					pathsint = int(paths)
				# control some times color, other time something some else
				control = line[i * 4 + 3]
				if control == ' ':
					colorint = 0
				elif control >= 'a':
					colorint = ord(control) - ord('a') + 10
				elif '0' <= control <= '9':
					colorint = int(control)
				else:
					colorint = 0

				tile = 0
				if types == 'O':
					tile = Wheel(pathsint)
					base.numwheels += 1
				elif types == '+':
					tile = Trigger(self.colors)
				elif types == '!':
					tile = Stoplight(stoplight)
				elif types == '&':
					tile = Painter(pathsint, colorint)
				elif types == '#':
					tile = Filter(pathsint, colorint)
				elif types == '@':
					if control == ' ':
						tile = Buffer(pathsint)
					else:
						tile = Buffer(pathsint, colorint)
				elif types == ' ' or ('0' <= types <= '8'):
					tile = Tile(pathsint)
				elif types == 'X':
					tile = Shredder(pathsint)
				elif types == '*':
					tile = Replicator(pathsint, colorint)
				elif types == '^':
					if control == ' ':
						tile = Director(pathsint, 0)
					elif control == '>':
						tile = Switch(pathsint, 0, 1)
					elif control == 'v':
						tile = Switch(pathsint, 0, 2)
					elif control == '<':
						tile = Switch(pathsint, 0, 3)
				elif types == '>':
					if control == ' ':
						tile = Director(pathsint, 1)
					elif control == '^':
						tile = Switch(pathsint, 1, 0)
					elif control == 'v':
						tile = Switch(pathsint, 1, 2)
					elif control == '<':
						tile = Switch(pathsint, 1, 3)
				elif types == 'v':
					if control == ' ':
						tile = Director(pathsint, 2)
					elif control == '^':
						tile = Switch(pathsint, 2, 0)
					elif control == '>':
						tile = Switch(pathsint, 2, 1)
					elif control == '<':
						tile = Switch(pathsint, 2, 3)
				elif types == '<':
					if control == ' ':
						tile = Director(pathsint, 3)
					elif control == '^':
						tile = Switch(pathsint, 3, 0)
					elif control == '>':
						tile = Switch(pathsint, 3, 1)
					elif control == 'v':
						tile = Switch(pathsint, 3, 2)

				elif types == '=':
					if control in teleporter_names:
						other = teleporters[teleporter_names.index(control)]
						tile = Teleporter(pathsint, control, other)
					else:
						tile = Teleporter(pathsint, control)
						teleporters.append(tile)
						teleporter_names.append(control)

				self.set_tile(i, j, tile)

				if '0' <= types <= '8':
					if control == '^':
						direction = 0
					elif control == '>':
						direction = 1
					elif control == 'v':
						direction = 2
					else:
						direction = 3
					self.marbles.append(
						Marble(int(types), tile.rect.center, direction))

		if boardtimer <= 0:
			boardtimer = DEFAULT_BOARD_TIMER * base.numwheels
		a = lv.getint(section1, 'board_timer',fallback=boardtimer)
		seconds = 30 #fug
		self.board_timer = seconds + a
		self.board_timeout_start = (seconds + a) * FRAMES_PER_SEC
		self.board_timeout = self.board_timeout_start
		base.set_board_timer_ex += (base.lk * base.lkb)
		base.lkb = 0
		aa = self.board_timeout_start / 10
		self.board_timeout += base.set_board_timer_ex * aa
		aaa = base.set_board_timer_ex
		return

	# Return values for this function:
	# -4: User closed the application window
	# -3: User aborted the level
	# -2: Board timer expired
	# -1: Launch timer expired
	#  1: Level completed successfully
	#  2: User requested a skip to the next level
	#  3: User requested a skip to the previous level

	@property
	def play_level(self):
		# Perform the first render
		self.update()

		if base.edit_act:
			if not base.edit_play:
				return
		# Launch the first marble
		self.launch_marble()

		# Do the first update
		pygame.display.update()
		pygame.event.clear()
		if not base.edit_act:
			a = True
			while a:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
					if event.type == MOUSEBUTTONDOWN:
						a = False
					elif event.type == KEYDOWN:
						if event.key == K_ESCAPE:
							return -3
						if event.key == ord('n'):
							return 2
						elif event.key == ord('b'):
							return 3
			base.atime = 4
			hi = HighScore(self.game.score)
			hi.display()
			b = base.level

		base.gameloop = 0  # time to  play the game
		sptime = 5 * FRAMES_PER_SEC

		clock = pygame.time.Clock()
		self.board_complete = base.skip
		while not self.board_complete:
			clock.tick(FRAMES_PER_SEC)

			# Handle Input Events
			sptime -= 1
			for event in pygame.event.get():
				if event.type is QUIT:
					return -4
				elif event.type == KEYDOWN:
					if event.key is K_ESCAPE:
						if sptime > 0:
							return -3
						self.count_holes()
						hi = HighScore(9)
						hi.start()
						return -3
					elif event.key == ord('n'):
						if sptime > 0:
							return 2
					elif event.key == ord('b'):
						if sptime > 0:
							return 3
					elif event.key == ord(' ') or event.key == ord('p') or event.key == K_PAUSE:
						self.paused = self.paused ^ 1
						if self.paused:
							if base.screenshot:
								pause_popup = None
							else:
								self.pop.popup('Game Paused\n\n')
						else:
							self.pop.popdown()

				elif event.type == MOUSEBUTTONDOWN:
					self.click(pygame.mouse.get_pos())
					a = 3
			if not self.paused:
				base.gameloop += 1  # time to  play the game
				self.update()

		if base.edit_act:
			return -9
		# Play the end sound
		if base.skip:
			hi = HighScore(-1)
			hi.start()
			return self.board_complete
		self.count_holes()
		if self.board_complete > 0:
			play_sound(base.levelfinish)
			hi = HighScore(self.game.score)
			hi.start()
		else:
			play_sound(base.die)
			hi = HighScore(self.board_complete)
			hi.start()
		return self.board_complete


class HighScore:
	def __init__(self, flag):
		self.fail = '99999'
		self.flag = flag

	def start(self):
		maxdays = 28

		# last
		cur = []
		cc = [self.fail, '1', self.fail, '0']

		cur.append(datetime.now().strftime('%d/%b/%y %H:%M'))

		cur.append(repr((base.wheelnew + base.wheeldid) * 1000 + base.empty_holes))
		if self.flag == 0:  # complete
			cur.append(repr(base.gamelooptext))
			BS.score.set(base.level, 'cur', ','.join(cur))
		else:
			cur.append(self.fail)
			BS.score.set(base.level, 'opp', ','.join(cur))
		cur.append(datetime.now().strftime('%Y%m%d'))

		aa = []
		aa = [[0 for i in range(4)] for j in range(7)]

		for i in range(6):
			if not BS.score.has_option(base.level, 'ti' + repr(i)):
				aa[i] = [self.fail, '1', self.fail, '0']
			else:
				aa[i] = BS.score.get(base.level, 'ti' + repr(i)).split(',')

		for i in range(6):
			bbb = (datetime.now() - timedelta(days=(6 - i) * maxdays)).strftime('%Y%m%d')
			if bbb >= aa[i][3]:
				aa[i] = cc

		aa[6] = cur

		if not cur[2] == self.fail:
			for _ in range(6):
				for i in range(6):
					a = float(aa[i][2])
					b = float(aa[i + 1][2])
					if a >= b:
						temp = aa[i]
						aa[i] = aa[i + 1]
						aa[i + 1] = temp

		for i in range(6):
			# bb = (datetime.now() - timedelta(days=(6 - i) * maxdays)).strftime('%Y%m%d')
			# if bb >= aa[i][3]:
			#	aa[i] = cc

			BS.score.set(base.level, 'ti' + repr(i), ','.join(aa[i]))

		aa = [[0 for i in range(4)] for j in range(7)]

		for i in range(6):
			if not BS.score.has_option(base.level, 'sc' + repr(i)):
				aa[i] = ['0', '1', '2', '3']
			else:
				aa[i] = BS.score.get(base.level, 'sc' + repr(i)).split(',')

		aa[6] = cur
		for i in range(6):
			bb = (datetime.now() - timedelta(days=(6 - i) * maxdays)).strftime('%Y%m%d')
			if bb >= aa[i][3]:
				aa[i] = cc

		for _ in range(6):
			for i in range(6):
				a = float(aa[i][1])
				b = float(aa[i + 1][1])
				if a <= b:
					temp = aa[i]
					aa[i] = aa[i + 1]
					aa[i + 1] = temp

		for i in range(6):

			bb = (datetime.now() - timedelta(days=(6 - i) * maxdays)).strftime('%Y%m%d')
			if bb >= aa[i][3]:
				aa[i] = cc

			BS.score.set(base.level, 'sc' + repr(i), ','.join(aa[i]))

		staf.save1()
		base.atime = 0
		self.display()

	def display(self):
		mess = ''
		if base.skipoff == 1:
			base.skip = BS.score.getint(base.level, 'skip', fallback=0)
			if base.skip == 1:
				mess = '**  SKIP Level  SKIP Level\n'
		cur = ['', '', 0, '']
		opp = ['', '', 0, '']

		ti = []
		ti = [[0 for i in range(4)] for j in range(8)]
		sc = []
		sc = [[0 for i in range(4)] for j in range(6)]

		if BS.score.has_option(base.level, 'cur'):
			cur = BS.score.get(base.level, 'cur').split(',')
		if BS.score.has_option(base.level, 'opp'):
			opp = BS.score.get(base.level, 'opp').split(',')

		if cur[2] == self.fail:
			cur[2] = 'Failed'
		else:
			cur[2] = convert1(int(float(cur[2])))

		for i in range(6):
			ti[i] = BS.score.get(base.level, 'ti' + repr(i)).split(',')
			sc[i] = BS.score.get(base.level, 'sc' + repr(i)).split(',')

		if not cur[1] == '':
			mess += 'Time: ' + cur[2] + '   Score:' + cur[1] + ' - ' + cur[0] + '\n'
		if not opp[1] == '':
			mess += 'Failed:          Score:' + opp[1] + ' - ' + opp[0] + '\n'
		mess += '\nLowest TIME\n'
		for i in range(6):
			if not ti[i][2] == self.fail:
				ti[i][2] = convert1(int(float(ti[i][2])))
				mess += 'Time: ' + ti[i][2] + '   Score:' + ti[i][1] + ' - ' + ti[i][0] + '\n'
		mess += '\nHighest Score\n'
		for i in range(6):
			if not sc[i][1] == '1':
				if sc[i][2] == self.fail:
					sc[i][2] = 'Failed'
				else:
					sc[i][2] = convert1(int(float(sc[i][2])))
				mess += 'Time: ' + sc[i][2] + '   Score:' + sc[i][1] + ' - ' + sc[i][0] + '\n'
		mess += '\n\n'
		pop = PopWindow(base.screen)
		pop.popup(mess)
		pop.popwait(1)
		pop.popdown()



class PopWindow:
	def __init__(self, screen):
		self.screen = screen
		self.backbuf = 0
		self.winrect = 0

	def popup(self, text):
		maxwidth = 0
		objss = []
		objs = text.split("\n")
		for i in range(objs.__len__()):
			obj = base.popup_font.render(objs[i], 1, (0, 0, 0))
			maxwidth = max(maxwidth, obj.get_rect().width)
			objss.append(obj)

		linespacing = base.popup_font.get_linesize()
		window_width = maxwidth + 40

		window_height = base.popup_font.get_height() * (len(objs) - 0)
		window = pygame.Surface((window_width, window_height))

		self.winrect = window.get_rect()
		window.fill((0, 0, 0))
		window.fill((250, 250, 250), self.winrect.inflate(-2, -2))

		y = linespacing

		for obj in objss:
			textpos = obj.get_rect()
			textpos.top = y
			textpos.centerx = self.winrect.centerx
			window.blit(obj, textpos)
			y += linespacing

		self.winrect.center = self.screen.get_rect().center

		self.backbuf = pygame.Surface(self.winrect.size).convert()
		self.backbuf.blit(self.screen, (0, 0), self.winrect)

		self.screen.blit(window, self.winrect)
		pygame.display.update()

	def popdown(self):
		self.screen.blit(self.backbuf, self.winrect)
		pygame.display.update(self.winrect)

	def popwait(self, flag=0):  # 15Dec23 30Jun2026
		wait_one_sec()
		skt = (time.time() + base.atime)
		while 1:
			www = pygame.event.poll()
			if flag == 1:
				if base.skipoff == 1:
					if base.skip:
						if time.time() > skt:
							break
					if www.type == MOUSEBUTTONDOWN:
						break
					if www.type == KEYDOWN:
						if www.key == K_F1:
							if base.skip == 0:
								BS.score.set(base.level, 'skip', '1')
								base.skip = 1
								play_sound1(base.ping)
						if www.key == K_F2:
							BS.score.set(base.level, 'skip', '0')
							base.skip = 0
			elif flag == 2:
				if www.type == KEYDOWN:
					if www.key == K_EQUALS:
						break
			elif flag == 3:
				if www.type == KEYDOWN:
					if www.key == K_y:
						return True
					elif www.key == K_n:
						return False

			elif flag == 4:
				base.lk = 0
				if www.type == KEYDOWN:
					a =  0
					if www.key == K_a:
						a = 1
					elif www.key == K_r:
						a = 2
					elif www.key == K_l:
						base.lk = 1
						a = 2
					elif www.key == K_n:
						staf.lev(1)
						a = 2
					if a != 0:
						pygame.event.clear()
						return a
			if www.type == MOUSEBUTTONDOWN:
				break


		pygame.event.clear()
		return False





class Game:
	def __init__(self, screen, in_type):  # circuit, in_level:
		self.screen = screen
		self.type = in_type
		# self.circuit = circuit
		# self.extra_lives = 0
		self.pop = PopWindow(self.screen)
		self.level = 0  # in_level
		self.score = 0
		self.board = 0
		self.gamestart = time.time()

	def play(self):
		# Draw the loading screen

		#  backdrop = LoadImage('backdrop.jpg', -2, (SCREEN_WIDTH, SCREEN_HEIGHT))
		self.screen.blit(base.backdrop, (0, 0))
		pygame.display.update()

		while 1:
			# Play a level
			self.board = Board(self, BOARD_POS)
			if base.check:  # Setuo game level check for tranfer
				return
			rc = self.board.play_level
			if base.edit_act:
				time.sleep(1)
				self.editboard()
				pass
				return -4

			# Check for the user closing the window
			if rc == -4:
				return -4

			if rc == 2 or rc == 1:
				staf.lev(1)
				continue

			if rc == 3:
				staf.lev(-1)
				continue

			if rc < 0:
				# The board was not completed
				if rc == -3:
					return -3

				if rc == -2:
					message = 'The board timer has expired.'
					mmm = 'board timer 10%'
					base.lk = 0
					base.lkb = 1
				else:
					message = 'The launch timer has expired.'
					mmm = 'launch timer 1 count'
					base.lkb = 0
					base.lkl = 1
				message += '.\nR=Retry\nL= Retry. The ' + mmm + ' longer\nN=next\nA = Abort\n\n'
				# '.\nPress C to continue\nPress Q to quit level\n Press N next level\n\n'

				pop = PopWindow(base.screen)
				pop.popup(message)
				a = pop.popwait(4)
				pop.popdown()
				rc = 0
				if a == 2:  # retry
					continue
				if a == 1:  #A
					rc = -3
					return rc
					continue
				if a == 3:
					staf.lev(1)
					continue
		pygame.event.clear()
		return a


	def editboard(self):
		ps = BOARD_POS
		pygame.event.clear()
		a = True
		y = x = 0

		while a:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						pos = pygame.mouse.get_pos()
						x = int((pos[0] - ps[0]) / TILE_SIZE)
						y = int((pos[1] - ps[1]) / TILE_SIZE)
						if 0 <= x < HORIZ_TILES and 0 <= y < VERT_TILES:
							a = False
		self.gline = 'g' + str(y + 1)
		self.gline_val = BS.circuit.get(BS.section1, self.gline)
		j = x + 1
		for i in range(len(self.gline_val)):
			if self.gline_val[i] == '|':
				j -= 1
				if j == 0:
					break
		self.gline_pos = i
		self.types = self.gline_val[i + 1]
		self.paths = self.gline_val[i + 2]
		self.control = self.gline_val[i + 3]
		self.cycle = True
		basemenu = 1
		sec = thr = 0

		while self.cycle:
			self.x_load(self.types, self.paths, self.control)
			base.sr.save()

			if self.paths == ' ':
				pathsint = 0
			else:
				pathsint = int(self.paths, 16)

			pone = pathsint & 1
			ptwo = pathsint & 2
			pthe = pathsint & 4
			pfor = pathsint & 8

			#   New main menu
			if basemenu == 1:
				main = ('SELECT One', 'Pipe - Ball start', 'Wheel', 'Painter', 'Buffer', 'Filter', 'Teleporter',
				        'Shredder', 'Replicator', 'Switch or Director', 'Trigger',
				        'Stoplights', 'done')
			elif basemenu == 2:
				main = ('TURN ON Path', 'Up', '> Right', 'Down', '< Left', 'next')
			elif basemenu == 3:
				main = ('PICK ONE', 'Save', 'cancel', 'Clear')
			elif basemenu == 4:
				main = ('PICK A COLOR', 'Black', 'White', 'Blue', 'Green', 'Yellow', 'Purple', 'Red', 'Orange')
			elif basemenu == 5:
				main = ('PICK A COLOR or NONE', 'none', 'Black', 'White', 'Blue', 'Green', 'Yellow', 'Purple', 'Red',
				        'Orange')
			elif basemenu == 6:
				main = ('PICK A PARE', 'a', 'b', 'c', 'd', 'e', 'g')
			elif basemenu == 7:
				main = ('Pick one, Main path', 'Up', '> Right', 'Down', '< Left')
			elif basemenu == 8:
				main = ('Pick one, Second path', 'Up', '> Right', 'Down', '< Left', 'None = Director')
			elif basemenu == 9:
				main = ('Enter the Count', '2', '3', '4', '5', '6', '7', '8', '9')
			what2do = 1
			menu = MainMenu(self.screen, base.background2, main)
			menu.from_top(150)
			menu.draw_menu()  # Menu line to start
			while what2do == 1:
				what2do = menu.select()
			what2do -= 1
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			################################
			if basemenu == 1:
				if what2do == 1:  # pipe and where a ball starts
					self.types = ' '
					basemenu = 2
					sec = 5
					thr = 7
				elif what2do == 2:  # Wheel
					self.types = 'O'
					self.control = ' P1'
					basemenu = 2
					sec = 3
				elif what2do == 3:  # Painter
					self.types = '&'
					basemenu = 2
					sec = 4
				elif what2do == 4:  # Buffer
					self.types = '@'
					basemenu = 2
					sec = 5
				elif what2do == 5:
					self.types = '#'  # Filter
					basemenu = 2
					sec = 4
				elif what2do == 6:
					self.types = '='  # Teleporter  does not show right or play but store is right
					basemenu = 2
					sec = 6
				elif what2do == 7:  # Shredder
					self.types = 'X'
					basemenu = 2
					sec = 3
				elif what2do == 8:  # Replicator
					self.types = '*'
					basemenu = 2
					sec = 9
				elif what2do == 9:
					self.types = '.'  # Switch
					basemenu = 2
					sec = 7
				elif what2do == 10:  # Trigger
					self.types = '+'
					self.control = ' '
					basemenu = 3
				elif what2do == 11:  # stop
					self.types = '!'
					self.control = ' '
					basemenu = 3

				elif what2do == 12:  # exit
					basemenu = 3



			#################################################
			elif basemenu == 2:
				if what2do == 1:
					pone = not pone
				elif what2do == 2:  # wheel
					ptwo = not ptwo
				elif what2do == 3:
					pthe = not pthe
				elif what2do == 4:
					pfor = not pfor
				elif what2do == 5:
					basemenu = 1
					if self.control == ' P1':
						self.control = ' '
					if not sec == 0:
						basemenu = sec
						sec = thr
						thr = 0
					continue
				pathsint = 0
				if pone:
					pathsint += 1
				if ptwo:
					pathsint += 2
				if pthe:
					pathsint += 4
				if pfor:
					pathsint += 8
				self.paths = hex(pathsint)[2:]

			############################################
			elif basemenu == 3:
				if what2do == 3:
					self.types = self.control = self.paths = ' '
					what2do = 1
				if what2do == 1:
					i = self.gline_pos + 1
					char_list = list(self.gline_val)
					char_list[i] = self.types
					char_list[i + 1] = self.paths
					char_list[i + 2] = self.control
					self.gline_val = "".join(char_list)
					BS.circuit.set(BS.section1, self.gline, self.gline_val)
					with open(BS.circuitspath, 'w') as configfile:
						BS.circuit.write(configfile, False)
					self.cycle = False

				elif what2do == 2:
					return

			####################################################################
			elif basemenu == 4:
				self.control = str(what2do - 1)
				basemenu = 3

			###################################
			elif basemenu == 5:
				if what2do == 1:
					self.control = ' '
					basemenu = 3
				else:
					self.control = str(what2do - 2)
					if self.types == ' ':
						self.types = self.control
						self.control = ' '
						basemenu = 7
					else:
						basemenu = 3
						if not sec == 0:
							basemenu = sec
							sec = thr
							thr = 0

			#######################  does not show right or play but store is right
			elif basemenu == 6:
				self.control = chr(ord('a') + (what2do - 1))
				basemenu = 3
			#####################
			elif basemenu == 7 or basemenu == 8:
				a = 0

				if what2do == 1:
					a = '^'
				elif what2do == 2:
					a = '>'
				elif what2do == 3:
					a = 'v'
				elif what2do == 4:
					a = '<'
				elif what2do == 5 and basemenu == 8:
					a = ' '

				if basemenu == 7:
					if ('0' <= self.types <= '8'):
						self.control = a
						basemenu = 3
					else:
						self.types = a
						basemenu = 8
				else:
					self.control = a
					basemenu = 3
			elif basemenu == 9:  # Replicator
				self.control = str(what2do + 1)
				basemenu = 3

	def x_load(self, types, paths, control):  # (self, circuit, level):
		rect = pygame.Rect((350, 40, TILE_SIZE, TILE_SIZE))

		base.screen.blit(base.backdrop, (0, 0))
		pygame.display.update()
		pathsint = colorint = 0

		if paths == ' ':
			pathsint = 0
		else:
			pathsint = int(paths, 16)

		base.screen.blit(base.Tile_plains[pathsint], rect)

		if control == ' ':
			colorint = 0
		elif '0' <= control <= '9':
			colorint = int(control)
		else:
			colorint = 0

		tile = 0
		aa = 0
		if types == 'O':  # wheel
			if not control == ' P1':
				base.screen.blit(base.Wheel_images[0], rect)


		elif types == '+':
			# tile = Trigger(self.colors)
			base.screen.blit(base.Trigger_image, rect)
		elif types == '!':
			# tile = Stoplight(stoplight)
			base.screen.blit(Stoplight.image, rect)
		elif types == '&':  # paint
			# tile = Painter(pathsint, colorint)
			base.screen.blit(base.Tile_tunnels[pathsint], rect)
			base.screen.blit(base.Painter_images[colorint], rect)
		elif types == '#':
			tile = Filter(pathsint, colorint)
			base.screen.blit(base.Tile_tunnels[pathsint], rect)
			base.screen.blit(base.Filter_images[colorint], rect)
		elif types == '@':
			if control == ' ':
				# tile = Buffer(pathsint)
				base.screen.blit(base.Tile_tunnels[pathsint], rect)
				base.screen.blit(base.Buffer_top, rect)
				base.screen.blit(base.Buffer_bottom, rect)
			else:
				base.screen.blit(base.Tile_tunnels[pathsint], rect)
				base.screen.blit(base.Buffer_top, rect)
				base.screen.blit(base.Filter_images[colorint], rect)
		# tile = Buffer(pathsint, colorint)
		elif types == ' ' or ('0' <= types <= '8'):
			base.screen.blit(base.Tile_plains[pathsint], rect)
			if self.types != ' ':
				base.screen.blit(base.marble_images[int(self.types)], rect.center)
		# tile = Tile(pathsint)
		elif types == 'X':
			# tile = Shredder(pathsint)
			base.screen.blit(base.Tile_tunnels[pathsint], rect)
			base.screen.blit(Shredder.image, rect)
		elif types == '*':
			# tile = Replicator(pathsint, colorint)
			base.screen.blit(base.Tile_tunnels[pathsint], rect)
			base.screen.blit(Replicator.image, rect)
			text = base.info_font.render(' ' + self.control + ' ', True, pygame.Color(
				'white'), pygame.Color('blue'))
			base.screen.blit(text, rect)

		elif types == '^' or types == '>' or types == '<' or types == 'v':
			base.screen.blit(base.Tile_tunnels[pathsint], rect)
			if self.control == ' ':
				aa = 0
				if types == '^':
					aa = 0
				elif types == '>':
					aa = 1
				elif types == '<':
					aa = 3
				elif types == 'v':
					aa = 2
				base.screen.blit(base.Director_images[aa], rect)
			else:  # Switch
				aa = 0
				if types == '^':
					aa = 0
				elif types == '>':
					aa = 1
				elif types == '<':
					aa = 3
				elif types == 'v':
					aa = 2
				bb = 0
				if self.control == None:
					self.control = ' '
				if self.control == '^':
					bb = 0
				elif self.control == '>':
					bb = 1
				elif self.control == '<':
					bb = 3
				elif self.control == 'v':
					bb = 2
				cc = Switch.images[aa][bb]
				if cc == None:
					cc = base.Buffer_bottom
				text = base.info_font.render(' ' + self.control + ' ', True, pygame.Color(
					'black'), pygame.Color('green'))
				textRect = text.get_rect()
				cc.blit(text, textRect)
				base.screen.blit(cc, rect)


		elif types == '+':  # Trigger
			base.screen.blit(base.Trigger_image, rect)

		elif types == '!':  # wheel
			base.screen.blit(base.Wheel_images[0], rect)

		elif types == '=':
			if pathsint == 0:
				pathsint = 5

			if pathsint & 5:
				tel = pygame.Surface.copy(Teleporter.image_v)
			else:
				tel = pygame.Surface.copy(Teleporter.image_h)

			text = base.info_font.render(' ' + self.control + ' ', True, pygame.Color(
				'white'), pygame.Color('black'))
			textRect = text.get_rect()
			tel.blit(text, textRect)
			base.screen.blit(tel, rect)
		# Flip the display
		pygame.display.flip()


def main():
	"""
	start: 14 Jul 2020

	"""
	# Configure the audio settings
	if sys.platform[0:3] == 'win':
		# On Windows platforms, increase the sample rate and the buffer size
		pygame.mixer.pre_init(44100, -16, 1, 4096)

	# Initialize the game module
	pygame.init()

	if not pygame.font:
		print('Warning, fonts disabled')
	if not pygame.mixer:
		print('Warning, sound disabled')

	menu = MainLoop()
	menu.mainloop()

	pygame.quit()


# Static 24 Jan 2021
def convert1(seconds):
	s = int(seconds)
	minus = ""
	if seconds < 0:
		minus = "-"
		s = abs(s)
	m, s = divmod(s, 60)
	h, m = divmod(m, 60)
	return f'{h:0d}:{m:02d}:{s:02d}'


#  STATIC Function 15 Sep 2020
def play_sound(mixersound):
	if base.sound_on:
		mixersound.play()


def play_sound1(mixersound):
	mixersound.play()


#  STATIC Function 29 Sep 2020
# Load all the images for the various game classes.
# The images are stored as class variables in the corresponding classes.
def ImageLoad(name, colorkey=-1, size=-1):
	fullname = os.path.join('graphics', name)
	image = 0
	try:
		image = pygame.image.load(fullname)
	except pygame.error as message:
		print('Cannot load image:' + message, fullname)
		SystemExit()

	if size != -1:
		image = pygame.transform.scale(image, size)  # size = (width, height)
	image = image.convert()

	if colorkey != -2:  # -2 Not used.
		if colorkey == -1:  # -1 Use corner at 0,0
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, RLEACCEL)

	return image


#  STATIC Function 29 Sep 2020
# Load the sounds
def load_sound(name, volume=1.0):
	class NoneSound:
		def play(self):
			pass

	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound()
	fullname = os.path.join('sounds', name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error as message:
		print('Cannot load sound:', fullname)
		print(message)
		return NoneSound()

	sound.set_volume(volume * SOUND_EFFECTS_VOLUME)
	return sound


#  STATIC Function 17 Oct 2020
def menu_music():
	if base.music_on == 0:  # 0 off, 1 fur elise, 2 normal
		pygame.mixer.music.stop()
	elif base.music_on == 1:
		base.furelise.play()
	elif base.music_on == 2:
		base.intromusic.play()


#  STATIC Function 18 Oct 2020
def background_music():
	if base.background_on == 0:  # 0 off, 1 fur elise, 2 normal
		pygame.mixer.music.stop()
	elif base.background_on == 1:
		base.furelise.play()
	elif base.background_on == 2:
		base.gamemusic.play()


class MainLoop:
	status = 0

	def __init__(self):
		self.save_cur_area = (0, 0, 0, 0)  # not saved
		self.save_cur = 0
		self.screen = 0

		Options()

		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		base.screen = self.screen  # 15Dec23
		icon = pygame.image.load(os.path.join('graphics', 'icon.png'))
		pygame.display.set_icon(icon)
		icon.set_colorkey(icon.get_at((0, 0)), RLEACCEL)

		VersionPF()
		pygame.display.set_caption(
			'April Two moving balls -- Version ' + VersionPF.number + ' ' + VersionPF.date + '  ' + VersionPF.text)

		base.sound_on = BS.ex.getboolean('sys', "Effect", fallback=True)  # True
		base.music_on = BS.ex.getint('sys', "Music", fallback=0)  # 1  # 0 off, 1 fur elise, 2 normal
		base.background_on = BS.ex.getint('sys', "Background", fallback=0)  # 0 off, 1 fur elise, 2 normal
		base.board_time_sw = BS.ex.getint('sys', "board_time_sw", fallback=True)
		base.sr = SRscreen(base.screen)
		base.skipoff = BS.ex.getint('sys', "skipoff", fallback=0)

		# self.mu = Music()
		# base()
		Sound()
		Font()
		Images()

		# Parse the command line
		for arg in sys.argv[1:]:

			if arg == '-cb':
				base.colorblind = 1
		if base.colorblind:
			base.cbext = '-cb.png'

	def ExitGame(self):
		staf.save()

	def mainloop(self):
		cycle = True
		while cycle:
			#   New main menu
			mainmenu = 'Serial Level', 'Radom Level', 'Exit', 'Options', 'Edit'
			# no option
			menu_music()
			menu = TheMenu(self.screen, base.background, mainmenu, '')

			menu.from_top(100)

			menu.draw_menu()  # Menu line to start
			what2do = menu.select()
			if what2do < 0:  # quit
				return
			elif what2do == 1:
				background_music()
				game = Game(self.screen, 0)  # 'all-boards', base.set_level
				a = game.play()
				if a == -4:
					self.ExitGame()
					exit(0)
				menu_music()



			elif what2do == 2:
				background_music()
				game = Game(self.screen, 1)  # 'all-boards', base.set_level)
				game.play()
				menu_music()

			elif what2do == 3:
				self.ExitGame()
				return

			elif what2do == 5:
				Editor(base.screen)
				pass

			else:
				self.menu_opt()
				staf.save()

	def menu_opt(self):
		opti_text = ("", "Off|Fur Elise|Normal", "Off|Fur Elise|Normal",
		             "Off|On", "Off|On", 'Off|On', "")
		while 1:
			menu_text = ("Main menu", "Music: ", "Back Music: ",
			             "Effect Sounds: ", "Board timeout: ", 'Skip Level:', "Editor (not fuctional)")
			menu = TheMenu(self.screen, base.background, menu_text, opti_text)
			menu.from_top(100)

			menu.draw_menu()  # Menu line to start
			what2do = menu.select()
			""" Output:
			-1 X button
			-2 Esc Key
			1 and up  Line number of menu.
			"""
			if what2do == -1:  # quit
				return
			elif what2do == -2:  # esc key
				return

			elif what2do == 1:  # menu quit
				return

			elif what2do == 8:  # editor
				pygame.mixer.music.stop()
				edi = Editor(self.screen)
				menu_music()


class ScrollText:
	def __init__(self, screen, textimage, y, speed, offset=10):
		self.screen = screen
		self.speed = speed
		self.image = textimage
		self.offset = offset
		self.textrect = self.image.get_rect()
		self.start_pos = (screen.get_rect().right - offset, y)
		self.area = (offset, y, screen.get_rect().right - offset * 2, self.textrect.bottom)
		self.move_pos = self.textrect.move(self.start_pos, )

	def move(self):
		if self.move_pos.left - self.speed < -self.textrect.right + self.offset:
			self.move_pos = self.textrect.move(self.start_pos, )
		else:
			self.move_pos.left = self.move_pos.left - self.speed

	def draw(self, bottomimage):
		self.screen.blit(bottomimage, self.area, self.area)
		self.move()
		self.screen.set_clip(self.area)
		self.screen.blit(self.image, self.move_pos)
		self.screen.set_clip()


class TheMenu(MainMenu):
	def __init__(self, in_screen, in_background, in_menu_text, in_option, id=False):
		a = MainMenu.__init__(self, in_screen, in_background, in_menu_text, in_option)
		self.first = 0
		self.second = 0
		self.sound = base.menu_scroll

		s = 9

	def in_options(self, index):  # must override if options are used
		a = index
		if index == 2:
			return base.music_on  # 0 off, 1 fur elise, 2 normal
		elif index == 3:
			return base.background_on  # 0 off, 1 fur elise, 2 normal
		elif index == 4:
			return base.sound_on  # True False
		elif index == 5:
			return base.board_time_sw  # True False
		elif index == 6:
			return BS.ex.getint('sys', "Skipoff", fallback=0)
		return 0

	def out_options(self, vdata, index):  # must override if options are used
		"""
		:param vdata: the value for that index to be stored
		:param index: 1 base Line 1
		"""
		if index == 2:
			base.music_on = vdata
			BS.ex.set('sys', "Music", str(base.music_on))
			menu_music()
		elif index == 3:
			base.background_on = vdata
			BS.ex.set('sys', "Background", str(base.background_on))
		elif index == 4:
			base.sound_on = vdata  # True False
			BS.ex.set('sys', "Effect", str(base.sound_on))
		elif index == 5:
			base.board_time_sw = vdata  # True False
			BS.ex.set('sys', "board_time_sw", str(base.board_time_sw))
		elif index == 6:
			base.skipoff = vdata
			BS.ex.set('sys', "skipoff", str(base.skipoff))

	def select_extra(self):
		self.sound.play()

	def in_draw(self):
		ver = VersionPF()
		font = pygame.font.SysFont('arial', 18)
		textver = font.render(ver.number + " " + ver.date, 1, (40, 40, 40))
		textverrect = textver.get_rect()
		textver_pos = textverrect.move(self.background.get_rect().right - textverrect.right - 10, 580)
		self.screen.blit(textver, textver_pos)
		y = 550
		font = pygame.font.SysFont('arial', 22)

		text = font.render(
			"Copyright © 2020-22 2024-26  Phillip Forrestal   Version: " + ver.number + " " + ver.date + " " + ver.text +
			" - Conversion for pygame " + f"{pygame.version.ver}" + " SDL  " + f'{pygame.version.SDL}'
			+ " , Python (" + f"{sys.version_info.major}" + '.' + f"{sys.version_info.minor}" + ")    ", 1,
			(40, 40, 40))
		self.second = ScrollText(self.screen, text, y, 2)

		y = 525
		font = pygame.font.SysFont('arial', 20)
		text = font.render("Copyright © 2003  John-Paul Gignac. Version 1.13    Soundtrack by Matthias Le Bidan.    "
		                   "Board designs contributed by Mike Brenneman and Kim Gignac.    "
		                   "To contribute your own board designs, see the website:    "
		                   "http://pathological.sourceforge.net/    "
		                   "Logo by Carrie Bloomfield.    Other graphics based on artwork by Mike Brenneman.    "
		                   "Project motivated by Paul Prescod.    Thanks to all my friends who helped make this project a success!    "
		                   "This program is free software; you can redistribute it and/or modify it under the terms of "
		                   "the GNU General Public License.  See the LICENSE file for details.", 1, (60, 60, 60))
		self.first = ScrollText(self.screen, text, y, 3)

		# Title
		font = pygame.font.SysFont('arial', 40)
		textver = font.render("April Two, moving balls", 0, (255, 255, 255))
		textverb = font.render("April Two, moving balls", 0, 0)

		textverrect = textver.get_rect()
		textver_pos = textverrect.right / 2 + 80, 40
		self.screen.blit(textverb, textver_pos)
		self.screen.blit(textver, textver_pos)

	def in_select(self):
		self.first.draw(self.background)
		self.second.draw(self.background)


class Options:
	def __init__(self):
		base.screenshot = 0
		base.fullscreen = 0
		base.colorblind = 1
		base.cbext = '.png'  # base.cbext = '-cb.png'
		#	base.sound_on =  1  # True
		# base.music_on = 1  # 1  # 0 off, 1 fur elise, 2 normal
		# base.background_on = 2  # 0 off, 1 fur elise, 2 normal
		base.music_loaded = 0
		#  base.write_highscores = "highscores"
		base.set_level = 0  # 1st level


class MusicItem:
	def __init__(self, name, volume):
		self.volume = volume
		self.loaded = True  # Music will load

		self.fullname = os.path.join('music', name)
		try:
			pygame.mixer.music.load(self.fullname)
		except pygame.error as message:
			print('Cannot load music:', self.fullname, message)
			self.loaded = False  # Music will load

	def play(self):
		if self.loaded is True:
			pygame.mixer.music.load(self.fullname)
			pygame.mixer.music.set_volume(self.volume)
			pygame.mixer.music.play(-1)


class Sound:
	def __init__(self):
		# Music
		base.furelise = MusicItem("furelise.ogg", 0.4)
		base.intromusic = MusicItem("intro.ogg", 0.4)
		base.gamemusic = MusicItem("background.xm", 0.5)

		# Sound
		base.filter_admit = load_sound('filter_admit.wav', 0.8)
		base.wheel_turn = load_sound('wheel_turn.wav', 0.8)
		base.wheel_completed = load_sound('wheel_completed.wav', 0.7)
		base.change_color = load_sound('change_color.wav', 0.8)
		base.direct_marble = load_sound('direct_marble.wav', 0.6)
		base.ping = load_sound('ping.wav', 0.8)
		base.trigger_setup = load_sound('trigger_setup.wav')
		base.teleport = load_sound('teleport.wav', 0.6)
		base.marble_release = load_sound('marble_release.wav', 0.5)
		base.levelfinish = load_sound('levelfinish.wav', 0.6)
		base.die = load_sound('die.wav')
		base.incorrect = load_sound('incorrect.wav', 0.15)
		base.switch = load_sound('switch.wav')
		base.shredder = load_sound('shredder.wav')
		base.replicator = load_sound('replicator.wav')
		base.extra_life = load_sound('extra_life.wav')
		base.menu_scroll = load_sound('menu_scroll.wav', 0.8)
		base.menu_select = load_sound('switch.wav')


class SRscreen:
	def __init__(self, screen):
		self.screen = screen
		base.background2 = 0
		self.winrect = 0

	def save(self):
		self.winrect = self.screen.get_rect()
		base.background2 = pygame.Surface(self.winrect.size).convert()
		base.background2.blit(self.screen, (0, 0), self.winrect)

	def restore(self):
		self.screen.blit(base.background2, self.winrect)
		pygame.display.update(self.winrect)


class Editor():
	"""
	9 Dec 2025
	redo 22Jul26
	"""

	def __init__(self, screen):
		self.level = base.level
		if base.level is None:
			self.level = ''
		staf.save()

		base.edit_act = True
		base.edit_play = False
		self.screen = screen

		self.test = 'test'
		BS.circuitspath = os.path.join(BS.circuitspath, 'testlvs')
		BS.circuit = 0
		BS.circuit = configparser.ConfigParser()

		flag = False
		if os.path.isfile(BS.circuitspath):
			BS.circuit.read(BS.circuitspath)
			if not BS.circuit.has_section('test'):
				BS.circuit.add_section('test')
				flag = True
		else:
			flag = True
		if flag:
			if not BS.circuit.has_section('test'):
				BS.circuit.add_section('test')
			self.clrlevel()

		BS.circuit.read(BS.circuitspath)
		self.read_level()
		self.write_level(BS.circuit)
		self.save_level()
		self.doedit()

	def clrlevel(self):
		line = '|'
		for j in range(HORIZ_TILES):
			line += '   |'
		for i in range(VERT_TILES):
			BS.circuit.set('test', 'g' + str(i + 1), line)

	def save_level(self):
		with open(BS.circuitspath, 'w') as configfile:
			BS.circuit.write(configfile, False)

	def read_level(self):
		self.tname = BS.circuit.get('test', 'name', fallback='test')
		self.tversion = BS.circuit.get('test', 'version', fallback='2.0')
		self.tscore = BS.circuit.get('test', 'score', fallback='')
		self.tauthor = BS.circuit.get('test', 'author', fallback='PRF')
		self.tmaxmarbles = BS.circuit.get('test', 'maxmarbles', fallback='10')  # 10
		self.tlaunchtimer = BS.circuit.get('test', 'launchtimer', fallback='6')  # 6
		self.tboardtimer = BS.circuit.get('test', 'boardtimer', fallback='0')
		self.tcolors = BS.circuit.get('test', 'colors', fallback=DEFAULT_COLORS)
		self.tstoplight = BS.circuit.get('test', 'stoplight', fallback=DEFAULT_STOPLIGHT)

	def write_level(self, temp: object, a='test', nw=0):
		temp.set(a, 'name', self.tname)
		temp.set(a, 'version', self.tversion)
		temp.set(a, 'score', self.tscore)
		temp.set(a, 'author', self.tauthor)
		if int(self.tmaxmarbles) >= 0 or self.tmaxmarbles == '10':  # default
			if temp.has_option(a, 'maxmarbles'):
				temp.remove_option(a, 'maxmarbles')
		else:
			temp.set(a, 'maxmarbles', self.tmaxmarbles)

		if int(self.tlaunchtimer) >= 0 or self.tlaunchtimer == '10':  # default
			if temp.has_option(a, 'launchtimer'):
				temp.remove_option(a, 'launchtimer')
		else:
			temp.set(a, 'launchtimer', self.tlaunchtimer)

		if int(self.tboardtimer) == 0 or int(self.tboardtimer) == (30 * nw):  # default
			if temp.has_option(a, 'boardtimer'):
				temp.remove_option(a, 'boardtimer')
		else:
			temp.set(a, 'boardtimer', self.tboardtimer)

		dd = DEFAULT_COLORS
		colors = self.tcolors
		flag = True
		for i in range(len(colors)):
			if self.tcolors[i].isdecimal():
				if colors[i] in dd:
					dd = dd.replace(colors[i], '', 1)
				else:
					flag = False
					break
		if not dd == '':
			flag = False
		if flag:
			if temp.has_option(a, 'colors'):
				temp.remove_option(a, 'colors')
		else:
			temp.set(a, 'colors', self.tcolors)

		flag = True

		dd = DEFAULT_STOPLIGHT
		color = self.tstoplight
		for i in range(len(color)):
			if colors[i].isdecimal():
				if colors[i] in dd:
					dd = dd.replace(colors[i], '', 1)
				else:
					flag = False
					break
		if not dd == '':
			flag = False
		if flag:
			if temp.has_option(a, 'stoplight'):
				temp.remove_option(a, 'stoplight')
		else:
			temp.set(a, 'stoplight', self.tstoplight)

	def doedit(self):
		self.editmenu()
		exit()

	# Each tile consists of three characters:  A tile type, a path descriptor
	# and a tile-type-specific control character.  If the tile is a painter or
	# a filter, the control character should be a color.  If the tile is a
	# switch, the control character should be the secondary switch direction
	# (^, >, v, or <).  If the tile is an initial marble location, the control
	# character should be the marble's initial direction of travel.  If the
	# tile is a teleporter, the control character is an arbitrary label used to
	# match it up with its partner teleporter.  If the tile type is a buffer,
	# the control character may be either a color to denote the initial marble
	# color, or blank to denote that the buffer is initially empty.  All other
	# tile types ignore the control character.

	# Note that this file is not validated.  If there are errors of any sort
	# in this file, the results are undefined.

	# Tile Types           Paths          Colors (control)
	# ----------           -----------    ----------
	# O - Wheel                           0 - Black
	# & - Painter          1:N            1 - White
	# # - Filter           2:E            2 - Blue
	# ^>v< - Arrow/Switch  4:S            3 - Green
	# = - Teleporter       8:W            4 - Yellow
	# + - Trigger  was %                  5 - Purple
	# ! - Stoplights                      6 - Red
	# @ - Buffer                          7 - Orange
	# X - Shredder                        8 - Crazy (wildcard)
	# * - Replicator
	# 0-8 - Initial marble location (the digit specifies the marble color)

	# Level parameters:
	# -----------------
	# name        - The name of the level (unick id)
	# author      - The person who designed the level (may include email address) not used
	# launchtimer - The launch timer, measured in number of passes (default: 6)
	# boardtimer  - The board timer, in seconds (default: 30 * number of wheels)
	# colors      - The colors that will be served on this level (default: 2,3,4,6)
	# maxmarbles  - The maximum number of active marbles (default: 10)
	# stoplight   - The colors in the stoplight (default: 6,4,3)
	def editop(self):
		cycle = True
		while cycle:
			base.stoplight = False
			self.read_level()
			base.check = True  # Setuo game level
			game = Game(self.screen, 2)
			game.play()
			base.check = False
			if base.stoplight:
				sl = self.tstoplight
			else:
				sl = 'Not Used'

			opmenu = ('Main MENU -- 0 = default',
			          'level Name: ' + self.tname,
			          'Score: ' + self.tscore, 'Author: ' + self.tauthor,
			          'Max active marbles [default: 10] ' + self.tmaxmarbles,
			          'Launch Timer [default: 6] ' + self.tlaunchtimer,
			          'Board Timer [default: 30 * ' + str(base.numwheels) + ' (' +
			          str(30 * base.numwheels) + ')] ' + self.tboardtimer,
			          'colors [default: 2,3,4,6] ' + self.tcolors,
			          'stoplight [default: 6,4,3] ' + sl)

			menu = MainMenu(self.screen, base.background, opmenu)
			menu.from_top(10)
			menu.draw_menu()  # Menu line to start
			what2do = menu.select()
			if what2do == 1:
				self.save_level()
				cycle = False
			elif what2do == 2:
				self.tname = menu.key_input(self.tname)
			elif what2do == 3:  # score
				self.tscore = menu.key_input(self.tscore)
			elif what2do == 4:  # author
				self.tauthor = menu.key_input(self.tauthor)
			elif what2do == 5:  # maxmarbles
				self.tmaxmarbles = menu.key_input(self.tmaxmarbles, True)
			elif what2do == 6:
				self.tlaunchtimer = menu.key_input(self.tlaunchtimer, True)
			elif what2do == 7:
				self.tboardtimer = menu.key_input(self.tboardtimer, True)
			elif what2do == 8 or (base.stoplight and what2do == 9):
				self.tcolors, self.tstoplight = self.color_menu(self.tcolors, self.tstoplight, base.stoplight)

			self.write_level(BS.circuit)

	def editmenu(self):
		cycle = True

		while cycle:
			#   New main menu
			mainmenu = ('Editor Menu', 'Transfer level', 'Map Options', 'Exit Program', 'Show', 'Play')
			# no option
			menu = MainMenu(self.screen, base.background, mainmenu)
			menu.from_top(100)

			menu.draw_menu()  # Menu line to start
			what2do = menu.select()
			if what2do == 1:
				pass
			elif what2do == 2:
				self.transfer_menu()
			elif what2do == 3:
				self.editop()
			elif what2do == 4:
				cycle = False
			elif what2do == 5:
				base.edit_play = False
				game = Game(self.screen, 2)
				game.play()
				cycle = True
			elif what2do == 6:
				base.edit_play = True
				game = Game(self.screen, 2)
				game.play()
				cycle = True

		sys.exit

	def transfer_menu(self):

		cycle = True
		cuson = 1
		while cycle:
			#   New main menu
			if self.level == '':
				a = 'not available'
			else:
				a = 'Transfer From Main or New: ' + self.level
			mainmenu = ('Transfer level menu', a,
			            'Clear level',
			            'Transfer to NEW end', 'Exit Transfer')
			# no option
			menu = MainMenu(self.screen, base.background, mainmenu)
			menu.from_top(100)

			menu.draw_menu(cuson)  # Menu line to start
			what2do = menu.select()
			if what2do == 1:
				continue
			elif what2do == 2:
				if self.level == '':
					continue
				temppath = os.path.join('circuits')
				temp = configparser.ConfigParser()
				temp.read(os.path.join(temppath, 'levels'))
				lv = 0
				if temp.has_section(self.level):
					lv = temp
				elif BS.new.has_section(self.level):
					lv = BS.new
				if lv == 0:  # will the source
					continue

				a = (BS.circuit.sections())  # testlvs
				for i in a:
					BS.circuit.remove_section(i)
				BS.circuit.add_section("test")

				a = lv.options(self.level)  # source
				for i in a:
					b = lv.get(self.level, i)
					BS.circuit.set('test', i, b)
				temp = lv = 0
				self.save_level()
				play_sound1(base.extra_life)
				cuson = 5
			elif what2do == 3:
				cuson = 5
				self.clrlevel()

			elif what2do == 4:
				base.stoplight = False
				base.edit_play = True
				base.check = True  # Setuo game level
				game = Game(self.screen, 2)
				game.play()

				self.read_level()
				g = []
				for i in range(6):
					g.append(BS.circuit.get('test', 'g' + str(i + 1)))

				f = True
				temp = configparser.ConfigParser()
				tempfile = os.path.join('circuits', 'levels')
				temp.read(tempfile)
				if temp.has_section(self.tscore):
					play_sound1(base.incorrect)
					Message('Score IS NOT unique to Main')
					f = False
				temp = 0
				temp = configparser.ConfigParser()
				tempfile = os.path.join('circuits', 'new_levels')
				temp.read(tempfile)
				if f:
					if temp.has_section(self.tscore):
						play_sound1(base.incorrect)
						f = Message('Score IS NOT unique to NEW\n Over write: ', 3)  # ask
						if f:
							temp.remove_section(self.tscore)
				if f:
					temp.add_section(self.tscore)
					self.write_level(temp, self.tscore, base.numwheels)

					for i in range(6):
						temp.set(self.tscore, 'g' + str(i + 1), g[i])

					with open(tempfile, 'w') as configfile:
						temp.write(configfile, False)
					temp = tempfile = None
					play_sound1(base.extra_life)
				temp = 0
				cuson = 5

			elif what2do == 5:
				cycle = False

	def color_menu(self, col, sto, flag):
		opti_text = [""]
		for i in range(8):
			if flag:
				opti_text.append("Off|On|SL top|SL mid|SL bot")
			else:
				opti_text.append("Off|On")
		opti_text.append("Off|On")

		menu_text = ['Which Color, SL = Stop Light', 'Black: ', 'White: ', 'Blue:  ', 'Green: ', 'Yellow:',
		             'Puple: ', 'Red:   ', 'Orange:', 'Crazy: ', 'Default', 'exit']
		while 1:

			base.ccc = [0] * 9
			ss = ''
			if flag:
				for char in sto:
					if char.isdigit():  # Check if the character is a number
						ss += char

			for i in range(len(col)):  # n, n n = color
				a = col[i]
				if a.isdigit():
					base.ccc[int(a)] = ss.find(a) + 2

			menu = The1Menu(self.screen, base.background, menu_text, opti_text)
			menu.from_top(50)
			menu.draw_menu(5)  # Menu line to start
			what2do = menu.select()
			if what2do == 1:
				continue
			elif what2do == 11:
				col = '2346'
				sto = '643'
				continue
			elif what2do == 12:
				col = ''
				t = m = b = '0'
				for i in range(9):
					a = base.ccc[i]
					if not a == 0:
						col += str(i)
					if a == 2:
						t = str(i)
					elif a == 3:
						m = str(i)
					elif a == 4:
						b = str(i)
				sto = t + m + b
				return col, sto


class The1Menu(MainMenu):
	def __init__(self, in_screen, in_background, in_menu_text, in_option, id=False):
		a = MainMenu.__init__(self, in_screen, in_background, in_menu_text, in_option)

	def in_options(self, index):  # must override if options are used
		a = index - 2
		if 0 <= a <= 8:
			return base.ccc[a]

	def out_options(self, vdata, index):  # must override if options are used
		"""
		:param vdata: the value for that index to be stored
		:param index: 1 base Line 1
		"""
		a = index - 2
		if 0 <= a <= 9:
			# base.ccc.insert(a,vdata)
			base.ccc[a] = vdata
			pass


"""
####################################################################
# Level parameters:
# -----------------
# name        - The name of the level - Required must be a unique id
# author      - The person who designed the level (may include email address)
# launchtimer - The launch timer, measured in number of passes (default: 6)
# boardtimer  - The board timer, in seconds (default: 30 * number of wheels)
# colors      - The colors that will be served on this level (default: 2,3,4,6)
# maxmarbles  - The maximum number of active marbles (default: 10)
# stoplight   - The colors in the stoplight (default: 6,4,3)

# name=The Game - The name of the level - Required must be a unique id
"""

if __name__ == "__main__":
	main()
