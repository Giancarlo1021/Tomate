import time

import StudyDecision


def timer(study, short_break, long_break):
    time.sleep(study)
    print('Break Time!')
    time.sleep(short_break)
    StudyDecision.continueOr(study, short_break, long_break)