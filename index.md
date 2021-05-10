<head>
  <!-- style sheet -->
  <style type = text/css>
    body{
        color: white;
        background-color: rgb(60, 60, 60);
    }

<!-- I don't know why, but both `a` and `a:link` must be changed -->
<!-- to change link colors -->
    a{ color: rgb(97, 175, 239) !important; }
    a:link{ color: rgb(97, 175, 239) !important; }
    a:visited{ color: rgb(230, 180, 180) !important; }

    :is(h1, h2, h3, h4, h5, h6, p) { color: white; }

    code{
        margin-left: 0.2em;
        margin-right: 0.2em;
        outline-style: solid;
        outline-color: rgb(160, 160, 160);
        outline-width: 1px;
        outline-offset: 1px;
        background-color: rgb(50, 50, 50);
    }

    pre code{
      margin-left: 0em;
      margin-right: 0em;
    }
  </style>
</head>

<!-- omit in toc -->
# NBA Salary Regression
<!-- omit in toc -->
## Author: Jackie Lu
<!-- omit in toc -->
## Date: 2021, Apr. 09

<section class="footer">
  <p>
    <a href="https://github.com/jql6/NBA_salary_regression">
      Link to the repository
    </a> | 
    <a href="https://jql6.github.io/">
      Return to homepage
    </a>
  </p>
</section>


<figure>
  <img src="https://raw.githubusercontent.com/jql6/NBA_salary_regression/main/images/nba_court.jpg"
    width="800"
    style="display:block;float:none;margin-left:auto;margin-right:auto;width:60%"/>
  <figcaption><a href="https://unsplash.com/photos/UegcSdRtmlg">Photo</a> by <a href="https://unsplash.com/@neonbrand">NeONBRAND</a> on <a href="https://unsplash.com/">Unsplash</a></figcaption>
</figure>
  

<!-- omit in toc -->
## Table of Contents
- [Colab notebook](#colab-notebook)
- [Data scraping, data cleaning, and data exploration](#data-scraping-data-cleaning-and-data-exploration)
- [Modelling](#modelling)
- [References](#references)

# Colab notebook
You can view the code and graphs in the [Colab notebook](https://colab.research.google.com/drive/1pCPfY6VaR6cS-8a1E8UiChtZLPn2pq9H#scrollTo=CwzSplE2GyVA) that I've posted.

# Data scraping, data cleaning, and data exploration
I used [Selenium](https://selenium-python.readthedocs.io/) and [NBA_API](https://github.com/swar/nba_api) to scrape the data that I used for the regression analysis.  

I thought it would be easy to join the data until I perused the salary data and saw that some of the players, such as P.J. Washington, didn't have periods in their names. I had faced this problem earlier when joining data between [Yahoo API](https://developer.yahoo.com/fantasysports/guide/) and NBA API in which certain players' names wouldn't match up with the other names.  

Thus, I wrote an algorithm to try to match the names between the two lists. I wanted to write a relatively simple algorithm so there are some false positives such as the match between Justin and Jerome Robinson. Luckily, the list was small enough to manually correct.

When I was exploring the data, I was able to make the relationship between salary and minutes per game look more linear on the scatterplot. I did this by applying a natural log transformation on salary. Unfortunately, the log transformation on salary made the other variables less linear with salary.  

<a href="https://colab.research.google.com/drive/1pCPfY6VaR6cS-8a1E8UiChtZLPn2pq9H#scrollTo=zTjVX0war6f7">
  <img src="https://raw.githubusercontent.com/jql6/NBA_salary_regression/main/images/plot1"
       alt="non-linear plot"
       width=600
       style="display:block;float:none;margin-left:auto;margin-right:auto;width:40%"/>
</a>

<a href="https://colab.research.google.com/drive/1pCPfY6VaR6cS-8a1E8UiChtZLPn2pq9H#scrollTo=zTjVX0war6f7">
  <img src="https://raw.githubusercontent.com/jql6/NBA_salary_regression/main/images/plot2"
       alt="non-linear plot"
       width=600
       style="display:block;float:none;margin-left:auto;margin-right:auto;width:40%"/>
</a>

# Modelling
I remember from my [machine learning class](https://www.sfu.ca/outlines.html?2020/fall/stat/452/d100) that a lot of the modelling we did involved doing cross-validation to prevent overfitting and comparing models by using their expected root mean squared error in R. When covering new models, the professor would tell us to throw the new model into the cross validation arena to duke it out with the other models. I decided to replicate this in Python.  

<a href="https://gfycat.com/faroffnegativeirrawaddydolphin-beybladegeeks-animation-episodes-cartoon">
  <img src="https://raw.githubusercontent.com/jql6/NBA_salary_regression/main/images/beyblade_battle.gif"
       alt="beyblades-duking-it-out"
       width=600
       style="display:block;float:none;margin-left:auto;margin-right:auto;width:40%"/>
</a>


One thing I enjoyed about modelling in Python is that the model parameters are all quite similar. Some of the models in R require training and test data split into `X` and `y` while some just need data split into training and test data. In addition, all the cross validation we did in class was done manually by randomly sampling indices. It's really nice to just be able to cross validate with one line of code and just use the data set for every model instead of having to figure out whether or not you needed to further split the data.

While I was testing the voting ensemble, the voting ensemble did better than both the LASSO and Random Forest models. However, in my subsequent tries it ended up being similar to LASSO and Random Forest. I wasn't able to figure out how to make it reproducible. I tried setting the `random_state` parameter for as many things in the code chunk as I could but it still wasn't reproducible. This was the same for the random forest importance plot results.  


# References
1. [Excellent answer on how to center images in markdown](https://stackoverflow.com/a/62383408)

<br>
<br>
<br>
<br>
<!-- Using four breaks here so that when you scroll all the way down -->
<!-- the text content won't be stuck at the very bottom of the screen. -->
<!-- Creating table of contents with Markdown All in One by Yu Zhang. -->