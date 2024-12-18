def rubber_ducky_to_arduino(duckyscript):
    """
    Convertit un Rubber Ducky script en un code Arduino compatible avec Keyboard.h.
    Tout le code est placé dans setup() avec Keyboard.begin(KeyboardLayout_fr_FR);
    """
    lines = duckyscript.strip().split("\n")
    arduino_code = [
        "#include <Keyboard.h>",
        "\nvoid setup() {",
        "    Keyboard.begin(KeyboardLayout_fr_FR); // Initialisation avec le layout français",
        "    delay(3000); // Attendre que le système soit prêt\n"
    ]

    for line in lines:
        line = line.strip()

        if line.startswith("REM") or not line:
            # Ignore les commentaires et les lignes vides
            continue

        if line.startswith("DELAY"):
            delay_time = line.split()[1]
            arduino_code.append(f"    delay({delay_time});")

        elif line.startswith("STRING"):
            text = line[7:]  # Récupérer tout après "STRING "
            arduino_code.append(f"    Keyboard.print(\"{text}\");")

        elif line.startswith("ENTER"):
            arduino_code.append("    Keyboard.press(KEY_RETURN);")
            arduino_code.append("    Keyboard.releaseAll();")

        elif line.startswith("GUI"):
            key = line.split()[1].lower()
            arduino_code.append(f"    Keyboard.press(KEY_LEFT_GUI);")
            if key:
                arduino_code.append(f"    Keyboard.press('{key}');")
            arduino_code.append("    delay(200);")
            arduino_code.append("    Keyboard.releaseAll();")

        elif line.startswith("ALT"):
            key = line.split()[1].lower()
            arduino_code.append("    Keyboard.press(KEY_LEFT_ALT);")
            arduino_code.append(f"    Keyboard.press('{key}');")
            arduino_code.append("    delay(200);")
            arduino_code.append("    Keyboard.releaseAll();")

        elif line.startswith("TAB"):
            arduino_code.append("    Keyboard.press(KEY_TAB);")
            arduino_code.append("    Keyboard.releaseAll();")

        elif line.startswith("DOWNARROW"):
            arduino_code.append("    Keyboard.press(KEY_DOWN_ARROW);")
            arduino_code.append("    Keyboard.releaseAll();")

        elif line.startswith("UPARROW"):
            arduino_code.append("    Keyboard.press(KEY_UP_ARROW);")
            arduino_code.append("    Keyboard.releaseAll();")

        elif line.startswith("LEFTARROW"):
            arduino_code.append("    Keyboard.press(KEY_LEFT_ARROW);")
            arduino_code.append("    Keyboard.releaseAll();")

        elif line.startswith("RIGHTARROW"):
            arduino_code.append("    Keyboard.press(KEY_RIGHT_ARROW);")
            arduino_code.append("    Keyboard.releaseAll();")

        else:
            # Par défaut, toute commande inconnue est ignorée avec un commentaire
            arduino_code.append(f"    // Commande inconnue : {line}")

    arduino_code.append("\n    while (1); // Boucle infinie pour arrêter l'exécution")
    arduino_code.append("}")
    arduino_code.append("\nvoid loop() { }")

    return "\n".join(arduino_code)

if __name__ == "__main__":
    print("Entrez votre script Rubber Ducky (lignes multiples supportées). Terminez avec une ligne vide :")
    ducky_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        ducky_lines.append(line)

    duckyscript = "\n".join(ducky_lines)
    arduino_code = rubber_ducky_to_arduino(duckyscript)

    print("\nVoici le code Arduino généré :\n")
    print(arduino_code)
