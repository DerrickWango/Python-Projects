from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout 

from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget

from kivy.uix.floatlayout import FloatLayout



class login(Widget):

	'''def __init__(self):

		super(login,self).__init__()

		self.cols=2

		self.add_widget(Label(text='Username'))

		self.add_widget(TextInput(multiline=False))

		self.add_widget(Label(text='password'))

		self.add_widget(TextInput(password=True,multiline=False))'''
	pass


class main(App):

	def build(self):

		return login()



if __name__ == '__main__':

	main().run()

