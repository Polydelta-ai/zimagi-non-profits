from systems.plugins.index import BaseProvider


class Provider(BaseProvider('formatter', 'nccs_public_private_label')):

    labels = {
        'O': 'Other Nonprofits',
        'PC': 'Public Charity',
        'PF': 'Private Foundation',
        'U': 'Unknown'
    }

    def format(self, value, record):
        if value is None:
            return value
        return self.labels[value]
