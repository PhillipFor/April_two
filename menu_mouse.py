
class VersionPF:
	"""
	version 1.06 16 Oct 2020 Finish adding option choice
	"""
	def __init__(self):
		self.number = "1.11"
		self.date = "26 Jun 2026"
		self.text = "add int_input"

"""
Copyright Phillip Forrestal 2023
Program name: menu mouse
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Finish adding option choice
::Version
1.11 26 Jun 2026 add int_input
1.10 = 2 Jan 2026 add key_input
1.09 24 Dec 2025 id
1.08 15 Jan 2024 With * can a both 
1.07 24 Nov 2023 Fix keyboard
1.06 16 Oct 2020 Finish adding option choice
1.05 15 Oct 2020 If option Space/Enter not used - tick faster
1.04 14 Oct 2020 Set up the left/right and output
1.03 12 Oct 2020 Left right on choice with in/out
1.02 11 Oct 2020 Add Option choice
1.01 30 Sep 2020 Add double click
1.00 25 Sep 2020 Done
0.08 24 Sep 2020 Mouse fuctions
0.07 24 Sep 2020 Fix below
0.06 23 Sep 2020 Offset, overrides
0.05 23 Sep 2020 Background working, def setting
0.04 22 Sep 2020 Add cursor bar
0.03 21 Sep 2020 Menu on screen
0.02 20 Sep 2020 test some
0.01 20 Sep 2020 Start size of menu


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
"""

import pygame
from pygame.locals import *


