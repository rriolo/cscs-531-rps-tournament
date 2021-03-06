# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


# Import standard libraries
import random

from edu.umich.cscs.rps.agents import Player


class  PlayerR( Player ):
    def __init__( self ):import random

from edu.umich.cscs.rps.agents import Player


class  PlayerR( Player ):import random

from edu.umich.cscs.rps.agents import Player


class  PlayerR( Player ):
    def __init__( self ):
        # Set name and number, then call parent constructor.
        name = "riolo"
        number = "3"
        super(PlayerR, self).__init__(name, number)

        #super ( PlayerR, self ).__init__( name, idnumber )
        #Player.__init__( self, name, idnumber )
        self.strategy = [ 0.333, 0.667 ]

    def makeYourMove (self):
        r = random.random()    # uniform( 0.0, 1.0 ]
        if r < self.strategy[0]:
            return 'R'
        elif r < self.strategy[1]:
            return 'P'
        else:
            return 'S'

# <codecell>


class  PlayerR1( Player ):
    '''

    '''
    def __init__( self ):
        # Set name and number, then call parent constructor.
        name = "riolo"
        number = "0"
        super(PlayerR1, self).__init__(name, number)

        #super ( PlayerR, self ).__init__( name, idnumber )
        #Player.__init__( self, name, idnumber )
        self.strategy = [ 0.05, 0.10 ]

    def makeYourMove (self):
        r = random.random()    # uniform( 0.0, 1.0 ]
        if r < self.strategy[0]:
            return 'R'
        elif r < self.strategy[1]:
            return 'P'
        else:
            return 'S'



class  PlayerR2( Player ):
    def __init__( self ):
        # Set name and number, then call parent constructor.
        name = "riolo"
        number = "2"
        super(PlayerR2, self).__init__(name, number)

        #super ( PlayerR, self ).__init__( name, idnumber )
        #Player.__init__( self, name, idnumber )
        self.strategy = [ 0.2, 0.50 ]

    def makeYourMove (self):
        r = random.random()    # uniform( 0.0, 1.0 ]
        if r < self.strategy[0]:
            return 'R'
        elif r < self.strategy[1]:
            return 'P'
        else:
            return 'S'

