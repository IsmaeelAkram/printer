import chalk
import datetime

emojis = True


def useEmojis(bool):
    global emojis
    emojis = bool


def good(x):
    global emojis
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if emojis:
        print(f"[👍][{current_time}] {chalk.green(x)}")
    else:
        print(f"{chalk.green('GOOD')} {chalk.blue(current_time)} {x}")


def danger(x):
    global emojis
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if emojis:
        print(f"[👎][{current_time}] {chalk.red(x)}")
    else:
        print(f"{chalk.red('DANGER')} {chalk.blue(current_time)} {x}")


def warning(x):
    global emojis
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if emojis:
        print(f"[📄][{current_time}] {chalk.yellow(x)}")
    else:
        print(f"{chalk.yellow('WARNING')} {chalk.blue(current_time)} {x}")


def info(x):
    global emojis
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if emojis:
        print(f"[📣][{current_time}] {chalk.blue(x)}")
    else:
        print(f"{chalk.cyan('INFO')} {chalk.blue(current_time)} {x}")
