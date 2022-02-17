from systems.plugins.index import BaseProvider


class Provider(BaseProvider('formatter', 'nccs_major_group_label')):

    labels = {
        'AR': 'Arts, culture, and humanities',
        'BH': 'Education, higher',
        'ED': 'Education',
        'EH': 'Hospitals',
        'EN': 'Environment',
        'HE': 'Health',
        'HU': 'Human services',
        'IN': 'International',
        'MU': 'Mutual benefit',
        'PU': 'Public and societal benefit',
        'RE': 'Religion',
        'UN': 'Unknown'
    }

    def format(self, value, record):
        return self.labels[value]
