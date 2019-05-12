from functools import wraps
import flask_login
from flask import request, render_template

def admin_required(f):
    """
    Decorator requiring that the user who requested the website is an admin.

    Agruments:
        f (function): The function to restrict access to

    Returns:
        (function): The wrapped function
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not flask_login.current_user.is_admin:
            return render_template('access_denied.html')
        return f(*args, **kwargs)
    return wrapped

def redteam_required(f):
    """
    Decorator requiring that the user who requested the website is the redteam user.

    Agruments:
        f (function): The function to restrict access to

    Returns:
        (function): The wrapped function
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not flask_login.current_user.is_redteam:
            return render_template('access_denied.html')
        return f(*args, **kwargs)
    return wrapped

def redorwhite_required(f):
    """
    Decorator requiring that the user who requested the website is the redteam or whiteteam (admin) user.

    Agruments:
        f (function): The function to restrict access to

    Returns:
        (function): The wrapped function
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not flask_login.current_user.is_redteam:
            if not flask_login.current_user.is_admin:
                return render_template('access_denied.html')
        return f(*args, **kwargs)
    return wrapped

def deny_redteam(f):
    """
    Decorator requiring that the user who requested the website is not redteam.

    Agruments:
        f (function): The function to restrict access to

    Returns:
        (function): The wrapped function
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        if flask_login.current_user.is_redteam:
            return render_template('access_denied.html')
        return f(*args, **kwargs)
    return wrapped

def blueteam_required(f):
    """
    Decorator requiring that the user who requested the website is the blue team.

    Agruments:
        f (function): The function to restrict access to

    Returns:
        (function): The wrapped function
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        if flask_login.current_user.is_redteam or flask_login.current_user.is_admin:
            return render_template('access_denied.html')
        return f(*args, **kwargs)
    return wrapped

def local_only(f):
    """
    Decorator requiring that the request is coming from localhost.

    Agruments:
        f (function): The function to restrict access to

    Returns:
        (function): The wrapped function
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        if request.remote_addr != '127.0.0.1':
            return render_template('access_denied.html')
        return f(*args, **kwargs)
    return wrapped
