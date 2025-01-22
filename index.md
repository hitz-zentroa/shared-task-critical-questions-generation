## Critical Questions Generation Shared Task

<img style="width:45%" src="assets/img/lupa.png" alt="CQs-Gen" title="CQs-Gen logo" align="right">

Welcome to the official website of the Critical Questions Generation shared task, hosted in [The 12th Workshop on Argument Mining](https://argmining-org.github.io/2025/), and co-located in [ACL 2025](https://2025.aclweb.org/), Vienna (Austria)!

In recent years, a growing concern within the educational community has been that the widespread use of LLM-based chats could foster superficial learning habits and weaken students' critical thinking skills. To counter this trend, in this task, we propose using LLMs to guide users towards asking critical questions. That is, questions that can uncover fallacious or poorly constructed arguments. In short: **we want to foster critical thinking by developing a system that generates insightful critical questions when given argumentative texts**.

In the same line, Natural Language Processing applications to deal with misinformation are a popular line of research. However, most applications face challenges regarding three issues: LLMs often lack the required up-to-date knowledge for these tasks, there is not always an agreement on what is the truth, and LLMs themselves can produce hallucinations or rely on unfaithful data, generating misinformation of their own making. **Yet, instead of requiring the LLMs to output factual knowledge, could we use them to point at the missing or potentially uninformed claims?**

#### What is the task of Critical Questions Generation?

The task of Critical Questions Generation consists of generating useful critical questions when given an argumentative text. For this purpose, a dataset of real debate interventions with associated critical questions will be released.

**Critical Questions** are the set of inquiries that should be asked in order to judge if an argument is acceptable or fallacious. Therefore, these questions are designed to unmask the assumptions held by the premises of the argument and attack its inference.

In the dataset, the argumentative texts are interventions of real debates, which have been annotated with Argumentation Schemes and later associated to a set of critical questions. For every intervention, the speaker, the set of Argumentation Schemes, and the critical questions are provided. These questions have been annotated according to their usefulness for challenging the arguments in each text. The labels are either Useful, Unhelpful, or Invalid. The goal of the task is to generate critical questions that are Useful. 

The participant will be asked to develop a system that gets one of the interventions as input, and outputs exactly 3 critical questions. The 3 critical questions should all be useful for challenging the arguments in the intervention. Each of this 3 critical questions will be evaluated separately and then the punctuation will be aggregated. 

See two output examples and their punctuation:

<img style="width:100%" src="assets/img/example.png" alt="example" title="example" align="center">

For more information on Critical Questions Generation, please read [Critical Questions Generation: Motivation and Challenges](https://aclanthology.org/2024.conll-1.9/).

#### How will participants be evaluated?

Each output containing 3 questions will be given a score between 0 and 1, depending on the usefulness of the critical questions. 

Useful critical questions (CQs) will be given 0.33 points, Unhelpful CQs will be given 0.1 points, and Invalid ones will have 0 points. The definitions of these categories are:

- **Useful (USE)**: The answer to this question can potentially challenge one of the arguments in the text.
- **Unhelpful (UN)**: The question is valid, but it is unlikely to challenge any of the arguments in the text.
- **Invalid (IN)**: This question is invalid because it can't be used to challenge any of the arguments in the text. Either because (1) its reasoning is not right, (2) the question is not related to the text, (3) it introduces new concepts not present in the intervention, (4) it is too general and could be applied to any text, or (5) it is not critical with any argument of the text (e.g. a reading-comprehension question). 

TODO: upload evaluation script

#### Participant info

TODO: explain how to sign for the task and how to submit

#### Data

Below are links to access the data already released, as well as provisional expected release dates for future splits.
Do note that release dates are subject to change.

| Dataset split | Access |
|---|---|
| **Sample set** | To be published |
| **Validation set** | To be published |
| **Unlabeled train set** | To be published |
| **Unlabeled test set** | To be published |
| **Labeled test set** | To be published |

<!-- 
### add as: <a href="slkdfjaldsf.zip" download>download</a> (v1)
-->

TODO: release of a simple baseline system and output example


#### Important dates

This information is subject to change.
- Sample data available: To be announced
- Validation data ready: To be announced
- Evaluation start: To be announced
- Evaluation end: To be announced
- Paper submission due: To be announced
- Notification to authors: To be announced
- Camera ready due: To be announced
- Workshop: 31th July (co-located with ACL 2025)


#### Organizers of the shared task

- [Blanca Calvo Figueras](https://github.com/BlancaCalvo), 
HiTZ Basque Center for Language Technology - Ixa, University of the Basque Country UPV/EHU, Spain
- [Rodrigo Agerri](https://ragerri.github.io/), 
HiTZ Basque Center for Language Technology - Ixa, University of the Basque Country UPV/EHU, Spain
- [Elena Cabrio](https://www-sop.inria.fr/members/Elena.Cabrio/), 
University of Côte d’Azur and member of the Inria-I3S research team Wimmics
- [Serena Villata](https://webusers.i3s.unice.fr/~villata/Home.html), 
University of Côte d’Azur and member of the Inria-I3S research team Wimmics

#### Do you have other questions?

TODO: indicate communication channels and potentially create a FAQS website
