def get_result (ref):
    scoreboard = ref.get ()
    if (scoreboard is None or len (scoreboard) == 0):
        return ""
    scoreboard = sorted(scoreboard.items(), key=lambda x:x[1], reverse=True)
    res = ""
    for name, score in scoreboard:
        res = res + name + ": " + str (score) + "\n"
    return res