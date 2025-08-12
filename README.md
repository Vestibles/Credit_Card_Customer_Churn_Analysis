# Customer Credit Card Churn Analysis

This project is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provided an intuitive interface for both technical and non technical individuals.

### Dataset Content
The dataset used is `cleaned_bank_churn.csv`, which contains anonymised customer data from a financial institution. It focuses on credit card usage and churn behavior. It has 10,127 customer records and 34 columns after preprocessing (one-hot encoding for categorical variables). Key features include demographics (e.g., Customer_Age, Gender_M), account details (e.g., Months_on_book, Credit_Limit), transaction metrics (e.g., Total_Trans_Amt, Total_Trans_Ct), and the target variable Churn (binary: 0 for retained, 1 for churned customers, with ~16% churn rate). The file size is approximately 2.5 MB, well within the 100 GB repository limit. Data is in CSV format, with no missing values post-cleaning, and includes derived features like Total_Trans_Amt_per_Transaction and Spend_Efficiency.

### Business Requirements

The primary business goal is to identify factors driving customer churn to inform retention strategies, such as targeted marketing or incentives for at-risk groups. Requirements include:
- Analyze differences in continuous variables (e.g., transaction counts, credit utilization) between churned and retained customers.
- Examine associations between categorical variables (e.g., income category, education level) and churn.
- Validate hypotheses using statistical tests to provide evidence-based insights.
- Visualize results in an interactive dashboard for stakeholders to explore churn predictors.
- Ensure analysis is reproducible and scalable for future datasets.

### User Stories

The data is real but the USER STORIES are made up as follows:
- As a bank analyst, I want to predict customer churn so that we can take preventative action.
- As a manager, I want a dashboard summarising churn rates so I can make strategic decisions.

### Hypothesis and how to validate?
Hypotheses:
1. Churned customers exhibit lower transaction activity (e.g., fewer transactions or lower amounts) compared to retained customers. Validation: Use t-tests and Mann-Whitney U tests on variables like Total_Trans_Ct and Total_Trans_Amt; compute Cohen's d for effect size. Reject null if p < 0.05.
2. Lower income categories are associated with higher churn rates. Validation: Chi-square test on Income_Category vs. Churn contingency table. Reject null of independence if p < 0.05.
3. Demographic factors like age or gender influence churn. Validation: Similar statistical tests on relevant variables.

Validation involves splitting data into churn/non-churn groups, running tests in Python (scipy.stats), and interpreting p-values and effect sizes.

### Project Plan
High-level steps:
1. Data collection: Load and explore the CSV dataset.
2. Processing: Handle encoding (already one-hot), compute descriptives, and ensure no outliers skew results.
3. Analysis: Perform hypothesis tests and visualizations.
4. Interpretation: Draw insights and map to business needs.

Data management: Stored locally in CSV; processed in-memory with pandas for efficiency. Version control via Git. Research methodologies: Inferential statistics chosen for hypothesis testing due to their rigor in detecting differences/associations; non-parametric tests (e.g., Mann-Whitney) used as alternatives for non-normal data.

Rationale for mapping business requirements to visualizations:
- Requirement: Identify churn predictors → Visual: Boxplots/histograms of transaction metrics by churn group.
- Requirement: Association with categories → Visual: Bar charts of churn rates by income/education.
- Requirement: Stakeholder communication → Interactive dashboard with filters.

### Analysis techniques used
Methods: T-tests (parametric mean comparison), Mann-Whitney U (non-parametric distribution comparison), Cohen's d (effect size), Chi-square (categorical association). Limitations: T-test assumes normality. Alternatives to consider may have been ANOVA for multi-group if expanded. Data did not limit significantly (large sample size >10k ensures power), but if skewed, log-transformations could be applied—no alternatives needed here.

Structure: Sequential—descriptives first, then tests on continuous variables, followed by categorical. Justified by building from univariate to multivariate insights.

Generative AI (e.g., Grok by xAI) aided ideation (brainstorming hypotheses), design thinking (outlining dashboard), and code optimization (suggesting efficient pandas queries and scipy implementations).

