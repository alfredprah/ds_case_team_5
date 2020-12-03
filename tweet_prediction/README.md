# Twitter | NLP Tweet Classification
[Data provided by Kaggle](https://www.kaggle.com/c/nlp-getting-started/)

Recently, there has been a rise in tweets flagged related to an emergency or disaster. It is unclear if this is a general algorithm issue or people exploiting the platform. In either case, if fake events were to be flagged as a disaster, it would be detrimental to Twitter's mission to be a reliable source of such events. It could also lead to exploitation from bad actors and cause a general PR nightmare.

Using RoBERTA, we have been able to predict such tweets with 84% accuracy while pushing a small percentage of the predictions we are least confident to manual review via content moderation frontend (powered by Streamlit).

<p align="center">
  <img src="https://github.com/alfredprah/ds_case_team_5/blob/readme_tweet_prediction/tweet_prediction/dashboard/assets/frontend_screenshot.png" width="550">
</p>

## Setup
Required Python packages can be found in the `requirements.txt` of the root repository directory as there is significant overlap between both this and the SNF Optimization project. Our model was trained using GPU resources on [Vanderbilt's ACCRE](https://www.vanderbilt.edu/accre/) compute cluster. As a result. it may run into issues if trying to run locally or in another environment. For details on how to use ACCRE, follow the instructions laid out in [accre-virtual-env.md](https://github.com/alfredprah/ds_case_team_5/blob/master/tweet_prediction/accre-virtual-env.md).

All required data, including that for the dashboard can be found in the `data` directory.

## Streamlit Content Moderation
With the Streamlit package installed, navigate to the `dashboard` directory and execute `streamlit run main.py` in bash/Terminal. As the tweets are labeled manually, they will also update the `dashboard_predictions.csv` data in real-time. Any updates to this CSV will also be relfected in the dashboard!
