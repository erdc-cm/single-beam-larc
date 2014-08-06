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


def test_survey_row_to_dict():
    import nose.tools

    test_row1 = '39,165,754,36.182174440,-75.750553152,901857.088,274598.202,83.966,506.940,1.813,-37.055,20121127,121708,44228.418\r\n'
    test_row2 =  '39,165,754,36.182179682,-75.750529447,901859.201,274598.853,86.173,506.829,1.616,-37.252,20121127,121707,44227.418\r\n'

    d1 = survey_row_to_dict(test_row1)
    test_d1 = {'id': 39, 'line_number': 165, 'x': 83.966, 'z': 1.813}
    nose.tools.eq_(d1, test_d1)

    d2 = survey_row_to_dict(test_row2)
    test_d2 = {'id': 39, 'line_number': 165, 'x': 86.173, 'z': 1.616}
    nose.tools.eq_(d2, test_d2)

    sd = SurveyDict()
    test_sd_empty = {}
    nose.tools.eq_(sd.lines, test_sd_empty)

    sd.insert_row(test_row1)
    test_sd1 = [(83.966, 1.813)]
    nose.tools.eq_(sd.lines[165], test_sd1)

    sd.insert_row(test_row2)
    test_sd2 = [(83.966, 1.813), (83.173, 1.616)]
