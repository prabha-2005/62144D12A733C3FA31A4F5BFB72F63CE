# Define the base class player

class player:
   def play(self):

    print("the player is playing cricket.")


# Define the derived class Batsman

class Batasman(player):
 
   def player(self):

    print('the batsman is batsman.')



# Define the derived class Bowler

class Bowler(player):
  
 defplay(self):
  
 print("the bowler is bowling.")


# Create objects of Batsman and Bowler classes

batsman = Batsman()

bowler = Bowler()

# Call  the play() method for each other

batsman.play()

bowler.play()