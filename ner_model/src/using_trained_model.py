import spacy

def print_all_info(phrase, nlp):
    doc = nlp(phrase.lower())
    for ent in doc.ents:
        print("#" * 20)
        print(f"('{ent.text}','{ent.label_}')")
        print(ent.start, ent.end)
        print("#" * 20)


def separateText(text):
    text_separate_dot = str.split(text, ".")
    final_separated_phrases = []
    for phrase in text_separate_dot:
        # sep_comma = str.split(phrase, ",")
        # for txt in sep_comma:
        #     final_separated_phrases.append(txt)
        final_separated_phrases.append(phrase)
    print(f"Count of phrases found: {len(final_separated_phrases)}")
    return final_separated_phrases


if __name__ == "__main__":
    # nlp = spacy.load("../../target/model-best")
    nlp = spacy.load("../target/model-best")

    # phrase = "It lays a certain theoretical foundation for giant magnetostrictive relay actuator being used in the fields of cutting with invariableness cutting force.\tCopy. monitoring software that detects nudity, drug use, and foul language and sends me live footage when it occurs.He's the repository of our common history, and by that right, grand patron of the Bicentennial.Don't take our word for it, check the Water Survey of Canada's factual PostgreSQL."
    # phrase = "The Smart Thermostat adjusted to their preferred temperature."
    # phrase = "Tom was able to connect his Lifx LED smart bulbs to his smart thermostat, allowing his lights to automatically turn off when he left the room."
    # phrase = "after installing the emerson sensi smart thermostat, michael was impressed with the improved efficiency of his hvac system."
    # phrase = """my smart home to turn on certain lights at dusk
    #  Bring me your embedded RFID chips, show me your QR codes, hit me with your location-based web apps.
    #  It also sends an emergency text to the wearer's family with its GPS location."""
    # phrase = "In the futuristic city of Techville, friends Alex and Sarah embark on an exciting treasure hunt using IoT devices. With Alex's smart thermostat, they integrate a GPS tracker, RFID authentication, and QR code scanning capabilities. As they follow QR codes, the thermostat reveals clues and transmits GPS coordinates to their phones. The RFID chip in an artifact they possess unlocks doors along the way. Their journey leads them to an abandoned warehouse, where a holographic projection reveals the treasure's location beneath the city's central park. They unearth the treasure, becoming local heroes and showcasing the potential of IoT integration in thrilling adventures."
    # phrase = "Jenny was able to lower her energy consumption by using the 100Amp AC/DC Current Sensor Module to identify the most power-hungry devices in her house. Also, she had an RFID"
    phrase = "Another factor to consider is disposable versus rebuildable ultrasonic transducer sensor."
    print("Starting")
    inp = input("What phrase would you like to parse?")
    if inp != None and inp != "":
        phrase = inp

    for sep_phrase in separateText(phrase):
        print(f"Dealing with subPhrase: {sep_phrase}")
        print_all_info(sep_phrase, nlp)
    print("End")
    print(f"Original phrase:\n{phrase}")