### Ethical considerations
Data privacy: Dataset is anonymised (no personal identifiers) and compliant with GDPR laws and standards. Bias/fairness: Potential income or gender biases in churn prediction—checked via stratified sampling if modeling; mitigated by transparent reporting of associations (e.g., lower income linked to churn, but not causal). No legal issues were identified; societal: Insights could inform equitable retention (e.g., support for low-income groups). 

### Dashboard Design
Dashboard pages (using Power BI):
1. Home: Overview with churn rate summary (card visual), dataset descriptives table (matrix visual), and slicers for filtering variables (e.g., Income_Category, Gender_M).
2. Continuous Analysis: Boxplots or line charts for variables like Total_Trans_Ct (scatter plot with jitter), test results displayed in a table visual.
3. Categorical Analysis: Bar charts for income vs. churn (stacked bar chart), chi-square results in a text box or KPI visual.
4. Insights: Key findings summary (text box), export button for reports (Power BI export feature).

Updates: Initially planned heatmaps for correlations but switched to bar charts for clearer categorical insights.

Communication: Technical audiences via detailed test stats in tables and tooltips; non-technical via intuitive visuals (e.g., color-coded churn rates) and plain-language summaries in text boxes. Design: User-centric—drag-and-drop interface, slicers for interactivity, tooltips explaining stats (e.g., "p-value <0.05 means significant difference"), optimized for desktop and mobile views.

### Unfixed Bugs
No major unfixed bugs; minor issue with Power BI rendering complex visuals in some environments (e.g., outdated DirectQuery mode), not fixed due to framework limitation (resolved by switching to Import mode). Recognized gaps: Limited experience with Power BI DAX—addressed by online tutorials and AI assistance. Peer feedback (hypothetical from collaborators): Suggested adding confidence intervals to visuals; incorporated using custom measures.

### Development Roadmap
Challenges: Handling large-ish dataset efficiently in Power BI (overcame with Import mode and data model optimisation); interpreting DAX for custom metrics. Strategies: Iterative testing, modular data model design.

Next skills/tools: Deepen Power BI expertise (DAX, Power Query); Streamlit, explore ML integration with Power BI for predictive churn models.

### Main Data Analysis Libraries
- pandas: For data loading and manipulation, e.g., `df = pd.read_csv('cleaned_bank_churn.csv'); churn_group = df[df['Churn'] == 1]`.
- scipy.stats: For tests, e.g., `stats.ttest_ind(churn_group['Total_Trans_Ct'], no_churn_group['Total_Trans_Ct'])`.
- matplotlib/seaborn: For visualizations, e.g., `sns.boxplot(x='Churn', y='Total_Trans_Amt', data=df)`.
- statsmodels: For effect sizes if extended.

### Requirements
numpy==1.26.1
pandas==2.1.1
matplotlib==3.8.0
seaborn==0.13.2
ydata-profiling==4.12.0 # can be removed from requirements before deployment
plotly==5.17.0
ppscore==1.1.0 # can be removed from requirements before deployment
streamlit==1.40.2
feature-engine==1.6.1
imbalanced-learn==0.11.0
scikit-learn==1.3.1
xgboost==1.7.6
yellowbrick==1.5 # can be removed from requirements before deployment
Pillow==10.0.1 # can be removed from requirements before deployment

### Credits

#### Content
- Dataset  Kaggle's Bank Customer Churn Prediction dataset (https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers).
- Guidance on statistical tests from SciPy documentation (https://docs.scipy.org/doc/scipy/reference/stats.html).
- Ideas for hypothesis validation from Towards Data Science articles on churn analysis.
- Assistance from Gen AI Copilot, ChatGPT, and GrokAI for ideation, code optimization, and design thinking.
- Support from Emma Lammont (Code Institute) and Code Institute LMS for project structure and guidance.
- Code snippets and versioning from GitHub repositories and tutorials.
- Power BI tutorials from Pragmatic Works

#### Media
- Icons and plots generated via matplotlib; no external media used.

****Thank you to all those who provided me with support through this project****