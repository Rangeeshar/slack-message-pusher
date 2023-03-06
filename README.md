# slack-message-pusher
Pushed slack messages to the webhook URL

## How to run

- Make sure python3.9 and python3-env is installed.
- Create a virtual env using `python3 -m venv virtual_env`.
- Now install the requirements.txt `pip install -r requirements.txt`.
- Now export the slack webhook url using -> `export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/Sdadas0EEV0HM/B04SH2125EN8/BQWgdBtVCLSrnzsYtbUiUHdsad`.
- Now Run the service using the command `uvicorn main:app --reload`.
- Now make a CURL or postman request to the endpoint.

Sample CURL

```bash
curl --location 'http://localhost:8000' \
--header 'Content-Type: application/json' \
--data-raw '{
  "RecordType": "Bounce",
  "Type": "SpamNotification",
  "TypeCode": 512,
  "Name": "Spam notification",
  "Tag": "",
  "MessageStream": "outbound",
  "Description": "The message was delivered, but was either blocked by the user, or classified as spam, bulk mail, or had rejected content.",
  "Email": "zaphod@example.com",
  "From": "notifications@honeybadger.io",
  "BouncedAt": "2023-02-27T21:41:30Z"
}'
```
