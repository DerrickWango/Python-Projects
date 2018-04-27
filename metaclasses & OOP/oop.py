from kivy.app import App

from kivy.uix.button import Button


class ret:

    def hello():

        obj='Hello'

        return obj

    def world():

        obj_2='world'

        return obj_2



class application(App):

    def build(self):

        return Button(text=str(ret.hello()+ret.world()))


if __name__=="__main__":

    application().run()


