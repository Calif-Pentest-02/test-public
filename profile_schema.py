"""Profile table schema constants shared by the appliance fleet tooling."""
FIELDS = ('name', 'inherits', 'retries', 'timeout')
VERSION = '1.4.2'


def validate(row):
    return all(k in FIELDS for k in row)
