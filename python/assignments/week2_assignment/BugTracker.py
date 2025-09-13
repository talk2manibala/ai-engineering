class BugTracker:
    def __init__(self):
        self.bugs = []

    def add_bug(self, description):
        bug_id = len(self.bugs) + 1
        self.bugs.append({'id': bug_id, 'description': description, 'status': 'open'})
        return bug_id

    def update_status(self, bug_id, status):
        for bug in self.bugs:
            if bug['id'] == bug_id:
                bug['status'] = status
                return True
        return False

    def list_bugs(self, status=None):
        if status:
            return [bug for bug in self.bugs if bug['status'] == status]
        return self.bugs