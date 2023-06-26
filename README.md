# planet-generator
Simple web-service for creating images of planet


## Installation and setup

- Clone repository:
    ```commandline
    git clone https://github.com/PavloShutz/planet-generator.git
    ```
- Make initial setup:
  * Install requirements:
    ```commandline
    pip install -r requirements.txt
    ```
  * Rename `.env.dist` to `.env`;
  * Set current parameters in `.env`:
     ```dotenv
      # Django's secret key
      SECRET_KEY=
      # OpenAI secret API key
      OPENAI_TOKEN=
      ```

## Task list
- [x] ~~Add more fields to planet model~~
  - [x] ~~image~~
  - [x] ~~resolution~~
  - [x] ~~atmosphere~~
  - [x] ~~temperature~~
- [x] ~~Create function to generate text request for DALL-E~~
- [x] ~~Add user authorization and authentication~~
- [x] ~~Create image portfolio for every user~~
- [ ] Make possible to: 
  - [x] ~~publish~~
  - [ ] like/dislike
  - [ ] comment on someone's post