# Agro CLI

Command line interface to get weather forcast globally.

## Installation

1. Clone the repo `git clone https://github.com/NamamiShanker/agro-cli.git`
2. Navigate to project directory `cd agro-cli`
3. Install the project using pip `pip3 install -e .`
4. Add an environment variable `WEATHER_API_KEY='your open weather map api key'`
5. Use the agro CLI  `agro --city=London --date=2021-07-29`

## Usage

* Get weather forecast for a city for a specified date.
```
agro --city=Lucknow --date=2021-07-29
```
![Agro CLI Search by city](https://i.imgur.com/z0nmZPW.png)

* Get weather forecast with coordinates and specified date.
```
agro -lt=26 -lg=82 --date=2021-07-29
```
![Agro CLI Search by coordinates](https://i.imgur.com/UF2HpRv.png)

* `--help` parameter to get started with arguments.
```
agro --help
```

![Agro CLI Help](https://i.imgur.com/7MCvnGU.png)