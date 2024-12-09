# Terry Stops Data Analysis

## Overview

This project analyzes **Terry Stops** data, which refers to brief detentions by law enforcement based on **reasonable suspicion** of criminal activity or the presence of a weapon. The goal of this analysis is to explore potential biases in policing practices, specifically in relation to **race**, **gender**, and **age**. Additionally, the analysis seeks to assess the **effectiveness** of these stops in achieving law enforcement outcomes, such as **arrests** or **summons**.

---

## Objectives

- Investigate the **demographic factors** (e.g., race, gender, and age) that influence the likelihood of being stopped.
- Identify potential **biases** in policing practices, with a particular focus on minority groups.
- Evaluate the **effectiveness** of Terry stops, assessing how often they lead to tangible law enforcement actions such as arrests.
- Develop **predictive models** to improve resource allocation and inform policing strategies.
- Provide **data-driven recommendations** for enhancing fairness, transparency, and effectiveness in policing.

---

## Dataset Overview

The dataset used in this project contains **61,980 records** and **23 features**. These features cover:
- **Subject Demographics**: Age, Gender, Race.
- **Officer Demographics**: Officer Gender, Officer Race, Officer Year of Birth.
- **Stop Details**: Stop Resolution, Officer Squad, Precinct, Sector, Beat.
- **Outcome**: Arrest Flag, Frisk Flag.

---

## Key Findings

- **Racial Bias**: There are more whites in the police force compared to all other demographic groups.
- **Gender Disparity**: Males are significantly more likely to be stopped compared to females.
- **Effectiveness of Stops**: The majority of stops result in **Field Contact** (no formal action), with only **6%** leading to arrests.
- **Officer Demographics**: The racial and gender composition of officers impacts their decisions to initiate Terry stops, with White officers predominantly interacting with Black and Hispanic subjects.
- **Temporal Trends**: There was an increase in the number of stops from **2015 to 2018**, followed by a steady decline through **2024**.
- **Geographical Patterns**: Certain precincts (e.g., **West**) have significantly higher stop frequencies, while others (e.g., **Southwest**) have fewer stops.

---

## Methodology

### Data Cleaning and Preprocessing:
- **Missing Data**: Handled by imputing missing values for categorical features using the **mode** and **"Unknown"** for geographic columns.
- **Outliers**: Identified and removed based on **box plots** and **percentile filtering**.
- **Categorical Data**: Encoded using **Label Encoding** and **One Hot Encoding** to convert non-numeric data into a machine-learning-friendly format.

### Exploratory Data Analysis (EDA):
- Analyzed **age**, **gender**, and **race** distributions for both subjects and officers.
- Explored **stop resolutions** to understand how often stops result in meaningful law enforcement actions.
- Investigated **temporal** and **geographical** patterns to identify any trends related to time of day, precincts, and sectors.

### Predictive Modeling:
- **Logistic Regression** and **Decision Trees** were used to predict the likelihood of an **arrest** based on demographic and situational factors.
- Models were evaluated using **cross-validation** and **classification metrics** (precision, recall, F1-score).
- **SMOTE** (Synthetic Minority Oversampling Technique) was used to address class imbalance in the dataset.

---

## Recommendations

### **1. Implement Targeted Training Programs for Law Enforcement Officers**
- Focus on recognizing and mitigating **implicit biases**, particularly regarding **race** and **gender**. The training should be informed by findings that indicate **disproportionate stops of minority groups**.

### **2. Enhance Data Transparency and Accountability**
- Establish a **public database** that tracks Terry stops, arrests, and outcomes, disaggregated by **race**, **gender**, and **precinct**. Ensure that the data is **regularly updated** and accessible to the public and oversight bodies.

### **3. Refine Stop Criteria and Procedures**
- Review and revise the criteria for initiating Terry stops to ensure they are based on **specific, articulable facts** rather than vague suspicions. Develop a **standardized protocol** for officers to follow when conducting stops.

### **4. Utilize Predictive Analytics for Resource Allocation**
- Leverage the **predictive models** developed in this analysis to inform resource allocation and deployment strategies, such as identifying **high-risk areas** and times for potential criminal activity.

### **5. Regularly Evaluate Policing Practices**
- Conduct **regular evaluations** of Terry stop outcomes, focusing on metrics like **R² values**, **p-values**, and **model accuracy** to continuously assess and improve policing practices.

---

## Conclusion

The analysis of **Terry Stops** data reveals important insights into policing practices, including evidence of racial and gender disparities in police stops. While the majority of stops do not lead to formal outcomes like arrests, the findings highlight the need for **policy reforms**, **better training**, and **increased transparency**. By implementing the recommendations outlined in this report, law enforcement agencies can take significant steps towards more **equitable**, **effective**, and **transparent** policing practices.

---

## Future Work

- Further research could explore the **root causes** of disparities in police stops and **longitudinal studies** to track changes in policing over time.
- Additionally, expanding the analysis to include **community feedback** on police practices could provide valuable insights into **public perceptions** of fairness and justice.

---

## Acknowledgements

This project utilizes publicly available data and leverages the collective work of researchers and organizations working toward **fairer policing**. Special thanks to the community, law enforcement experts, and policymakers dedicated to improving police practices and ensuring transparency and accountability.

---
---

## Contact

For further inquiries, please contact:

**Email**: [My Mail](dennis.limo@student.moringaschool.com)  
**GitHub**: [GitHub Link](https://github.com/ShemDennis)

