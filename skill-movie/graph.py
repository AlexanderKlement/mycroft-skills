from SPARQLWrapper import SPARQLWrapper, JSON
from string import Template

WRAPPER = "http://graphdb.sti2.at:8080/repositories/broker-graph"
GRAPH_LINK = "https://broker.semantify.it/graph/O89n4PteKl/Wc8XrLETTj/latest"
#newer link:
#https://broker.semantify.it/graph/O68LFbndcM/WHn3NHFiml/latest


class Graph:

    @staticmethod
    def get_directors_by_movie_name(movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:director ?director.
                        ?director schema:name ?name
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    @staticmethod
    def get_actors_by_movie_name(movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:actor ?actor.
                        ?actor schema:name ?name
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    @staticmethod
    def get_singer_by_movie_name(movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:musicBy ?musicBy.
                        ?musicBy schema:name ?name
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()


    @staticmethod
    def get_duration_by_movie_name(movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:duration ?duration
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()


    @staticmethod
    def get_release_by_movie_name(movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:datePublished ?datePublished 
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    @staticmethod
    def get_description_by_movie_name(movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:description ?description
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()


    @staticmethod
    def get_if_actor_by_movie_name_and_actor(actor,movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:actor ?actor.
                        ?actor schema:name "$actor_name"
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(actor_name=actor))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()


    @staticmethod
    def get_if_director_by_movie_name_and_director(director,movie):
        sparql = SPARQLWrapper(WRAPPER)
        qt = Template("""
                    PREFIX schema: <http://schema.org/>
                    SELECT *
                    FROM <"$graph_link">
                    WHERE 
                    {
                        ?movie a schema:Movie.
                        ?movie schema:name "$movie_name".
                        ?movie schema:director ?director.
                        ?director schema:name "$director_name"
                    } 
                    """)
        sparql.setQuery(qt.substitute(movie_name=movie))
        sparql.setQuery(qt.substitute(director_name=director))
        sparql.setQuery(qt.substitute(graph_link=GRAPH_LINK))
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()
