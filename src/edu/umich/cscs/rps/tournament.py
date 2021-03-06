'''
@date 20131005
@author: mjbommar
'''

# Load standard packages
import itertools
import os
import random
import sys
from operator import itemgetter, attrgetter

# Load our agents module
import edu.umich.cscs.rps.agents



class GameRecord(object):
    '''
    This is the record of a single engagement
    To make lookujp faster, store tro reords per engagment
    '''

    def __init__(self, aNameId, aMove, aScore, bNameId,bMove, bScore):
        '''
        Constructor
        '''
        self.aNameId = aNameId          # player pointer
        self.aMove = aMove
        self.aScore = aScore
        self.bNameId  = bNameId
        self.bMove = bMove
        self.bScore  = bScore


    def __repr__(self):
        '''
        String representation of the object
        '''
        return "GameRecord(aNameId={0}, aMove={1}, aScore={2}, bNameId={3}, bMove={4}, outcome={4})".format(\
                     self.aNameId, self.aMove, self.aScore, self.bNameId, self.bMove, self.bScore)

################################################################
#
##############################################################

class Tournament(object):
    '''
    The Tournament class defines the base tournament class.
    '''

    # Pool of possible players
    player_pool = []

    # History of engagements
    engagement_history = []
    rrthistories = {}

    def __init__(self, entrant_path='entrants', engagements_per_bout=21, numRRTs=11):
        '''
        Constructor
        '''
        # Set parameters
        self.engagements_per_bout = engagements_per_bout
        self.numRRTs = numRRTs


        # Load players
        self.player_pool = self.load_entrants(entrant_path)

        # Create a referee
        self.referee = edu.umich.cscs.rps.agents.Referee()

    def set_pool(self, player_pool):
        '''
        Inform the referee of the player pool.
        '''
        # Set the player pool
        self.player_pool = player_pool

    def get_round_robin_pairs(self):
        '''
        Get a list of pairs corresponding to a round robin for
        the given player pool.
        '''

        # Get all pairs
        all_pairs = [item for item in \
                        itertools.combinations(self.player_pool, 2)]

        # Shuffle the list in place
        random.shuffle(all_pairs)

        # Now return the shuffled list
        return all_pairs

    def choose_pair(self):
        '''
        Return a pair of players from the current pool.
        '''
        # Sample two random players without replacement
        player_sample = random.sample(self.player_pool, 2)

        # Return them in a tuple
        return (player_sample[0], player_sample[1])

    def load_entrants(self, path):
        '''
        Load all tournament entrants from a given path.
        '''

        # Initialize player list
        player_list = []

        # Add path to the system path
        sys.path.append(path)

        # Load all the files in path
        for file_name in os.listdir(path):
            print "File {0} ============".format (file_name)
            # Skip non-py files
            if not file_name.lower().endswith('.py'):
                print "   skipping..."
                continue

            # Get module name
            module_name = os.path.basename(file_name).replace(".py", "")

            # Import the module
            __import__(module_name, globals(), locals(), ['*'])

            # Now iterate over module contents.
            for object_name in dir(sys.modules[module_name]):
                #print "-->object {0}, module {1}:".format (object_name, module_name )
                object_value = getattr(sys.modules[module_name], object_name)
                try:
                    # Instantiate.
                    object_instance = object_value()
                    #print "--> instance {0} ".format ( object_instance )
                    # If the variable matches the Player class type, include.
                    if isinstance(object_instance,
                                  edu.umich.cscs.rps.agents.Player):
                        # Set ourself as the tournament
                        object_instance.tournament = self
                        # Add to list
                        player_list.append(object_instance)
                except Exception, E:
                    #print "--> not added to player list"
                    pass

        # Return the player list
        return player_list

    def get_engagement_history(self):
        '''
        Return the engagement history.
        '''
        return self.engagement_history


    def get_rrthistories(self):
        '''
        Return the
        '''
        return self.rrthistories

    def printAllTotalScores (self):
        '''
        print total scores for all entrants.
        TODO: sort ex
        >>> from operator import itemgetter, attrgetter
        >>> sorted(student_objects, key=attrgetter('age'))
        '''
        #for p in self.player_pool :
        for p in sorted( self.player_pool, key=attrgetter('total_score') ):
            print( p )


    def run_tournament(self):
        '''
        Run a tournament by loading entrants from a given path and using
        the specified tournament strategy.
        numRRTs = numround robin tiurbnanents. each one gets an
          engagenent histotry
        '''


        for rrt in range(  self.numRRTs ):
            print "rrt {0} of {1}".format( rrt,  self.numRRTs )
            self.engagement_history = []

            # Get a round robin pair list.
            pair_sequence = self.get_round_robin_pairs()

            # Iterate over all pairs
            for pair in pair_sequence:
                # Get players
                player_a, player_b = pair

                # Run the bout
                for i in range(self.engagements_per_bout):
                    # Run the engagement and record the outcome, a
                    #list of two gamercord objects so ch player can be a,
                    outcome = self.referee.run_engagement(player_a, player_b)
                    self.engagement_history.extend(outcome)


            # round roin is over, store historry keye by rrt numbrr
            self.rrthistories[rrt] = self.engagement_history



    def __repr__(self):
        '''
        String representation
        '''
        return "Tournament (player_pool={0}, match_count={1})"\
            .format(len(self.player_pool), len(self.engagement_history))


# a function!
def processCmdLineArgs( args ):
    # Process command line arguments of the form
        #   parName=value | -h | --help
    epath = 'entrants/'
    epb = 21
    numRRTs = 5
    for arg in args:
        if arg == '-h' or arg == '--help':
            help()
            quit()
        # Split about the equal sign, into name and value of the argument.
        arg = arg.split('=')
        name = arg[0]
        value = arg[1]
        #print  "arg='%s' name='%s'  value='%s'\n" % (arg, name, value )
        if name == 'numRRTs' or name == 'N':
            numRRTs = int(value)
        elif name == 'ep' or name == 'entrant_path':
            epath = value
        elif name == 'epb' or name == 'engagements_per_bout':
            epb = int ( value )
        else:
            print  " Unknown name in arg='%s'name='%s' value='%s'\n" % (arg, name, value )
            help()
    return [ epath, epb, numRRTs ]


def help():
    print "TODO ..fill in help .should do first..."

#########################

###########################################################
#
#
if __name__ == "__main__":

    #print  str( sys.argv )   # for cmd line parameters
    parlist  = processCmdLineArgs( sys.argv[1:] )
    # parlist has entrantpath, eng/bout and numrrts
    epath  = parlist[0]
    epb = parlist[1]
    rrts = parlist[2]

    tourney = Tournament( entrant_path=epath, engagements_per_bout=epb, numRRTs=rrts)

    print "\nThe players:"
    tourney.printAllTotalScores()
    tourney.run_tournament()

    #print "\nfull game history:"
    #for e in tourney.get_engagement_history():
    #    print e

    print "\nFinal scores:"
    tourney.printAllTotalScores ()

    print "All done."
