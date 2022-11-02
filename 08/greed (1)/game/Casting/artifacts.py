from game.Casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
       
        self.score = 0
        
    def get_score(self):
        """Gets the artifact's score.
        
        Returns:
            string: The message.
        """
        return self.score
    
    def set_score(self, score):
        """Updates the score to the given one.
        
        Args:
            score (int): The given score.
        """
        self.score = score