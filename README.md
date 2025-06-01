
# iiot2025.github.io

This is the official website for the 2025 Budapest Finals of the International Informatics Olympiad in Teams.


## Run Locally

Clone the project:
```bash
  git clone https://github.com/kodkupa/iiot2025.github.io
```

Install dependencies:
```bash
  cd iiot2025.github.io
```
```bash
  npm install
```

Run the project locally:

```bash
  npm run dev
```


## Deployment

To deploy on github pages, run:

```
  npm run deploy
```


## Participants

The participants and teams are stored in the `src/lib/json-data/teams.json` file, in the given format, extend if necessary.
Pictures of the participants are stored at `static/images/participants`.


## Schedule

The schedule table is downloaded as a comma separated csv file from google sheets and stored at `src/lib/Program.html`, it can be easily replaced this way.


## Documents

The documents that are linked on the site such as the *privacy_policy.pdf* etc. are in the `static/documents` folder, replace them there if needed.


## Authors

| Github | Email |
| :- | :- |
| [@TkcsHnr](https://www.github.com/TkcsHnr) | [tkcshnr@gmail.com](mailto:tkcshnr@gmail.com) |
| [@niklaci](https://www.github.com/niklaci) | [laszlo.nikhazy@gmail.com](mailto:laszlo.nikhazy@gmail.com) |


## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| IIOT logo turquoise | ![#6dc1c3](https://placehold.co/15x15/6dc1c3/6dc1c3.png) `#6dc1c3` |
| IIOT logo purple | ![#f8f8f8](https://placehold.co/15x15/595bb4/595bb4.png) `#595bb4` |
| IIOT logo grey | ![#00b48a](https://placehold.co/15x15/a3a3a3/a3a3a3.png) `#a3a3a3` |



