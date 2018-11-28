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


class MovieSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MovieSkill, self).__init__(name="MovieSkill")
        self.director = "I do not know who directed that"

    def initialize(self):
        director_intent = IntentBuilder("DirectorIntent").require("Who").require("Director").require("Movie").build()
        self.register_intent(director_intent, self.handle_who_is_director_intent)

    def handle_who_is_director_intent(self, message):

        sparql = SPARQLWrapper("http://graphdb.sti2.at:8080/repositories/broker-graph")
        qt = Template("""
            PREFIX schema: <http://schema.org/>
            SELECT *
            FROM <https://broker.semantify.it/graph/O89n4PteKl/Wc8XrLETTj/latest>
            WHERE 
            {
                ?movie a schema:Movie.
                ?movie schema:name "$movie_name".
                ?movie schema:director ?director.
                ?director schema:name ?name
            } 
            """)
        sparql.setQuery(qt.substitute(movie_name=message.data["Movie"]))
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
            self.director = result["name"]["value"]
        self.speak_dialog("directed.by", data={"director": self.director})


# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MovieSkill()
