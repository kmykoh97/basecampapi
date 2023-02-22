# Coingecko Basecamp API Wrapper

This Python wrapper allows simple interaction with [Basecamp API](https://github.com/basecamp/bc3-api) using Python.

## Initial authentication: Getting your refresh token

**You only need to do this the first time. Once you get your Refresh token you should pass it with your credentials to gain access. If you already have a Refresh token you should skip this step.**

To begin the authentication process, you first need to create a file credentials.json and fill it up like credentials.example.json:

```python
from basecampapi import Basecamp

your_credentials = {
	"account_id": "your-account-id",
	"client_id": "your-client-id",
	"client_secret": "your-client-secret",
	"redirect_uri": "your-redirect-uri"
}

bc = Basecamp(credentials=your_credentials)
```
Your account ID can be found on your Basecamp home page, in the URL address:
> https:<SPAN></SPAN>//3.basecamp.com/<b>YOUR-ACCOUNT-ID</b>/projects

If your credentials dictionary does not contain a "refresh_token", an error will be raised which contains a link for the authorization of your app. You need to open that link on the browser where you are logged into your Basecamp account and  click on "Yes, I'll allow access":

![Verification page](https://user-images.githubusercontent.com/24939829/209202366-bae05d01-5f8d-4ca6-a0f8-5e1eb9088acd.png  "Verification page")

Clicking that button will redirect you to the link you provided as Redirect URI in your credentials, but it will have the verification code in the url address. Save that verification code:

![Verification code](https://user-images.githubusercontent.com/24939829/209202400-d2aa342b-70e1-4fd1-9787-2f3dc1280a57.png  "Verification code")

Initiate the `Basecamp` object again, and provide the code you gathered via the `verification_code` parameter:

```python
# Verification code variable 
your_verification_code = "17beb4cd"

bc = Basecamp(credentials=your_credentials, verification_code=your_verification_code)
```

This will generate your Refresh token. Fill the token to credentials.json

## Run

1. To get New Exchanges' Stats
- runs: `python3 newexchange.py`
- csv data files will be generated in `data/*.csv`

2. To get Bugs' Stats
- Developing...