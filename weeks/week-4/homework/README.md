# Week 4 Homework

## Prerequisites

For this week's lab, follow the **step-by-step** notebook provided in the course repository (or the environment used in class). The notebook covers:
1. **Setting up a simple ChatGPT-like app** (`chatboot.py`). Leveraging Streamlit as the frontend linked to our backend developed in the notebook.
2. **Using semantic caching** to save tokens and speed up responses.
3. **Collecting and monitoring logs** to observe the app’s performance and usage.

## Homework Assignment

### 1. Record a 3–5 Minute Video

- **Goal**: Present the **backend architecture** of the app discussed in class.
- **Contents of the Video**:
  1. **Explain the backend architecture**: Describe how requests flow from the user interface (or a script) to the vector store, cache, LLM, and back.
  2. **Describe the functionality** of the app, focusing on:
     - How **semantic caching / DB** is used to **save tokens** and **speed up requests**.
     - How the app processes an input query, fetches embeddings/vectors (if used), and communicates with the LLM.
  3. **Demo** Try few queries as `What is covered under the PerksPlus program?`or `What health plans are available at Contoso Electronics?` and demonstrate the functionality. 
- **Video Upload**:
  - Host the video on **your own site**, **Vimeo**, **YouTube**, or any preferred platform.
  - Provide the **public link** or **upload** it to the platform.

### 2. (Optional) Enhance the App

- Add additional components, features, or integrations:
  - **Monitoring and logging**: Use any observability tool or set up advanced logs (e.g., Apps Insight).
  - **Containerization**: Dockerize the app and run it in the cloud (e.g., Azure Container apps or web apps).
  - **UI improvements**: Imprpve the sreamlit code to amke it mor eitnneattciev with yoru new features.

### 3. Extra Incentive

- The **top 3** most **creative** or **feature-rich** demonstrations (or videos) will have the chance to **present in class**.
- Ensure your enhancements are well documented and easy to follow for your classmates!