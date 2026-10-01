# 2

A minimal demo project.

## Usage

```sh
python3 demo.py           # Hello, world!
python3 demo.py Atif      # Hello, Atif!
```

## Random bar

```sh
python3 bar.py            # fills a bar to a random 0–100%
```

Example output:

```
[#################-----------------------]  43%
```

## Browser bar

**Try it online:** [open the bar](https://claude.ai/artifact/1Y7iHukk3n7yBVaPgDQfbT)

GitHub only shows the code of `bar.html`; it can't run it. To run your own copy, download `bar.html` and open it in a web browser. The bar fills to a random 0–100%; click **Roll again** for a new number.

## PID loop

**Try it online:** [open the PID loop](https://claude.ai/artifact/98hQxziYUNTmeUXmr9zV45)

`pid.html` simulates a PID controller on a first-order process. Move the setpoint and the process value follows it automatically. Tune Kp, Ki and Kd, turn on auto setpoint steps, or kick in a load disturbance.
