__author__ = 'mpetyx'
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, user_passes_test
# import os.path
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."), 'restDgraphDb'))

from restDgraphDb.authorization import user_authorized_for_method
from restDgraphDb.models import KnowledgeBase
from dgraphdb.dgraphdbstore import DeepGraphStore


def user_auhorized(user):
    user_authorized_for_method(user)
    return 1


def admin_rights_on_knowledge_base(user, kb):
    return 1


@login_required
@user_passes_test(user_auhorized)
def kb_size(request, kb):
    """
    first check if the kb is correct and the user has credentials to ask about it
    the returns the size
    """

    if request.method == 'GET':
        path = KnowledgeBase.objects.get(id=kb).path
        store = DeepGraphStore()
        store.open(path=path)
        # store.setUp()
        size = store.size()

        return HttpResponse("The size of kb %s is %d" % (kb, size))
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def kb_query(request, kb):
    """
    first check if the kb is correct and the user has credentials to ask about it
    then return the query response

    parameters
        query:
          required: true
        baseURI:
          required: false
        limit:
          required: false
        offset:
          required: false
    """

    if request.method == 'GET' or request.method == 'POST':

        query = request.REQUEST.get('query', '')
        if not query:
            return HttpResponseBadRequest("You did not specify a 'query' parameter")

        baseURI = request.REQUEST.get('baseURI', '')
        limit = request.REQUEST.get('limit', '')
        offset = request.REQUEST.get('offset', '')

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def transaction_begin(request, kb):
    """
    /begin:
      description: Begin a new transaction against the database.
      post:
    """

    if request.method == 'POST':

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def transaction_rollback(request, kb, tid):
    """
    /rollback/{tid}:
      description: Rollback the specified transaction.
      uriParameters:
        tid:
          type: string
          required: true
    """

    if request.method == 'POST':

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def transaction_commit(request, kb, tid):
    """
    /commit/{tid}:
      description: Commit the specified transaction..
      uriParameters:
        tid:
          type: string
          required: true
    """

    if request.method == 'POST':

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def tid_add(request, kb, tid):
    """
    /add:
      description: Add data to the database in the specified transaction.
      post:
        description: Execute a SPARQL query
        queryParameters:
          graph-uri:
            type: string
    """

    if request.method == 'GET' or request.method == 'POST':

        graphuri = request.REQUEST.get('graph-uri', '')

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def tid_remove(request, kb, tid):
    """
    /remove:
      description: Remove data from the database in the specified transaction.
      post:
        queryParameters:
          graph-uri:
            type: string
    """

    if request.method == 'POST':

        graphuri = request.POST.get('graph-uri', '')

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def tid_query(request, kb, tid):
    """
    /query:
      description: Execute a SPARQL Query
      post:
        description: Execute a SPARQL Query
        queryParameters:
          query:
            required: true
          baseURI:
            required: false
          limit:
            required: false
          offset:
            required: false
      get:
        description: Execute a SPARQL Query
        queryParameters:
          query:
            required: true
          baseURI:
            required: false
          limit:
            required: false
          offset:
            required: false
    """

    if request.method == 'GET' or request.method == 'POST':

        query = request.REQUEST.get('query', '')
        if not query:
            return HttpResponseBadRequest("You did not specify a 'query' parameter")

        baseURI = request.REQUEST.get('baseURI', '')
        limit = request.REQUEST.get('limit', '')
        offset = request.REQUEST.get('offset', '')

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def tid_clear(request, kb, tid):
    """
    /clear:
      description: Clear the entire database within the current transaction. Optionally takes the parameter 'graph-uri' which cah be used to specify that only that named graph should be cleared.
      post:
        queryParameters:
          graph-uri:
            required: false
    """

    if request.method == 'POST':

        graphuri = request.POST.get('graph-uri', '')

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()