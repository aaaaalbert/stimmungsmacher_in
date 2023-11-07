# Stimmungsmacher\_in

Der\_die Stimmungsmacher\_in ist ein Patch in
[Pure Data](https://puredata.info/),
um mit unterschiedlichen Stimmungen zu experimentieren.

Der Patch nimmt MIDI-Daten entgegen, verstimmt sie der ausgewählten
Stimmung entsprechend, und gibt sie über einen polyphonen Synthesizer
hörbar wieder.

Zurzeit werden die gleichschwebende, eine auf der Obertonreihe basierende,
die pythagoräische und die reine Stimmung unterstützt. Zusätzlich sind
die Stimmungsverhältnisse der Hammond-Orgel verfügbar.

Um die "Verschiebung" der Töne innerhalb einer Stimmung zu verdeutlichen,
kann der Grundton der Stimmung variiert werden. Die Verhältnisse werden
dann nicht von c, sondern vom ausgewählten Ton darüber aus aufgebaut.

Wenn alle Stricke reißen (z.B. Töne "hängenbleiben", weil während des
Spielens umgestimmt wird), gibt es noch die `stop`-Message, um alle
Töne zu beenden.


## Dateien

`Instrument.pd` ist der spielbare Hauptpatch.

`Stimmungsmacher_in.pd` empfängt Notendaten und nimmt die Verstimmung
vor. Die Tabellen für die jeweilige Stimmung liegen im Unterordner
`Stimmungen/` und können mit dem dort befindlichen Python-Skript
berechnet und ausgegeben werden.

`Stimme.pd` ist die Implementierung einer einzelnen Synthesizer-Stimme.
Sehr banal: Ein `[osc~]` mit 90 Grad Start-Phasenverschiebung, um
das Einklingen zu entknacksen, und Nutzung der MIDI-Velocity als
(linearer) Lautstärkefaktor.

# Future Work
Käsigen Synthesizer raus, Ausgabe über MIDI (aufgetrennt auf Kanäle, jeder
mit angepasstem Pitch Bend) rein.


# Inspiration und Quellen
* VO Allgemeine Musiklehre (Mag. S. Reisigl)
* Buch "ABC Musik · Allgemeine Musiklehre" (W. Ziegenrücker)
* https://de.wikipedia.org/wiki/Tonstruktur_(mathematische_Beschreibung)#Beispiele_ausf%C3%BChrlich
* Eigene unveröffentlichte Vorarbeiten an der "Cheese Wheel Organ", einer
  Hammond-Emulation in Pure Data.

