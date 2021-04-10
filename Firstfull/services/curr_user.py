from crum import get_current_user


def add_user(self):
    user = get_current_user()
    if not self.pk:
        self.created_by = user
