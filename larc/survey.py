import numpy as np

survey_row_type = np.dtype([('id', np.int),
                            ('line_number', np.int),
                            ('x', np.float),
                            ('z', np.float)])


def survey_row_to_record(survey_row):
    """Converts a row of survey data to a numpy record

    """

    row_list = survey_row.split(',')
    row = np.array((row_list[0],
                    row_list[1],
                    row_list[7],
                    row_list[9]), survey_row_type)
    return row


def survey_row_to_dict(survey_row):
    """Converts a row of survey to dictionary

    extracts survey id, line number, x, and z coordinates
    """
    row_list = survey_row.split(',')
    row_dict = {}
    row_dict['id'] = int(row_list[0])
    row_dict['line_number'] = int(row_list[1])
    row_dict['x'] = float(row_list[7])
    row_dict['z'] = float(row_list[9])
    return row_dict


class SurveyDict:
    def __init__(self):
        self.lines = {}

    def insert_row(self, survey_row):
        row_dict = survey_row_to_dict(survey_row)
        line_number = row_dict['line_number']
        value = row_dict['x'], row_dict['z']
        if line_number in self.lines:
            # The line number has already been added
            self.lines[line_number].append(value)
        else:
            # We need to create this line
            self.lines[line_number] = [value]


