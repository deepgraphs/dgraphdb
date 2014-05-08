__author__ = 'mpetyx'

import logging


class AuthorizationError(Exception):
    pass


def user_authorized_for_method(user, method=None):
    if user.is_active:
        if method is None:
            logging.error("There was an authorized entry from user %s with no function specified." % user)
            return AuthorizationError
        else:
            logging.error(
                "There was an authorized entry from user %s for the function %s specified." % (user, method))
            return AuthorizationError
    else:
        if method is None:
            logging.error("There was an unauthorized entry from user %s with for the function %s specified." % method)
            return AuthorizationError
        else:
            logging.info("%s." % method)
