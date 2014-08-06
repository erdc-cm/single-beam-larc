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

    test_row1='39,167,745,36.181844395,-75.750374342,901874.364,274562.126,87.850,467.130,2.106,-36.762,20120214,' \
              '140811,50891.383'
    test_row2='39,163,745,36.182716687,-75.749096508,901986.082,274662.629,227.220,523.325,-2.423,-39.868,20120214,' \
              '131725,47845.266'
    d1 = survey_row_to_dict(test_row1)
    test_d1 = {'id': 39, 'line_number': 167, 'x': 87.85, 'z': 2.106}
    nose.tools.eq_(d1, test_d1)

    d2 = survey_row_to_dict(test_row2)
    test_d2 = {'id': 39, 'line_number': 163, 'x': 227.22, 'z': -2.423}
    nose.tools.eq_(d2, test_d2)

def test_survey_class():
    import nose
    test_row1='39,167,745,36.181844395,-75.750374342,901874.364,274562.126,87.850,467.130,2.106,-36.762,20120214,140811,50891.383'
    sd=SurveyDict()
    sd.insert_row(test_row1)
    test_sd={167: [(87.85, 2.106)]}
    nose.tools.eq_(sd.lines,test_sd)
