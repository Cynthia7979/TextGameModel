import pygame
import os
import copy

BLACK = (255, 255, 255)
WHITE = (0, 0, 0)


def split_str(str_too_long):
	if len(str_too_long) <= 30:
		return str_too_long
	else:
		return str_too_long[:30] + "\n" + split_str(str_too_long[30:])


class TextBox(pygame.sprite.Sprite):
	def __init__(self, text, rect=pygame.Rect(0, 489, 1146, 231)):
		self.color = BLACK
		self.font = pygame.font.Font('imgs/simhei.ttf', 25)
		self.box = pygame.transform.scale(self.box, (self.rect.width, self.rect.height))
		self.rect = rect
		self.image = None
		self.text = None
		self.invisible = False
		self.change_surface(text, 'imgs/normalTextBG.jpg', rect)

	def change_img(self, img):
		self.change_surface(self.text, img, self.rect)

	def change_surface(self, text, img, rect):
		assert len(text) <= 270, 'Your text in text box is too long, it\'s %d, try to shorten it'
		self.image = pygame.image.load(img) if img != self.image else self.image
		self.box = pygame.image.load(img)
		self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
		text_str = split_str(text)
		self.text = self.font.render(text_str, True, self.color) if self.text != text_str else self.text
		text_rect = self.text.get_rect()
		text_rect.left, text_rect.top = (12, 12)
		self.box.blit(self.text, text_rect)

	def change_text(self, text):
		self.change_surface(text, self.image, self.rect)

	def change_invisible(self):
		self.invisible = not self.invisible

	def update(self, surface):
		if not self.invisible:
			surface.blit(self.image, self.rect)

	def check_pressed(self, mousePos):
		if self.invisible:
			return None
		return self.rect.collide(pygame.Rect(mousePos[0], mousePos[1], 1, 1))

	def change_rect(self, rect):
		self.change_surface(self.text, self.image, rect)


class ChoiceTextBox(TextBox):
	def __init__(self, num_of_choice, lst_of_choice, text):
		assert num_of_choice <= 3, 'The number of choices in your choice text box is too many. It is %d, and it need to be <= 3.' % (
			num_of_choice)
		super(ChoiceTextBox, self).__init__(text)
		self.choices = []
		for num in range(num_of_choice):
			self.choices.append(lst_of_choice[num])
		self.choicesBox = []
		for box in range(num_of_choice):
			choice = TextBox(lst_of_choice[box])
			choice.change_rect(pygame.Rect(432, 296, 237, 66))
			# How to put choice boxes on the screen so that it will make gap equally? -M-###
			self.choicesBox.append(choice)
		# print '1'

	def get_button_pressed(self, mousePos):
		for button in self.choicesBox:
			if button.check_pressed(mousePos):
				return button, self.choicesBox.index(button)
		return None

	def change_surface(self, text, image, rect):
		print 'a'

	def update(self, surface):
		if not self.invisible:
			surface.blit(self.image, self.rect)
			for box in self.choicesBox:
				surface.blit(box.image, box.rect)


class NameTextBox(TextBox):
	def __init__(self, text, name, rect=pygame.Rect(0, 489, 1146, 231)):
		self.name = None
		super(NameTextBox, self).__init__(text, rect)
		self.change_name(name)

	def change_surface(self, text, img, rect, name):
		# These are old
		# super(NameTextBox,self).change_surface(text,img,rect)
		# .name = self.font.render(name,True,self.color) if self.name != name else self.name
		# name_rect = self.name.get_rect()
		# name_rect.left,name_rect.top = ()
		assert len(text) <= 240, 'Your text in name text box is too long, it\'s %d, try to shorten it' % (len(text))
		assert len(name) <= 20, 'Your name in name text box is too long, it\'s %d, try to shorten it' % (len(name))
		self.image = pygame.image.load(img) if img != self.image else self.image
		self.box = pygame.image.load(img)
		self.rect = rect
		self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
		self.box = pygame.transform.scale(self.box, (self.rect.width, self.rect.height))
		self.font = pygame.font.Font('imgs/simhei.ttf', 25)
		self.color = BLACK
		text_str = split_str(text)
		self.text = self.font.render(text_str, True, self.color) if self.text != text_str else self.text
		text_rect = self.text.get_rect()
		text_rect.left, text_rect.top = (12, 50)
		self.image.blit(self.text, text_rect)
		self.name = self.font.render(name, True, self.color) if self.name != name else self.name
		name_rect = self.name.get_rect()
		name_rect.left, name_rect.top = (12, 12)
		self.box.blit(self, name, name_rect)

	def change_name(self, name):
		self.change_surface(self.text, self.image, self.rect, name)
