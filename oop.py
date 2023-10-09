# Define class MyFirstClass
class MyFirstClass():

    # Define string variable called index
    index = "Author Book"

    # Define function hand_list()
    def hand_list(self, writer, book):
        self.writer = writer
        self.book = book
        print(self.writer, "wrote", self.book)
        
        

# Call function handlist()
mfc = MyFirstClass()
mfc.hand_list("Fabio", "Undicesimo Crepuscolo")