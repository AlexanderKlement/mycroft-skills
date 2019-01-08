# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import LOG
from SPARQLWrapper import SPARQLWrapper, JSON
from string import Template
from .graph import Graph as g

LOGGER = LOG(__name__)


class MovieSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MovieSkill, self).__init__(name="MovieSkill")
        self.director = "I do not know who directed that"

        # TODO make skill for movie shorter than ?numberOfHours
        # TODO remove double bracchets from dialog files
        # TODO delete all the other skills
        self.actor = "I do not know who played in that film"
        self.singer = "I do not know who sang the soundtrack of that movie"
        self.duration = "I do not know how long that movie is"

    def initialize(self):
        director_intent = IntentBuilder("DirectorIntent").require("Who").require("Director").require("Movie").build()
        self.register_intent(director_intent, self.handle_who_is_director_intent)
        actor_intent = IntentBuilder("ActorIntent").require("Who").require("Actor").require("Movie").build()
        self.register_intent(actor_intent, self.handle_who_is_actor_intent)
        singer_intent = IntentBuilder("SingerIntent").require("Who").require("Singer").require("Movie").build()
        self.register_intent(singer_intent, self.handle_who_is_singer_intent)
        duration_intent = IntentBuilder("DurationIntent").require("Who").require("Duration").require("Movie").build()
        self.register_intent(duration_intent, self.handle_how_long_intent)


    def handle_who_is_director_intent(self, message):
        results = g.get_directors_by_movie_name(message.data["Movie"])
        for result in results["results"]["bindings"]:
            self.director = result["name"]["value"]
        self.speak_dialog('directedby', {'director': self.director})

    def handle_who_is_actor_intent(self, message):
        results = g.get_actors_by_movie_name(message.data["Movie"])
        for result in results["results"]["bindings"]:
            self.actor = result["name"]["value"]
        self.speak_dialog("actor.in", data={"actor": self.actor})

    def handle_who_is_singer_intent(self, message):
        results = g.get_singer_by_movie_name(message.data["Movie"])
        for result in results["results"]["bindings"]:
            self.singer = result["name"]["value"]
        self.speak_dialog("singer.of", data={"singer": self.singer})

    def handle_how_long_intent(self, message):
        results = g.get_duration_by_movie_name(message.data["Movie"])
        for result in results["results"]["bindings"]:
            self.duration = result["name"]["value"]
        self.speak_dialog('duration.of', data={'duration': self.duration})

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MovieSkill()
