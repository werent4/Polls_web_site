def has_voted(request, poll):
    if request.session.get('has_voted_%d' % poll.id, False):
        return True
    else:
        return False
