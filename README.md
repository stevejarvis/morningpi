Raspberry Pi and the Morning Update
===================================

Just for fun, the Pi should say hi in the morning. Maybe like an alarm,
read the weather, someone's last tweet... I dunno.

Installation (on Raspian)
-------------------------

* Python 3 is needed, installed in Raspian by default.
* Mplayer is needed for speech:
`$ sudo apt-get install mplayer`
* Clone this repository:
`$ git clone https://github.com/stevejarvis/morningpi.git`
* Run the tests:
`$ cd morningpi`
`$ python3 tests.py`
* If they pass, you should be set! See if it talks:
`$ python3 main.py`
