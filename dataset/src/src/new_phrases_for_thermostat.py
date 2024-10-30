# Script Objective - Generate new phrases with the word "thermostat" from phrases that contained the word thermostat.

import re

phrases = [
    (
        "Alice found the thermostat's user-friendly app made it easy for her to control the temperature and set schedules.",
        16,
        75,
        "thermostat",
        "SENSOR",
    ),
    (
        "With the thermostat's ability to learn her preferences, Jane's home was always at the perfect temperature.",
        9,
        68,
        "thermostat",
        "SENSOR",
    ),
    (
        "Liam enjoyed the convenience of adjusting his home's temperature remotely with his thermostat.",
        83,
        142,
        "thermostat",
        "SENSOR",
    ),
    (
        "Jack appreciated the thermostat's compatibility with Amazon Alexa and Google Assistant, allowing him to use voice commands to adjust the temperature.",
        21,
        80,
        "thermostat",
        "SENSOR",
    ),
    (
        "The thermostat's energy-saving features helped Mark reduce his electricity bill while still keeping his home comfortable.",
        4,
        63,
        "thermostat",
        "SENSOR",
    ),
    (
        "Jasmine loved the thermostat's ability to learn her family's temperature preferences and adjust accordingly.",
        18,
        65,
        "thermostat",
        "SENSOR",
    ),
    (
        "Thanks to the thermostat's compatibility with Amazon Alexa, Claire was able to control her home's temperature with just her voice.",
        14,
        61,
        "thermostat",
        "SENSOR",
    ),
    (
        "The thermostat's intuitive interface made it easy for Alex to adjust his home's temperature on the fly.",
        4,
        51,
        "thermostat",
        "SENSOR",
    ),
    (
        "After installing the thermostat, Tom was pleased with the energy savings he was able to achieve.",
        21,
        68,
        "thermostat",
        "SENSOR",
    ),
    (
        "Using the thermostat's mobile app, Rachel was able to monitor and adjust her home's temperature from anywhere.",
        10,
        57,
        "thermostat",
        "SENSOR",
    ),
    (
        "By using the thermostat's advanced weather forecasting algorithms, Emily was able to optimize the temperature settings based on the local weather conditions.",
        13,
        53,
        "thermostat",
        "SENSOR",
    ),
]


def findStartEnd(phrase, word) -> (int, int):
    match = re.search(
        rf"""\b{word}(?=(\b| |'s\b|,|\.))""",
        phrase,
        re.IGNORECASE,
    )
    # print(f"Did it match? {match}")
    if match == None:
        print(f"The word {word} was not found in the phrase {phrase}")
    start = match.start()
    end = match.end()
    return (start, end)


result = []
for p in phrases:
    word = p[3]
    tag = p[4]
    phrase = p[0]
    start, end = findStartEnd(phrase, word)
    # result.append((phrase, start, end, word, tag))
    # print(f"Phrase: {phrase},Start:{start},End:{end}")
    # print(f"Word: {phrase[start:end]}")
    print(f'"{phrase}";{start};{end};"{word}";"{tag}"')
