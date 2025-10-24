# Week 2: Designing Intelligent Cloud-Native AI Systems 🛠️

## 🌐 Available Languages

- [🇺🇸 English](./README.md) ← You are here
- [🇪🇸 Español](./README.es.md)

## Table of Contents 📑
- [Overview](#overview-📋)
- [Learning Objectives](#learning-objectives-🎯)
- [Prerequisites](#prerequisites-📚)
- [Materials](#materials-📂)
- [In-Class Activities](#in-class-activities-🛠️)
- [Assignments](#assignments-📝)
- [Setup Instructions](#setup-instructions-⚙️)

## Overview 📋
In Week 2, we focus on advancing your knowledge of Azure AI by exploring orchestration frameworks like Microsoft’s **Semantic Kernel**. You will also learn how to enhance chatbot functionality with multimodal AI integration, enabling the processing of multiple data types such as text, images, and documents.

### Defining the AI System Framework:
This week introduces the concept of an **AI System** as a composite system where the **Large Language Model (LLM)** acts as the central processing and reasoning engine, seamlessly orchestrating calls to multiple Azure AI services. We will demonstrate this by building a **Retrieval-Augmented Generation (RAG) system** that integrates various services and capabilities into a unified pipeline.

#### What is RAG?
**Retrieval-Augmented Generation (RAG)** is a system design pattern that combines information retrieval (retrieving relevant data from structured or unstructured sources) with generation (leveraging LLMs to synthesize and respond to user queries). This pattern ensures:
- Contextual and accurate responses by grounding the LLM in real-world data.
- Improved performance by narrowing the scope of generative tasks through retrieved evidence.

### Key Focus:
- **Pro-Code Indexing and Customization**: We enhance the chatbot from Week 1 by implementing advanced, code-driven indexing in Azure AI Search. This provides flexibility and precision in managing search and retrieval pipelines.
- **Semantic Kernel Integration**: Leveraging the orchestration capabilities of Semantic Kernel, we unify multiple services, including Azure AI Vision, Content Understanding, and Azure OpenAI, enabling multimodal AI capabilities.
- **Dynamic System Design**: The AI system is designed to dynamically adapt its LLM usage and retrieval strategies based on user queries and context, exemplifying a highly scalable and efficient architecture.

This hands-on session equips you with the tools and knowledge to build and operationalize a cloud-native AI system, showcasing the power of **Semantic Kernel** in orchestrating Azure AI services to create intelligent, scalable solutions.


## Learning Objectives 🎯
- **Master Orchestration Frameworks with Semantic Kernel**: Gain a deep understanding of how Microsoft’s Semantic Kernel enables seamless coordination of multiple Azure AI services to build scalable and intelligent AI systems. 
- **Build a Vector Database in Azure**: Create and manage a vector-based data store laveraging Azure AI Search, leveraging integrated vectorization for efficient indexing and searching.  
- **Enable Multimodality in Your Chatbot**: Incorporate text, images, and other data types to provide a richer, more dynamic user experience.  
- **Build a Backend Orchestration Framework**: Establish a robust architecture that coordinates services and tasks for our chatbot.  
- **Develop a Front-End with Streamlit**: Implement a streamlined interface that interacts with backend  microservices and components, facilitating a fully functional AI solution.

## Prerequisites 📚
To make the most of this session, you should have:

 - **Week 1 Materials**: Review foundational concepts and services from Week 1, including Azure AI Foundry, OpenAI, and Azure AI Search. [Learn more](./weeks/week-1/README.md)

- **Cloud and Azure Expertise**:
  - Hands-on experience with Azure services, including creating and managing resources.
  - Basic knowledge of Azure AI services such as Azure AI Search, OpenAI, Vision, and Content Understanding, as introduced in Week 1.

- **Required Access**:
  - Active Azure subscription with permissions to deploy and use AI services.

## Materials 📂
- **Slides**: [Link to presentation slides]
- **Readings**:
  - **Introduction to Semantic Kernel**: Learn how to orchestrate AI services effectively. [Learn more](https://learn.microsoft.com/en-us/semantic-kernel/overview)
  - **Multimodal AI Integration**: Explore techniques for handling multiple data types. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
  - **Enhancing AI Systems with Azure**: Tutorials on integrating Azure AI services. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/)
- **Additional Resources**:
  - **Azure AI Vision Services**: Tools for image and video analysis. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
  - **Azure AI Content Understanding**: Advanced document analysis. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
 
> Ensure you are comfortable with the Week 1 chatbot implementation, as it forms the baseline for enhancements this week.

## In-Class Activities 🛠️
This session includes a hands-on group activity to walk through the **lab.ipynb** notebook together:
  - Learn about designing scalable, modular systems using microservices in Azure.
  - Explore the role of Semantic Kernel in orchestrating AI workflows and enabling dynamic capabilities.
  - Set up a vector database for advanced retrieval capabilities.
  - Integrate Azure AI Vision, Content Understanding, and OpenAI services to create a system capable of processing text, images, and documents.
  - Test end-to-end functionality, including retrieval and dynamic responses, within the lab notebook.

### Practical Data: Employee Handbook
- Use sample Contoso HR documents for multimodal analysis and enhanced chatbot responses.

## Assignments 📝
- **Mandatory**:
  - Complete the **lab.ipynb** notebook.  
  - Fill out the **quiz.md** to test your knowledge of Week 2’s topics.
- **Optional**:
  - Deploy the enhanced chatbot using Streamlit and Azure App Services.

> **Due Date**: Before the start of Week 3.

## Setup Instructions ⚙️

To participate effectively in this session, follow these steps to set up your environment:

### Prerequisites 📚

- **Azure Subscription**: Ensure you have an active Azure subscription. Create one [here](https://azure.microsoft.com/free/).
- **Development Tools**:
  - Install **Visual Studio Code** from [here](https://code.visualstudio.com/).
  - Install **Azure CLI** from [here](https://learn.microsoft.com/cli/azure/install-azure-cli).

### Setting Up Semantic Kernel
- **Clone Repository**: Clone the Semantic Kernel repository for examples and libraries. [Learn more](https://github.com/microsoft/semantic-kernel)
- **Install Dependencies**: Follow the repository’s instructions to set up the environment.

### Configuring Azure AI Services
- **Azure AI Vision**:
  - Create and configure a Vision Service for image analysis. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- **Azure AI Content Understanding**:
  - Set up a Content Understanding service for document analysis. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- **Azure OpenAI**:
  - Deploy an OpenAI model for reasoning and chatbot functionalities. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

Once setup is complete, you are ready for the Week 2 activities!
