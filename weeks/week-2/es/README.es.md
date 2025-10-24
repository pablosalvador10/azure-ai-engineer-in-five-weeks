# Semana 2: Diseñando Sistemas de IA Inteligentes Nativos de la Nube 🛠️

## 🌐 Idiomas Disponibles

- [🇺🇸 English](./README.md)
- [🇪🇸 Español](./README.es.md) ← Estás aquí

## Tabla de Contenidos 📑
- [Descripción General](#descripción-general-📋)
- [Objetivos de Aprendizaje](#objetivos-de-aprendizaje-🎯)
- [Prerrequisitos](#prerrequisitos-📚)
- [Materiales](#materiales-📂)
- [Actividades en Clase](#actividades-en-clase-🛠️)
- [Tareas](#tareas-📝)
- [Instrucciones de Configuración](#instrucciones-de-configuración-⚙️)

## Descripción General 📋
En la Semana 2, nos enfocamos en avanzar tu conocimiento de Azure AI explorando frameworks de orquestación como **Semantic Kernel** de Microsoft. También aprenderás cómo mejorar la funcionalidad del chatbot con integración de IA multimodal, habilitando el procesamiento de múltiples tipos de datos como texto, imágenes y documentos.

### Definiendo el Framework del Sistema de IA:
Esta semana introduce el concepto de un **Sistema de IA** como un sistema compuesto donde el **Modelo de Lenguaje Grande (LLM)** actúa como el motor central de procesamiento y razonamiento, orquestando de manera fluida llamadas a múltiples servicios de Azure AI. Demostraremos esto construyendo un **sistema de Generación Aumentada por Recuperación (RAG)** que integra varios servicios y capacidades en un pipeline unificado.

#### ¿Qué es RAG?
**Generación Aumentada por Recuperación (RAG)** es un patrón de diseño de sistema que combina recuperación de información (recuperar datos relevantes de fuentes estructuradas o no estructuradas) con generación (aprovechando LLMs para sintetizar y responder a consultas de usuarios). Este patrón asegura:
- Respuestas contextuales y precisas fundamentando el LLM en datos del mundo real.
- Rendimiento mejorado al estrechar el alcance de las tareas generativas a través de evidencia recuperada.

### Enfoque Clave:
- **Indexación y Personalización Pro-Código**: Mejoramos el chatbot de la Semana 1 implementando indexación avanzada dirigida por código en Azure AI Search. Esto proporciona flexibilidad y precisión en la gestión de pipelines de búsqueda y recuperación.
- **Integración de Semantic Kernel**: Aprovechando las capacidades de orquestación de Semantic Kernel, unificamos múltiples servicios, incluyendo Azure AI Vision, Content Understanding y Azure OpenAI, habilitando capacidades de IA multimodal.
- **Diseño de Sistema Dinámico**: El sistema de IA está diseñado para adaptar dinámicamente su uso de LLM y estrategias de recuperación basadas en consultas de usuario y contexto, ejemplificando una arquitectura altamente escalable y eficiente.

Esta sesión práctica te equipa con las herramientas y conocimiento para construir y operacionalizar un sistema de IA nativo de la nube, mostrando el poder de **Semantic Kernel** en orquestar servicios de Azure AI para crear soluciones inteligentes y escalables.

## Objetivos de Aprendizaje 🎯
- **Dominar Frameworks de Orquestación con Semantic Kernel**: Obtén una comprensión profunda de cómo Semantic Kernel de Microsoft habilita coordinación fluida de múltiples servicios de Azure AI para construir sistemas de IA escalables e inteligentes. 
- **Construir una Base de Datos Vectorial en Azure**: Crea y gestiona un almacén de datos basado en vectores aprovechando Azure AI Search, utilizando vectorización integrada para indexación y búsqueda eficientes.  
- **Habilitar Multimodalidad en tu Chatbot**: Incorpora texto, imágenes y otros tipos de datos para proporcionar una experiencia de usuario más rica y dinámica.  
- **Construir un Framework de Orquestación de Backend**: Establece una arquitectura robusta que coordine servicios y tareas para nuestro chatbot.  
- **Desarrollar un Front-End con Streamlit**: Implementa una interfaz optimizada que interactúe con microservicios y componentes de backend, facilitando una solución de IA completamente funcional.

## Prerrequisitos 📚
Para aprovechar al máximo esta sesión, deberías tener:

 - **Materiales de la Semana 1**: Revisa conceptos fundamentales y servicios de la Semana 1, incluyendo Azure AI Foundry, OpenAI y Azure AI Search. [Más información](./weeks/week-1/README.md)

- **Experiencia en la Nube y Azure**:
  - Experiencia práctica con servicios de Azure, incluyendo crear y gestionar recursos.
  - Conocimiento básico de servicios de Azure AI como Azure AI Search, OpenAI, Vision y Content Understanding, como se introdujo en la Semana 1.

- **Acceso Requerido**:
  - Suscripción activa de Azure con permisos para desplegar y usar servicios de IA.

## Materiales 📂
- **Diapositivas**: [Enlace a las diapositivas de presentación]
- **Lecturas**:
  - **Introducción a Semantic Kernel**: Aprende cómo orquestar servicios de IA de manera efectiva. [Más información](https://learn.microsoft.com/en-us/semantic-kernel/overview)
  - **Integración de IA Multimodal**: Explora técnicas para manejar múltiples tipos de datos. [Más información](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
  - **Mejorando Sistemas de IA con Azure**: Tutoriales sobre integración de servicios de Azure AI. [Más información](https://learn.microsoft.com/en-us/azure/ai-services/)
- **Recursos Adicionales**:
  - **Servicios de Visión de Azure AI**: Herramientas para análisis de imágenes y videos. [Más información](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
  - **Azure AI Content Understanding**: Análisis avanzado de documentos. [Más información](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
 
> Asegúrate de estar cómodo con la implementación del chatbot de la Semana 1, ya que forma la línea base para las mejoras de esta semana.

## Actividades en Clase 🛠️
Esta sesión incluye una actividad práctica grupal para recorrer el notebook **lab.ipynb** juntos:
  - Aprende sobre el diseño de sistemas escalables y modulares usando microservicios en Azure.
  - Explora el papel de Semantic Kernel en orquestar flujos de trabajo de IA y habilitar capacidades dinámicas.
  - Configura una base de datos vectorial para capacidades de recuperación avanzadas.
  - Integra Azure AI Vision, Content Understanding y servicios OpenAI para crear un sistema capaz de procesar texto, imágenes y documentos.
  - Prueba funcionalidad de extremo a extremo, incluyendo recuperación y respuestas dinámicas, dentro del notebook de laboratorio.

### Datos Prácticos: Manual del Empleado
- Usa documentos de muestra de RRHH de Contoso para análisis multimodal y respuestas mejoradas del chatbot.

## Tareas 📝
- **Obligatorio**:
  - Completa el notebook **lab.ipynb**.  
  - Completa el **quiz.md** para probar tu conocimiento de los temas de la Semana 2.
- **Opcional**:
  - Despliega el chatbot mejorado usando Streamlit y Azure App Services.

> **Fecha de Entrega**: Antes del inicio de la Semana 3.

## Instrucciones de Configuración ⚙️

Para participar efectivamente en esta sesión, sigue estos pasos para configurar tu entorno:

### Prerrequisitos 📚

- **Suscripción de Azure**: Asegúrate de tener una suscripción activa de Azure. Crea una [aquí](https://azure.microsoft.com/free/).
- **Herramientas de Desarrollo**:
  - Instala **Visual Studio Code** desde [aquí](https://code.visualstudio.com/).
  - Instala **Azure CLI** desde [aquí](https://learn.microsoft.com/cli/azure/install-azure-cli).

### Configurando Semantic Kernel
- **Clonar Repositorio**: Clona el repositorio de Semantic Kernel para ejemplos y librerías. [Más información](https://github.com/microsoft/semantic-kernel)
- **Instalar Dependencias**: Sigue las instrucciones del repositorio para configurar el entorno.

### Configurando Servicios de Azure AI
- **Azure AI Vision**:
  - Crea y configura un Servicio de Visión para análisis de imágenes. [Más información](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- **Azure AI Content Understanding**:
  - Configura un servicio de Content Understanding para análisis de documentos. [Más información](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- **Azure OpenAI**:
  - Despliega un modelo OpenAI para razonamiento y funcionalidades de chatbot. [Más información](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

¡Una vez completada la configuración, estarás listo para las actividades de la Semana 2!