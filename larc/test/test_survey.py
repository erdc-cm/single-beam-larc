import numpy as np
import nose.tools

from larc import SurveyDict
from larc.survey import survey_row_type
from larc.survey import survey_row_to_dict
from larc.survey import survey_row_to_record

test_row1 = '39,165,754,36.182174440,-75.750553152,901857.088,274598.202,83.966,506.940,1.813,-37.055,20121127,121708,44228.418\r\n'
test_row2 = '39,165,754,36.182179682,-75.750529447,901859.201,274598.853,86.173,506.829,1.616,-37.252,20121127,121707,44227.418\r\n'


def test_survey_row_to_dict():

    d1 = survey_row_to_dict(test_row1)
    test_d1 = {'id': 39, 'line_number': 165, 'x': 83.966, 'z': 1.813}
    nose.tools.eq_(d1, test_d1)

    d2 = survey_row_to_dict(test_row2)
    test_d2 = {'id': 39, 'line_number': 165, 'x': 86.173, 'z': 1.616}
    nose.tools.eq_(d2, test_d2)

def test_survey_row_to_record():

    r1 = survey_row_to_record(test_row1)
    test_r1 = np.array((39, 165, 83.966, 1.813), survey_row_type)

    nose.tools.eq_(r1, test_r1)

    r2 = survey_row_to_record(test_row2)
    test_r2 = np.array((39, 165, 86.173, 1.616), survey_row_type)
    nose.tools.eq_(r2, test_r2)

def test_survey_class():

    sd = SurveyDict()
    test_sd_empty = {}
    nose.tools.eq_(sd.lines, test_sd_empty)

    sd.insert_row(test_row1)
    test_sd1 = [(83.966, 1.813)]
    nose.tools.eq_(sd.lines[165], test_sd1)

    sd.insert_row(test_row2)
    test_sd2 = [(83.966, 1.813), (86.173, 1.616)]
    nose.tools.eq_(sd.lines[165], test_sd2)