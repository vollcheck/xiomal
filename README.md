# xiomal

### Description

`xiomal` is a study project that process XML (unfortunately, that's the requirement) data from external API.

### Preparation

All you need before you start is just install dependencies using following command:

```console
pip install -r requirements.txt
```

### Usage

After dependency installation, you can use the application by writing:

```console
python xiomal.py
```

After that you should see the usage:

```console
Usage: xiomal.py [OPTIONS] CITY
Try 'xiomal.py --help' for help.

Error: Missing argument 'CITY'.
```

Okay, you are ready to go! Ask for weather information of, let's say, Toronto:

```console
python xiomal.py Toronto
```


Result:

```console
You've requested data for 'Toronto'
Country: Canada
Local time: 2022-01-12 13:14
Air condition: Overcast
Pressure: 1013
Temperature (°C): 2
Feels like temperature (°C): -3.2
```
