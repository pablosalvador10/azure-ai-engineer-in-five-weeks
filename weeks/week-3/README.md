# Week 3: Evaluation and Tracing

This week's assignment will have you running a console based generative AI application and evaluating your own prompt engineering.

To be successful with this week's homework, please be sure to have completed the following steps:

1. Ensure all of your model deployments are in your AI Foundry deployment.
    ![All models should be deployed under your AI Foundry default](./img/week-03-all-models-needed-in-default-aoai-endpoint.png "Models should be under default AI Foundry deployment")
2. You will need three deployments:
    * gpt-4o
    * gpt-4o-mini
    * text-embedding-ada-002
    * If you choose global standard, your [region should be available](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#model-summary-table-and-region-availability)
3. Rename `.env.sample` to `.env` and update the variables:
    * AIPROJECT_CONNECTION_STRING
    * AISEARCH_INDEX_NAME
4. In your Python virtual environment, install this week's requirements.txt
    `pip install -r requirements.txt`
5. Verify that the `genaiapp.py` script works by executing:
    ```bash
    cd /path/to/weeks/week-3
    python ./genaiapp.py
    ```
6. Read through the genaiapp.py code to verify your understanding of what it's doing. Follow the links to learn more about evaluation.
7. Perform prompt engineering on the `week-3/assets/grounded_chat.prompty` file.
8. Evaluate your results across the test set by running `python ./single-query-evaluate.py` with the `week-3` folder as the current working directory.

---
## Assignment Evaluation

For the final homework submission please complete the following:

* (Paper) Find at least one "Prompt Engineering Best Practices" article from a reputable source (e.g. academic paper or practitioner blog)
* Decide on three independent experiments you will run to evaluate your prompt engineering. For each experiment you will submit the files `0X_grounded_chat.prompty` and `0X_evaluation-results.json` where `X` is your experiment number (1, 2, or 3). You will submit six files (3 prompty files, 3 json files).
    * (Grounded Prompty) Make three successive changes to the `assets/grounded_chat.prompty` and save a copy of the changed files.
        * For example, the first change you make might be to prevent hallucinations. Save the prompty file after your changes as 01_grounded_chat.prompty
        * Your second change might be to only prevent answering questions on other topics.
        * Your third change might be combining both of these experiments into one.
    * (Evaluation) Store the results of each successive run as `0X_evaluation-results.json` where `X` is your experiment number (1, 2, or 3). You must rename the file before re-running the `python ./single-query-evaluate.py` command or the results of the previos run will be overwritten.
* (Interpretation) Provide a written response in the format below under "Interpretation of Results"

---
## Interpretation of Results

(Summarize your interpretation of the results. What prompt engineering actions worked best? What did worse? What would you do next to make this ready for users?)

### Research Article

I found a prompt engineering article written by (Author's Name) through (LinkedIn, Arxiv, etc.). I decided to experiment with the following prompt engineering tips:

* (Tip #1)
* (Tip #2)
* (Tip #3)

(Link to article)

### Experiment Summary

**Experiment 1:(Tip #1)**

* I changed the ground chat prompty by... (e.g. adding this line...)

Groundedness Change:

* Groundedness (improved|declined) over the baseline resulting in an average of (average the groundedness scores from the evaluation-results.json)

**Experiment 2:(Tip #2)**

* I changed the ground chat prompty by... (e.g. adding this line...)

Groundedness Change:

* Groundedness (improved|declined) over the baseline resulting in an average of (average the groundedness scores from the evaluation-results.json)

**Experiment 3:(Tip #3)**

* I changed the ground chat prompty by... (e.g. adding this line...)

Groundedness Change:

* Groundedness (improved|declined) over the baseline resulting in an average of (average the groundedness scores from the evaluation-results.json)

---

## Rubric

Each component's inclusion and quality of response and effort are graded as follows

* (Paper) 5 points - A link to a reputable source on prompt engineering tactics that you then implement three of them
* (Grounded Prompty) 5 points - All three files are included using the naming convention and have differences across the three files
* (Evaluation) 5 points - All three files are included using the naming convention and have differences across the three files
* (Interpretation) 15 points - Provide a brief, complete interpretation of the experiments in prompt engineering that you ran and a meaningful attempt to interpret the change in groundedness and describe the additional prompt engineering steps you would try before putting this in front of users.
