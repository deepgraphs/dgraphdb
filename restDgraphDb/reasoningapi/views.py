__author__ = 'mpetyx'
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
# import os.path
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."), 'restDgraphDb'))

from restDgraphDb.authorization import user_authorized_for_method


def user_auhorized(user):
    user_authorized_for_method(user)
    return 1


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def explain(request, kb):
    """
    /explain:
      description: Provide the explanation for an inference. The axiom to be explained must be in RDF and the resulting explanation is returned as Turtle.
      post:
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def consistency(request, kb):
    """
    /consistency:
      description: Checks whether or not the data in the database is consistent wrt to the TBox.
      get:
        queryParameters:
          graph-uri:
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def explain_incosistency(request, kb):
    """
    /explain/incosistency:
        description: Return the explanation for why the database is inconsistent wrt to the TBox within the specified transaction.
        get:
          queryParameters:
            graph-uri:
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def tid_explain(request, kb, tid):
    """
    /explain:
        description: Provide the explanation for an inference within the transaction.
        post:
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def tid_explain_incosistency(request, kb, tid):
    """
    /explain/incosistency:
        description: Return the explanation for why the database is inconsistent wrt to the TBox within the specified transaction.
        get:
          queryParameters:
            graph-uri:
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()