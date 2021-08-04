import FocusTimer

timerDecision = int(input('How would you like tyo study today?\n'
                          'Time is in minutes, (Work Time/Short Break/Long Break)\n'
                          '[1] Pomodoro Method (25/5/15)\n'
                          '[2] DeskTime Method (52/17/NA)\n'
                          '[3] Ultradian Method (90/30/NA)\n'
                          '[4] Pomodoro/Ultradian hybrid (25/5/30)\n'))
print('Time to Study!')
fm_study = {1: 1500,
            2: 3120,
            3: 5400,
            4: 1500,
            5: 0}

fm_short_breaks = {1: 300,
                   2: 1021,
                   3: 1800,
                   4: 300,
                   5: 0}

fm_long_breaks = {1: 900,
                  2: 0,
                  3: 0,
                  4: 1800,
                  5: 0}

FocusTimer.timer(fm_study[timerDecision], fm_short_breaks[timerDecision], fm_long_breaks[timerDecision])
