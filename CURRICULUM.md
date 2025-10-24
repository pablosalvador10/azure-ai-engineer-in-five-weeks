# Azure AI Engineering in 5 Weeks - Curriculum 🚀

## 🌐 Available Languages

- [🇺🇸 English](./CURRICULUM.md) ← You are here
- [🇪🇸 Español](./CURRICULUM.es.md)

Welcome to the Azure AI Engineering in 5 Weeks curriculum. This guide will help you navigate through the weekly lessons, labs, and quizzes designed to enhance your skills in Azure AI services.

# Table of Contents 📅
- [Week 1: Introduction to Azure AI Services 📘](#week-1-introduction-to-azure-ai-services-📘)
- [Week 2: Designing Intelligent Cloud-Native AI Systems 🏗️](#week-2-designing-intelligent-cloud-native-ai-systems-🏗️)
- [Week 3: Operationalizing and Managing AI Solutions ⚙️](#week-3-operationalizing-and-managing-ai-solutions-⚙️)
- [Week 4: Advanced Optimization and Fine-Tuning of AI Systems 🔧](#week-4-advanced-optimization-and-fine-tuning-of-ai-systems-🔧)
- [Week 5: Building Autonomous AI Systems (Agents) 🤖](#week-5-building-autonomous-ai-systems-agents-🤖)

# Week by Week 📅

## Week 1: Introduction to Azure AI Services 📘
### Topics
- **Overview of Azure AI Services**:
  - Azure AI Foundry: Learn how to use the most comprehensive AI platform.
  - Azure OpenAI Service: Leverage large language models for NLP tasks.
  - Azure AI Search: Implement AI-powered search within applications.
  - Azure AI Document Intelligence: Process and extract information from documents.
  - Azure AI Vision Services: Image and video analysis tools.
  - Azure AI Speech Services: Speech recognition and synthesis functionalities.
- **Introduction to Retrieval-Augmented Generation (RAG) Patterns**:
  - Combining retrieval-based methods with generative AI for enhanced performance.
  - Implementing basic RAG architectures using Azure services.

### Practical Session
- **Building Your First Chatbot**:
  - Configure necessary Azure services.
  - Develop a chatbot using Azure AI Search and Azure OpenAI through the Azure AI Foundry portal’s UI.

### Homework
- **Lab**: Complete the `lab.ipynb` notebook to practice building and refining your first chatbot.  
- **Quiz**: Test your understanding by filling out the `quiz.md` file for Week 1.  
- **Reinforcement**:  
  - Upload sample data (Contoso HR documents) and index it using Azure AI Search.  
  - Implement hybrid search, combining vector-based and keyword-based retrieval.  
  - Enable question-answering capabilities using Azure OpenAI as the reasoning engine.

> **Note**: For setup and detailed instructions, refer to the [Week 1 README](./weeks/week-1/README.md).

---

## Week 2: Designing Intelligent Cloud-Native AI Systems 🏗️

### Topics
- **Introduction to Orchestration Frameworks**:
  - **Semantic Kernel**: Explore Microsoft's open-source framework that facilitates the integration of large language models (LLMs) with conventional programming languages, enabling the creation and orchestration of complex AI solutions.
- **Enhancing Chatbot Functionality with Multimodality**:
  - **Multimodal AI Integration**: Learn how to extend your chatbot's capabilities by incorporating multiple data types, such as text, images, and documents, to provide richer and more context-aware interactions.
- **Vector Database in Azure**:
  - **Azure AI Search**: Dive into building a vector-based data store using Azure AI Search, learning how to efficiently index and search data with integrated vectorization.

### Practical Session
- **Upgrading Your Chatbot with Semantic Kernel**:
  - **Integration**: Rebuild the chatbot developed in Week 1 by incorporating Semantic Kernel as the orchestrator, allowing for seamless interaction between various AI services and data modalities.
  - **Multimodal Capabilities**: Enhance the chatbot to process and respond to inputs beyond text, such as images and documents, utilizing Azure AI Services.
  - **Vector Search**: Integrate a vector database for storing and retrieving embeddings, enabling efficient multimodal search capabilities.
- **Building a Front-End with Streamlit**:
  - **User Interaction**: Develop a streamlined interface using Streamlit that communicates with the backend, showcasing the chatbot's enhanced multimodal capabilities.

### Homework
- **Lab**: Work through the `lab.ipynb` notebook to integrate multimodal features and vector search into your chatbot.  
- **Quiz**: Complete the Week 2 `quiz.md` to assess key takeaways and ensure understanding of newly introduced concepts.  
- **Reinforcement**:
  - Extend your chatbot to handle at least two data modalities (e.g., image and document) with Semantic Kernel and Azure AI Services.  
  - Build and query a vector database in Azure AI Search for storing embeddings and performing efficient searches.  
  - **Advanced (Optional)**: Deploy the chatbot using the Semantic Kernel framework and Streamlit, containerized with Azure App Services or Azure Container Apps.

> **Note**: For setup and detailed instructions, refer to the [Week 2 README](./weeks/week-2/README.md).

---

## Week 3: Operationalizing and Managing AI Solutions ⚙️
### Topics
- **Transition from MLOps to LLMOps**:
  - Understanding the lifecycle of large language models in production.
  - Implementing best practices for deployment and maintenance.
- **Monitoring and Management**:
  - Utilizing Azure Monitor, Log Analytics, and KQL for system observability.
  - Setting up end-to-end monitoring with OpenTelemetry and correlation IDs.
- **Continuous Evaluation and Benchmarking**:
  - Establishing frameworks for ongoing model assessment.
  - Using Azure AI Studio for evaluation and tracing.

### Practical Session
- **Implementing LLMOps Practices**:
  - Set up CI/CD pipelines with GitHub Actions for automated deployments.
  - Configure monitoring tools to track system performance.
  - Implement data drift detection and automated retraining workflows.

### Homework
- **Lab**: Follow the `lab.ipynb` notebook to add monitoring and management capabilities to your AI system.  
- **Quiz**: Answer the Week 3 quiz in `quiz.md`, focusing on operational best practices for AI systems.  
- **Reinforcement**:  
  - Establish comprehensive monitoring and evaluation for your AI solution.  
  - Implement an enterprise-grade evaluation framework within your RAG pattern.  
  - **Optional**: Integrate multimodal evaluation to monitor diverse data types effectively.

> **Note**: For setup and detailed instructions, refer to the [Week 3 README](./weeks/week-3/README.md).

---

## Week 4: Advanced Optimization and Fine-Tuning of AI Systems 🔧
### Topics
- **Designing Scalable AI Systems**:
  - Architectural patterns for scalability in AI solutions.
  - Leveraging Azure's infrastructure to support large-scale AI deployments.
- **Leveraging Small Language Models**:
  - Introduction to small language models and their applications.
  - Understanding the Phi-4 architecture and its benefits.
- **Fine-Tuning Large Language Models (LLMs)**:
  - Techniques for customizing LLMs for specific domain tasks.
  - Tools and resources available in Azure for model fine-tuning.
- **Enhancing RAG Pattern Performance**:
  - Methods to reduce latency and improve accuracy in RAG implementations.
  - Case studies demonstrating performance optimization.

### Practical Session
- **Fine-Tuning an Azure OpenAI Model**:
  - Hands-on experience in customizing an OpenAI model within Azure.
  - Evaluating performance improvements post fine-tuning.

### Homework
- **Lab**: Use the `lab.ipynb` notebook to fine-tune an Azure OpenAI model and analyze the performance improvements.  
- **Quiz**: Check your knowledge by completing the Week 4 `quiz.md`, focusing on optimization strategies.  
- **Reinforcement**:  
  - Submit a detailed analysis of your results, highlighting performance gains.  
  - **Optional**: Compare the fine-tuned model with a baseline to assess the impact of your optimizations.

> **Note**: For setup and detailed instructions, refer to the [Week 4 README](./weeks/week-4/README.md).

---

## Week 5: Building Autonomous AI Systems (Agents) 🤖
### Topics
- **Understanding Agent Architectures**:
  - **Single-Agent Systems**: Explore the structure and functionality of standalone AI agents, including their decision-making processes and applications.
  - **Multi-Agent Systems**: Delve into systems where multiple AI agents interact, collaborate, or compete to achieve individual or collective goals.

- **Designing Multi-Agent System Architectures on Azure**:
  - **System Design**: Learn to architect multi-agent applications using Azure services, ensuring scalability, security, and efficiency.
  - **Communication Protocols**: Understand the methods and protocols that facilitate effective communication between agents.
  - **Coordination Strategies**: Study strategies for coordinating tasks among agents to optimize performance and resource utilization.

- **Quickstart: Building Agents in Azure**:
  - **Azure AI Agent Service**: Introduction to Azure's fully managed service for building, orchestrating, and scaling AI agents.
  - **Development Tools**: Overview of tools like Azure AI Foundry and Azure AI Studio for agent development.
  - **Deployment Best Practices**: Guidelines for deploying AI agents in production environments, focusing on reliability and performance.

### Practical Session
- **Prototyping a Multi-Agent System**:
  - **Integration with RAG Patterns**: Implement a multi-agent system that utilizes Retrieval-Augmented Generation (RAG) to enhance information retrieval and response generation.
  - **Agent Collaboration**: Set up agents with distinct roles that collaborate to complete complex tasks, demonstrating effective inter-agent communication.
  - **Azure Services Utilization**: Leverage Azure AI Agent Service and other relevant Azure services to build and deploy your multi-agent system.

### Homework
- **Lab**: Work through the `lab.ipynb` to develop a multi-agent system that integrates RAG patterns and demonstrates agent collaboration.  
- **Quiz**: Update your progress by filling out the Week 5 `quiz.md`, focusing on agent-based architectures and their practical applications.  
- **Reinforcement**:  
  - Provide comprehensive documentation detailing the system architecture, agent roles, communication protocols, and deployment process.  
  - Prepare a demo that illustrates the functionality and effectiveness of your multi-agent system.  
  - **Optional**: Investigate and implement advanced features such as additional data modalities or enhanced agent learning capabilities.

> **Note**: For setup and detailed instructions, refer to the [Week 5 README](./weeks/week-5/README.md).