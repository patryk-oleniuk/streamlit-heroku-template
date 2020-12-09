# streamlit-heroku-template
Template to create ML apps using Streamlit and deploy it on Heroku.
Should work nicely and easily. Just click [Use this Template](https://github.com/patryk-oleniuk/streamlit-heroku-template/generate) button on the top-right and name your app.

Detailed tutorial available in Towards Data Science:

[Show your ML Project to the Internet in Minutes](https://towardsdatascience.com/show-your-ml-project-to-the-internet-in-minutes-2a7bc3167bd0)

Instruction for a quick run:
1. Use this template, change the name to yours.
2. (can skip this step if you just wanna deploy my dummy app for now) Develop your streamlit app in `app/streamlit_app.py`. Try locally using `streamlit run app/streamlit_app.py`. Remembers to adjust `requirements.txt` with your required python packages and python version in `runtime.txt`.
3. Deploy to Heroku by connecting this repo to you Heroku project. It should recognize everything automatically and just deploy to `https://yourname.herokuapp.com` for free (if you selected free tier).

This template app is currently automatically deployed to 
https://streamlit-heroku-template.herokuapp.com/
(you can deploy your version just with the different app name)

# References
- Streamlit : https://www.streamlit.io/ 
- Deploying the app on Heroku: https://towardsdatascience.com/deploy-streamlit-on-heroku-9c87798d2088
