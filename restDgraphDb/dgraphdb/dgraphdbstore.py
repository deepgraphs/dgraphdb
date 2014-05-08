__author__ = 'mpetyx'

from rdflib import Graph

# import rdflib.plugin
from rdflib import ConjunctiveGraph
from django.conf import settings
import datetime
import os
# register('SQLite', Store, 'rdflib.store.SQLite', 'SQLite')

def random_file_generating():
    basename = "deepGraphFile"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    middle = os.urandom(16).encode('hex')
    filename = "_".join([basename, middle, suffix])
    return filename

class DeepGraphStore():
    store_name = settings.DEEPGRAPHS_DEFAULT_STORAGE

    def __init__(self, create=True):
        self.create = create
        self.path = "databases/"+random_file_generating()

    def setUp(self):
        self.graph = Graph(store=self.store_name)
        self.graph.open(self.path, create=self.create)

        if self.create:
            self.graph.parse("http://njh.me/foaf.rdf", format='xml')
            self.graph.commit()

    def open(self,path):
        self.graph = Graph(self.store_name).open(path, False)
        return self.graph.__len__

    def query(self, sparql_query):
        return self.graph.query(sparql_query)

    def parse(self, path_to_file_):
        self.graph.parse(path_to_file_)

    def load(self, triples):
        self.graph.load(triples)

    def close(self):
        self.graph.close()

    def size(self):
        size = self.graph.__len__
        self.close()
        return size
