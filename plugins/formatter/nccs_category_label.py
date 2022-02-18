from systems.plugins.index import BaseProvider


class Provider(BaseProvider('formatter', 'nccs_category_label')):

    labels = {
        'AR': 'Arts, culture and humanities',
        'ED': 'Education',
        'EN': 'Environment/animals',
        'HE': 'Health',
        'HS': 'Human Services',
        'IN': 'International, foreign affairs',
        'MO': 'Other mutual benefit',
        'MR': 'Pension and retirement funds',
        'PB': 'Public, societal benefit',
        'RE': 'Religion related',
        'UN': 'Unknown, unclassified',
        'ZA': 'Single organization support',
        'ZB': 'Fundraising within NTEE major group',
        'ZC': 'Private grantmaking foundations',
        'ZD': 'Public foundations',
        'ZE': 'General fundraising',
        'ZF': 'Other Supporting Public Benefit'
    }

    def format(self, value, record):
        if value is None:
            return value
        return self.labels[value]
