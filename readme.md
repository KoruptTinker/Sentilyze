# Sentilyzer
A machine learning based approach towards social media analysis using natural language processing. It offered the following services :- Getting analysis using a simple keyword search, user profile analysis, trending topics analysis. The initial build was primarily focused towards Twitter. Cross-platform usability will be accomodated by deploying it as an API service.

# Installation
Use the package manager using the requirements.txt provided.
```bash 
pip install -r {path to requirements.txt}
```

# Usage
The program provides a basic GUI right now (Java required). The files have been provided for the same. 

API :- 
1) Copy all the files presented. Get your API keys from [Twitter Developer](https://developer.twitter.com/)
2) Put in the keys at the appropriate places in the file analysis.py
3) Run 'api.py'
4) For username search ```curl 127.0.0.1:5000/searchByUser?id={put in the twitter handle here} ```
   For topic/hashtag search ```curl 127.0.0.1:5000/searchByHash?id={put in the hashtag excluding #}```
5) Obtain json. 

## Contributing
Pull requests are welcome. Kindly open an issue beforehand so we can discuss the same.

