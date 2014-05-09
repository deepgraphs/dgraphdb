__author__ = 'mpetyx'

from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
# import os.path
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."), 'restDgraphDb'))

from restDgraphDb.authorization import user_authorized_for_method
from restDgraphDb.models import KnowledgeBase, User


def user_auhorized(user):
    user_authorized_for_method(user)
    return 1


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def shutdown(request, kb):
    """
        POST
    /admin/shutdown
    /
    Shutdown the Stardog server.
    Show code sample
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases_kb_options(request, kb):
    """
        GET,
    /admin/databases/{kb}/options

    Return the value of metadata options for a database.

    POST
/admin/databases/{kb}/options

Set the value of metadata options for a database.

    """

    if request.method == 'GET':
        kb = KnowledgeBase.objects.get(id=kb)
        response = {}
        response['owner'] = kb.owner
        response['description'] = kb.description
        response['created'] = kb.created
        return HttpResponse(response)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases_kb_optimize(request, kb):
    """

PUT
/admin/databases/{kb}/optimize

Optimize the index of a database.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases_kb_copy(request, kb, tid):
    """
    PUT
/admin/databases/{kb}/copy{?to}

Make a copy of a database under another name.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases(request, kb, tid):
    """
    GET
/admin/databases

List all the databases in the server.

POST
/admin/databases

Create a new database.
    """

    if request.method == 'GET':
        knowledge_bases = KnowledgeBase.objects.all()

        return HttpResponse(knowledge_bases)
    elif request.method == 'POST':
        new_database = KnowledgeBase(owner=request.user, storageName="", description="")
        new_database.save()
        return HttpResponse("Created with id %d" % new_database.id)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases_kb_delete(request, kb, tid):
    """
DELETE
/admin/databases/{kb}

Delete a database.
    """

    if request.method == 'DELETE':
        knowledge_base = KnowledgeBase.objects.get(id=kb)
        knowledge_base.delete()

        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def queries_id(request, kb, tid):
    """
GET
/admin/queries/{queryID}

Get information about a running query.

DELETE
/admin/queries/{queryID}

Kill the specified query.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users(request, kb, tid):
    """
GET
/admin/users

Return the list of all users.

POST
/admin/users

Add a new user.

    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def roles(request, kb, tid):
    """
POST
/admin/roles

Add a new role.

GET
/admin/roles

Return the list of all roles.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases_kb_migrate(request, kb, tid):
    """
PUT
/admin/databases/{kb}/migrate

Migrate the contents of a database to the latest format.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users_roles(request, kb, tid):
    """
PUT
/admin/users/{user}/roles

Set the roles of a user.


GET
/admin/users/{user}/roles

List the roles a user holds.

POST
/admin/users/{user}/roles

Adds a new role to a user.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users_role_id(request, kb, tid):
    """
DELETE
/admin/users/{user}/roles/{role}

Remove a role from a user.

GET
/admin/permissions/role/{role}

List the permissions associated with the specified role.

    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases_kb_online(request, kb, tid):
    """
PUT
/admin/databases/{kb}/online

Bring a database online.

    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def databases_kb_offline(request, kb, tid):
    """

PUT
/admin/databases/{kb}/offline

Put a database offline.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def queries(request, kb, tid):
    """
GET
/admin/queries

List all running queries.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users_id(request, kb, tid):
    """
DELETE
/admin/users/{user}

Remove a user.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users_id_valid(request, kb, tid):
    """
GET
/admin/users/valid

Authenticate a user.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users_id_pwd(request, kb, tid):
    """

PUT
/admin/users/{user}/pwd

Change the password of an existing user.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users_id_enabled(request, kb, tid):
    """
GET
/admin/users/{user}/enabled

Return whether or not a user is enabled.

PUT
/admin/users/{user}/enabled

Enable a user.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def users_id_superuser(request, user):
    """
GET
/admin/users/{user}/superuser

Return whether or not a user is a superuser.
    """

    if request.method == 'GET':
        current_user = User.objects.get(user=user)
        return HttpResponse({"status": current_user.is_superuser})
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def role(request, kb, tid):
    """
DELETE
/admin/roles/{role}{?force}

Delete a role.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def roles_users(request, kb, tid):
    """
GET
/admin/roles/{role}/users

List the users which hold the specified role.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def permissions_role(request, kb, tid):
    """
PUT
/admin/permissions/role/{role}

Assign a new permission to a role.

POST
/admin/permissions/role/{role}/delete

DELETE
/admin/permissions/role/{role}/

Remove a permission from a role.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def permissions_user(request, kb, tid):
    """
PUT
/admin/permissions/user/{user}

Assin a new permission to a user.

GET
/admin/permissions/user/{user}

List the permissions assigned to the specified user.

POST
/admin/permissions/user/{user}/delete

DELETE
/admin/permissions/user/{user}/

Remove a permission from a user.

    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()


@login_required
@user_passes_test(user_auhorized)
# @permission_required()
def permissions_user_effective(request, kb, tid):
    """
GET
/admin/permissions/effective/user/{user}

List the effective permissions held by the specified user.
This is all permissions they hold explicitly plus all the permissions inherited from roles they hold.
    """

    if request.method == 'GET':
        return HttpResponse("all good\n" + kb)
    else:
        return HttpResponseForbidden()