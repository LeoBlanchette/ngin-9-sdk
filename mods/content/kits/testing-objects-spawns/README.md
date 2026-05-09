# Spawner Interval Reference

See item_spawn.cfg as an example. 

[spawner]
spawner_type = "item"                (Required)
interval = "SIMULATION_MINUTE"       (Optional; defaults to SIMULATION_HOUR)
spawn_table = "test"                 (Optional)
clearance_radius = 1.0               (Optional; radius of clearance from the last spawned object. Determines whether another spawn will occur.)
freeze_on_spawn = true                        (Optional; freeze on spawn. Useful for objects that should remain stable and immovable.)

Real-time intervals use normal clock time. Simple enough.

If you want to spawn using real-time intervals, these are the available options:

DECISECOND
HALF_SECOND
SECOND
MINUTE
FIVE_MINUTES
TEN_MINUTES
FIFTEEN_MINUTES
THIRTY_MINUTES
HOUR
TWELVE_HOURS
DAY


Spelling must be accurate. Case is optional.

For better world-based spawn management, it is recommended to use the game timescale:

SIMULATION_SECOND
SIMULATION_MINUTE
SIMULATION_FIVE_MINUTES
SIMULATION_TEN_MINUTES
SIMULATION_FIFTEEN_MINUTES
SIMULATION_THIRTY_MINUTES
SIMULATION_HOUR
SIMULATION_TWELVE_HOURS
SIMULATION_DAY


Example:

interval = "SIMULATION_DAY"


Example:


interval = "MINUTE"


Simulation intervals use the world clock. By default:


real_seconds_per_simulated_day = 3600.0


So:


1 real hour = 1 simulated day
1 real second = 24 simulated seconds


## Simulation Interval Conversions

| Config Value                 | Simulation Time |     Real Time |
| ---------------------------- | --------------: | ------------: |
| `SIMULATION_SECOND`          |        1 second | ~0.04 seconds |
| `SIMULATION_MINUTE`          |        1 minute |   2.5 seconds |
| `SIMULATION_FIVE_MINUTES`    |       5 minutes |  12.5 seconds |
| `SIMULATION_TEN_MINUTES`     |      10 minutes |    25 seconds |
| `SIMULATION_FIFTEEN_MINUTES` |      15 minutes |  37.5 seconds |
| `SIMULATION_THIRTY_MINUTES`  |      30 minutes |    75 seconds |
| `SIMULATION_HOUR`            |          1 hour |   2.5 minutes |
| `SIMULATION_TWELVE_HOURS`    |        12 hours |    30 minutes |
| `SIMULATION_DAY`             |           1 day |        1 hour |
