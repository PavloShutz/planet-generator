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
      ```

## Task list
- [ ] Add more fields to planet model
  - [x] ~~image~~
  - [x] ~~resolution~~
- [ ] Create function to generate text request for DALL-E
- [ ] Add user authorization and authentication
- [ ] Create image portfolio for every user
- [ ] Make possible to publish, like/dislike and comment on someone's planet