class MainMenu:
	def __init__(self, in_screen, in_background, in_menu_text, in_option_text="", id_text=''):
		self.screen = in_screen
		self.cursor_down = -1  # double click count

		self.id = list(id_text)
		self.idflag = True
		if id_text == '':
			self.idflag = False
		#  What to display in menu
		self.menu_text = list(in_menu_text)
		self.menu_option = list(in_option_text)
		if in_option_text == "":
			self.option_used = False
		else:
			self.option_used = True
		self.text_rend = []
		self.cursor_rects = []  # used in mouse self.cursor_rects[ii].collidepoint(x, y):
		#  On this background
		self.background = in_background

		# Font
		self.menu_font_height = 24
		self.menu_font = pygame.font.SysFont("Consolas", self.menu_font_height) # Arial Consolas Courier

		self.cursor_lr_margin = 5
		self.cursor_tb_margin = 2
		self.offset_top = 0
		self.offset_left = 0

		# Color of menu text and menu bar
		self.menu_text_color = (255, 255, 255)
		self.cursor_color = (60, 60, 60)

		# Start of draw menu. Over lap.

		# Start with menu item
		self.cursor = 0  # Select item  Top
		self.cur_h = 0
		# compute the menu size and lines

		self.menu_rect = Rect(0, 0, 0, 0)  #
		self.cursor_rect = Rect(0, 0, 0, 0)

		self.save_cur = -1  # -1 not been saved. Valid 0 to len of menu

		self.mouse_moves = True

	def in_options(self, index):  # must override if options are used
		"""
		:param index:  1 base
		:return: the option value for that index (int)
		"""
		pass

	def out_options(self, value, index):  # must override if options are used
		"""
		;param value: the value for that index to be stored
		:param index: 1 base Line 1
		"""
		pass

	def draw_menu(self, in_cursor=1):
		# Start with menu item
		self.save_cur = -1  # -1 not been saved. Valid 0 to len of menu
		self.cursor = in_cursor - 1  # Select cursor line 0 to end
		self.cur_h = 0  # must be 0
		# compute the menu size and lines
		self.text_rend = []
		self.cursor_rects = []  # used in mouse self.cursor_rects[ii].collidepoint(x, y):


		self._draw_background()
		w = 0
		h = 0
		cnt = len(self.menu_text)
		cntopt = len(self.menu_option)
		# computer area of text include option text , look for the largest rect need.

		for i in range(cnt):
			txt = self.menu_text[i]
			if self.option_used:
				if i >= cntopt:
					opt = ""
					self.menu_option.append("")
				else:
					opt = self.menu_option[i]
			else:
				opt = ""

			if opt != "":
				spt = opt.split("|")
				for each in spt:
					aa = self.menu_font.render(txt + " " + each, 1, self.menu_text_color)
					aa = aa.get_rect()
					w = max(w, aa.w)
					h = max(h, aa.h)
			else:
				aa = self.menu_font.render(txt, 1, self.menu_text_color)
				aa = aa.get_rect()
				w = max(w, aa.w)
				h = max(h, aa.h)

		cur_w = w + self.cursor_lr_margin * 2
		self.cur_h = h + self.cursor_tb_margin * 2

		# the cursor rect same size of each line
		self.cursor_rect = Rect(0, 0, cur_w, self.cur_h)
		#
		self.menu_rect = Rect(0, 0, cur_w, self.cur_h * cnt)
		# Center menu on screen
		scr_rect = self.screen.get_rect()
		#  NEED to add offset
		self.menu_rect.center = scr_rect.center

		if self.offset_top > 0:
			self.menu_rect.top = self.offset_top

		if self.offset_left > 0:
			self.menu_rect.left = self.offset_left

		y = self.menu_rect.top + self.cursor_tb_margin

		for i in range(cnt):
			txt = self.menu_text[i]
			if self.option_used:
				if i < cntopt:
					opt = self.menu_option[i]
					if opt != "":
						spt = opt.split("|")
						val = self.in_options(i + 1)
						txt = txt + " " + spt[val]

			aa = self.menu_font.render(txt, 1, self.menu_text_color)
			self.text_rend.append(aa)
			self.screen.blit(aa, (self.menu_rect.left + self.cursor_lr_margin, y))
			self.cursor_rects.append(Rect(self.menu_rect.left, self.menu_rect.top + (i * self.cur_h), cur_w, self.cur_h))
			y += self.cur_h

		self._draw_cursor()
		self.in_draw()
		pygame.display.update()  # update display

	def select(self):
		clock = pygame.time.Clock()

		while True:
			# slow frame rate for menu
			clock.tick(30)
			self.cursor_down -= 1  # used in double click

			self.in_select()  # override per tick cycle

			pygame.display.update()  # update display

			is_option_line = False
			is_option_sel = False
			if self.option_used:   # determine if line is an option
				if self.menu_option[self.cursor] != "":
					is_option_line = True
					if self.menu_text[self.cursor][0] == '*':
						is_option_sel = True

			for event in pygame.event.get():
				if event.type is QUIT:
					return -1
				elif event.type == KEYDOWN:   #  ~~~~~~~~~~~~~~~ need override to turn off  THINK ABOUT 0A15
					if event.key == K_ESCAPE:
						return -2

					elif event.key == K_DOWN:
						self.select_extra()
						self.cursor += 1
						if self.cursor == len(self.menu_text):
							self.cursor = 0
						self._draw_cursor()

					elif event.key == K_UP:
						self.select_extra()
						self.cursor -= 1
						if self.cursor < 0:
							self.cursor = len(self.menu_text) - 1
						self._draw_cursor()

					elif not is_option_line:

						if event.key == K_SPACE or event.key == K_RETURN:
							return self.cursor + 1

					elif is_option_line:
						if is_option_sel is True:
							if event.key == K_SPACE or event.key == K_RETURN:
								return self.cursor + 1

						if event.key == K_LEFT:
							opt = self.menu_option[self.cursor]
							spt = opt.split("|")
							val = self.in_options(self.cursor + 1) - 1
							if val == -1:
								val = len(spt) - 1
							self.out_options(val, self.cursor + 1)
							txt = self.menu_text[self.cursor] + " " + spt[val]
							self.text_rend[self.cursor] = self.menu_font.render(txt, 1, self.menu_text_color)
							self._draw_cursor()

						elif event.key == K_RIGHT:
							opt = self.menu_option[self.cursor]
							spt = opt.split("|")
							val = self.in_options(self.cursor +1) + 1  # val = 1  # val get from outside
							if len(spt) == val:
								val = 0
							self.out_options(val, self.cursor +1)
							txt = self.menu_text[self.cursor] + " " + spt[val]
							self.text_rend[self.cursor] = self.menu_font.render(txt, 1, self.menu_text_color)
							self._draw_cursor()

				elif event.type == MOUSEBUTTONDOWN:
					mousex, mousey = event.pos
					hit = self._checkpos(mousex, mousey)
					if hit >= 0:
						if self.mouse_moves:
							self.select_extra()  # Override
							if self.cursor == hit:
								if self.cursor_down > 0:
									if is_option_line:  # do option next
										opt = self.menu_option[self.cursor]
										spt = opt.split("|")
										val = self.in_options(self.cursor + 1) + 1  # val = 1  # val get from outside
										if len(spt) == val:
											val = 0
										self.out_options(val, self.cursor + 1)
										txt = self.menu_text[self.cursor] + " " + spt[val]
										self.text_rend[self.cursor] = self.menu_font.render(txt, 1, self.menu_text_color)
										self._draw_cursor()
									else:
										return	(hit + 1)
								else:
									self.cursor_down = 15  # Tick cound 1 sec is 15
							else:
								self.cursor = hit
								self._draw_cursor()
								self.cursor_down = 15  # Tick cound 1 sec is 15
						else:
							return (hit + 1)


	def _draw_cursor(self):
		if self.save_cur != -1:  # -1 has not been set
			#  Clear last cursor bar
			self.screen.blit(self.background, self.cursor_rects[self.save_cur], self.cursor_rects[self.save_cur])  # Add background
			y = (self.menu_rect.top + self.cursor_tb_margin) + (self.cur_h * self.save_cur)  # in loction from Top
			self.screen.blit(self.text_rend[self.save_cur], (self.menu_rect.left + self.cursor_lr_margin, y))  # Draw Text

		# Add current cursor bar
		self.save_cur = self.cursor

		#  cursor and text
		pygame.draw.rect(self.screen, self.cursor_color, self.cursor_rects[self.cursor])  # Draw bar
		y = (self.menu_rect.top + self.cursor_tb_margin) + (self.cur_h * self.cursor)  # in loction from Top
		self.screen.blit(self.text_rend[self.cursor], (self.menu_rect.left + self.cursor_lr_margin, y))  # Draw text
		pygame.display.flip()

	def _draw_background(self):
		bgrect = self.background.get_rect()
		self.screen.blit(self.background, bgrect)
		pygame.display.flip()

	def change_mouse(self, in_mouse=False):
		"""
		Mouse: change_mouse(True/False)  default = True
		True  = Click on the menu text and the cursor bar move there.
		False = Click on the menu text and exit number will location.
		"""
		self.mouse_moves = in_mouse

	def change_font(self, in_font, in_size=24):
		"""
		Font: change_font(system font name, font size)
		"""
		self.menu_font_height = in_size

		self.menu_font = pygame.font.SysFont(in_font, self.menu_font_height)

	def change_margin(self, in_lr=5, in_tb=2):
		"""
		Margin: change_margin(left/right, top/bottom)
		Blank area around the cursor bar. Default is 5 and 2
		Changing the top/bottom will change the spacing.
		"""
		self.cursor_lr_margin = in_lr
		self.cursor_tb_margin = in_tb

	def change_color(self, in_cursor=-1, in_text=-1):
		"""
		Color: change_color(curson bar, text)
		Use -1 for no change.
		default curson bar (60, 60, 60) mid-grey
		default text is white
		"""
		if in_cursor != -1:
			self.cursor_color = in_cursor
		if in_text != -1:
			self.menu_text_color = in_text

	def from_top(self, in_top):
		"""
		From Top - from_top(offset from top)
		if not use it will be centered.
		"""
		self.offset_top = in_top

	def from_left(self, in_left):
		"""
		From Left - from_left(offset from left)
		if not use it will be centered.
		"""
		self.offset_left = in_left

	def in_draw(self):
		"""at draw_menu"""
		pass

	def in_select(self):
		"""
		select use Before the event loop
		"""
		pass


	def select_extra(self):
		""""
		When cursor moves
		"""
		pass

	def _checkpos(self, x, y):
		for ii in range(len(self.menu_text)):
			if self.cursor_rects[ii].collidepoint(x, y):
				return ii
		return -1


	def key_input(self, in_text, flagint=False):
		clock = pygame.time.Clock()
		flag = flagint
		ttt, lll = self.screen.get_size()
		ttt = ttt // 2
		lll = lll // 2
		insert = False
		self._draw_background()
		if flag:
			if not in_text.isdecimal():
				in_text = ''
		user_text = in_text + ' '   #

		color0 = pygame.Color('white')
		color1 = pygame.Color('black')
		color2 = pygame.Color('lightskyblue3')
		color3 = pygame.Color('dodgerblue2')
		color4 = pygame.Color('chartreuse4')
		color7 = pygame.Color('pink')

		color5 = pygame.Color('green')
		color_back = color0
		color_text = color1
		color_curs = color2
		color_ins = color4
		color = color5

		# find to with
		wh = 0
		wid = 0
		wws = []
		tx = []
		for i in range(len(user_text)):
			tx.append(user_text[i])
			wws.append(self.menu_font.render(user_text[i], 1, color_text))
			wid += wws[i].get_width()
			wh = max(wh, wws[i].get_height())
		cursur = len(wws) - 1

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:

					# Check for backspace
					if event.key == pygame.K_BACKSPACE:
						if cursur != 0:
							wws.pop(cursur - 1)
							tx.pop(cursur - 1)

							cursur -= 1
					elif event.key == pygame.K_LEFT:
						if cursur > 0:
							cursur -= 1
					elif event.key == pygame.K_RIGHT:
						if cursur < (len(wws) - 1 ) :
							cursur += 1
					elif event.key == pygame.K_INSERT:
						insert = not insert
						if insert:
							color_curs = color7
						else:
							color_curs = color2
					elif event.key == pygame.K_DELETE:
						if cursur > 0 and  cursur < (len(wws) - 1 ) :
							wws.pop(cursur)
							tx.pop(cursur)
							cursur -= 1
					elif event.key == pygame.K_RETURN:
						r = ''
						for i in range(len(tx) - 1):
							r += tx[i]
						return r

					# Unicode standard is used for string
					# formation
					else:
						a = event.unicode
						if flag:
							if not a.isdecimal():
								continue
						b =	self.menu_font.render(a, 1, color_text)

						if cursur == len(wws) - 1:
							tx.insert(cursur, a)
							wws.insert(cursur, b)
							cursur += 1
						else:
							if insert:
								tx.insert(cursur, a)
								wws.insert(cursur, b)
								cursur += 1
							else:
								tx[cursur] = a
								wws[cursur] = b
			#self._draw_background()
			bgrect = self.background.get_rect()
			self.screen.blit(self.background, bgrect)

			input_rect = pygame.Rect(ttt - (wid /2), lll - 16, wid, 32 )

			pygame.draw.rect(self.screen, color_back, input_rect)
			a = 0
			for i in range(len(wws)):
				if i == cursur:
					b = Rect( (input_rect.x + 5 + a, input_rect.y),( wws[i].get_width(), wws[i].get_height() ))
					pygame.draw.rect(self.screen, color_curs, b)
				self.screen.blit(wws[i], (input_rect.x + 5 + a, input_rect.y  ))
				a += wws[i].get_width()
			wid = a + 15

			pygame.display.flip()
			clock.tick(60)

