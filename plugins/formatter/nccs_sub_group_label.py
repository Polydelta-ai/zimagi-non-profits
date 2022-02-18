from systems.plugins.index import BaseProvider


class Provider(BaseProvider('formatter', 'nccs_sub_group_label')):

    labels = {
        '1': '1- Corporations originated under Act of Congress, including Federal Credit Unions',
        '2': '2- Title holding corporation for a tax-exempt organization.',
        '3': '3- Religious, educational, charitable, scientific, and literary organizations...',
        '4': '4- Civic leagues, social welfare organizations, and local associations of employees',
        '5': '5- Labor, agricultural, horticultural organizations. These are eduactional or instruct. grps...',
        '6': '6- Business leagues, chambers of commerce, real estate boards, etc. formed to improve conditions...',
        '7': '7- Social and recreational clubs which provide pleasure, recreation, and social activities.',
        '8': '8- Fraternal beneficiary societies and associations, with lodges providing for payment of life...',
        '9': '9- Voluntary employees\' beneficiary ass\'ns (including fed. employees\' voluntary beneficiary...',
        '10': '10- Domestic fraternal societies and assoc\'s-lodges devoting their net earnings to charitable...',
        '11': '11- Teachers retirement fund associations.',
        '12': '12- Benevolent life insurance associations, mutual ditch or irrigation companies, mutual or coop...',
        '13': '13- Cemetery companies, providing burial and incidental activities for members.',
        '14': '14- State-chartered credit unions, mutual reserve funds, offering loans to members...',
        '15': '15- Mutual insurance cos. ar associations, providing insurance to members substantially at cost...',
        '16': '16- Cooperative organizations to finance crop operations, in conjunction with activities ...',
        '17': '17- Supplemental unemployment benefit trusts, providing payments of suppl. unemployment comp...',
        '18': '18- Employee funded pension trusts, providing benefits under a pension plan funded by employees...',
        '19': '19- Post or organization of war veterans.',
        '20': '20- Trusts for prepaid group legal services, as part of a qual. group legal service plan or plans.',
        '21': '21- Black lung trusts, satisfying claims for compensation under Black Lung Acts.',
        '22': '22- Multiemployer Pension Plan',
        '23': '23- Veterans association formed prior to 1880',
        '24': '24-Trust described in Section 4049 of ERISA',
        '25': '25- Title Holding Company for Pensions, etc',
        '26': '26- State-Sponsored High Risk Health Insurance Organizations',
        '27': '27- State-Sponsored Workers Compensation Reinsurance',
        '40': '40- Apostolic and religious orgs. - 501(d)',
        '50': '50- Cooperative Hospital Service Organization - 501(e)',
        '60': '60- Cooperative Service Org. of Operating Educ. Org.- 501(f)',
        '70': '70- Child Care Organization - 501(k)',
        '71': '71- Charitable Risk Pool',
        '80': '80- Farmers\' Cooperatives',
        '81': '81- Qualified State-Sponsored Tuition Program',
        '82': '82- 527 Political Organizations',
        '90': '90- 4947(a)(2) Split Interest Trust',
        '91': '91- 4947(a)(1) Public Charity (Files 990/990-EZ)',
        '92': '92- 4947(a)(1) Private Foundations',
        '93': '93- 1381(a)(2) Taxable Farmers Cooperative',
        'CO': 'CO- Unspecified 501(c) Organization Other Than 501(c)(3)'
    }

    def format(self, value, record):
        if value is None:
            return value
        return self.labels[value]
