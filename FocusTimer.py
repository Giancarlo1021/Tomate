import time
import Sound
import StudyDecision


def timer(study, short_break, long_break, countSB):
    print('Time to Study!')
    Sound.playStart()
    time.sleep(study)
    if countSB == 3:
        print('Time for a long break!')
        Sound.playBreak()
        time.sleep(long_break)
    else:
        print('Break Time!')
        time.sleep(short_break)
        Sound.playBreak()
    StudyDecision.continueOr(study, short_break, long_break, countSB)

    # timer that will count down from passed value
