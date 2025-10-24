# Ingeniería de IA de Azure en 5 Semanas - Currículo 🚀

Bienvenido al currículo de Ingeniería de IA de Azure en 5 Semanas. Esta guía te ayudará a navegar por las lecciones semanales, laboratorios y cuestionarios diseñados para mejorar tus habilidades en los servicios de IA de Azure.

## 🌐 Idiomas Disponibles

- [🇺🇸 English](./CURRICULUM.md)
- [🇪🇸 Español](./CURRICULUM.es.md) ← Estás aquí

# Tabla de Contenidos 📅
- [Semana 1: Introducción a los Servicios de IA de Azure 📘](#semana-1-introducción-a-los-servicios-de-ia-de-azure-📘)
- [Semana 2: Diseñando Sistemas de IA Inteligentes Nativos de la Nube 🏗️](#semana-2-diseñando-sistemas-de-ia-inteligentes-nativos-de-la-nube-🏗️)
- [Semana 3: Operacionalización y Gestión de Soluciones de IA ⚙️](#semana-3-operacionalización-y-gestión-de-soluciones-de-ia-⚙️)
- [Semana 4: Optimización Avanzada y Ajuste Fino de Sistemas de IA 🔧](#semana-4-optimización-avanzada-y-ajuste-fino-de-sistemas-de-ia-🔧)
- [Semana 5: Construyendo Sistemas de IA Autónomos (Agentes) 🤖](#semana-5-construyendo-sistemas-de-ia-autónomos-agentes-🤖)

# Semana por Semana 📅

## Semana 1: Introducción a los Servicios de IA de Azure 📘
### Temas
- **Descripción General de los Servicios de IA de Azure**:
  - Azure AI Foundry: Aprende a usar la plataforma de IA más completa.
  - Servicio Azure OpenAI: Aprovecha los modelos de lenguaje grandes para tareas de PLN.
  - Azure AI Search: Implementa búsqueda potenciada por IA dentro de aplicaciones.
  - Azure AI Document Intelligence: Procesa y extrae información de documentos.
  - Servicios de Visión de Azure AI: Herramientas de análisis de imágenes y videos.
  - Servicios de Voz de Azure AI: Funcionalidades de reconocimiento y síntesis de voz.
- **Introducción a los Patrones de Generación Aumentada por Recuperación (RAG)**:
  - Combinando métodos basados en recuperación con IA generativa para un rendimiento mejorado.
  - Implementando arquitecturas RAG básicas usando servicios de Azure.

### Sesión Práctica
- **Construyendo tu Primer Chatbot**:
  - Configurar los servicios de Azure necesarios.
  - Desarrollar un chatbot usando Azure AI Search y Azure OpenAI a través de la interfaz de usuario del portal Azure AI Foundry.

### Tarea
- **Laboratorio**: Completa el notebook `lab.ipynb` para practicar la construcción y refinamiento de tu primer chatbot.  
- **Cuestionario**: Prueba tu comprensión completando el archivo `quiz.md` para la Semana 1.  
- **Refuerzo**:  
  - Sube datos de muestra (documentos de RRHH de Contoso) e indexa usando Azure AI Search.  
  - Implementa búsqueda híbrida, combinando recuperación basada en vectores y palabras clave.  
  - Habilita capacidades de respuesta a preguntas usando Azure OpenAI como motor de razonamiento.

> **Nota**: Para configuración e instrucciones detalladas, consulta el [README de la Semana 1](./weeks/week-1/README.md).

---

## Semana 2: Diseñando Sistemas de IA Inteligentes Nativos de la Nube 🏗️

### Temas
- **Introducción a Frameworks de Orquestación**:
  - **Semantic Kernel**: Explora el framework de código abierto de Microsoft que facilita la integración de modelos de lenguaje grandes (LLMs) con lenguajes de programación convencionales, permitiendo la creación y orquestación de soluciones de IA complejas.
- **Mejorando la Funcionalidad del Chatbot con Multimodalidad**:
  - **Integración de IA Multimodal**: Aprende cómo extender las capacidades de tu chatbot incorporando múltiples tipos de datos, como texto, imágenes y documentos, para proporcionar interacciones más ricas y conscientes del contexto.
- **Base de Datos Vectorial en Azure**:
  - **Azure AI Search**: Sumérgete en la construcción de un almacén de datos basado en vectores usando Azure AI Search, aprendiendo cómo indexar y buscar datos de manera eficiente con vectorización integrada.

### Sesión Práctica
- **Actualizando tu Chatbot con Semantic Kernel**:
  - **Integración**: Reconstruye el chatbot desarrollado en la Semana 1 incorporando Semantic Kernel como orquestador, permitiendo interacción fluida entre varios servicios de IA y modalidades de datos.
  - **Capacidades Multimodales**: Mejora el chatbot para procesar y responder a entradas más allá del texto, como imágenes y documentos, utilizando los Servicios de IA de Azure.
  - **Búsqueda Vectorial**: Integra una base de datos vectorial para almacenar y recuperar embeddings, habilitando capacidades de búsqueda multimodal eficientes.
- **Construyendo un Front-End con Streamlit**:
  - **Interacción del Usuario**: Desarrolla una interfaz optimizada usando Streamlit que se comunica con el backend, mostrando las capacidades multimodales mejoradas del chatbot.

### Tarea
- **Laboratorio**: Trabaja con el notebook `lab.ipynb` para integrar características multimodales y búsqueda vectorial en tu chatbot.  
- **Cuestionario**: Completa el `quiz.md` de la Semana 2 para evaluar los puntos clave y asegurar la comprensión de los conceptos recién introducidos.  
- **Refuerzo**:
  - Extiende tu chatbot para manejar al menos dos modalidades de datos (ej., imagen y documento) con Semantic Kernel y Servicios de IA de Azure.  
  - Construye y consulta una base de datos vectorial en Azure AI Search para almacenar embeddings y realizar búsquedas eficientes.  
  - **Avanzado (Opcional)**: Despliega el chatbot usando el framework Semantic Kernel y Streamlit, containerizado con Azure App Services o Azure Container Apps.

> **Nota**: Para configuración e instrucciones detalladas, consulta el [README de la Semana 2](./weeks/week-2/README.es.md).

---

## Semana 3: Operacionalización y Gestión de Soluciones de IA ⚙️
### Temas
- **Transición de MLOps a LLMOps**:
  - Comprendiendo el ciclo de vida de los modelos de lenguaje grandes en producción.
  - Implementando mejores prácticas para despliegue y mantenimiento.
- **Monitoreo y Gestión**:
  - Utilizando Azure Monitor, Log Analytics y KQL para observabilidad del sistema.
  - Configurando monitoreo de extremo a extremo con OpenTelemetry e IDs de correlación.
- **Evaluación Continua y Benchmarking**:
  - Estableciendo frameworks para evaluación continua del modelo.
  - Usando Azure AI Studio para evaluación and seguimiento.

### Sesión Práctica
- **Implementando Prácticas LLMOps**:
  - Configurar pipelines CI/CD con GitHub Actions para despliegues automatizados.
  - Configurar herramientas de monitoreo para rastrear el rendimiento del sistema.
  - Implementar detección de drift de datos y workflows de reentrenamiento automatizado.

### Tarea
- **Laboratorio**: Sigue el notebook `lab.ipynb` para agregar capacidades de monitoreo y gestión a tu sistema de IA.  
- **Cuestionario**: Responde el cuestionario de la Semana 3 en `quiz.md`, enfocándose en mejores prácticas operacionales para sistemas de IA.  
- **Refuerzo**:  
  - Establece monitoreo y evaluación comprensivos para tu solución de IA.  
  - Implementa un framework de evaluación de nivel empresarial dentro de tu patrón RAG.  
  - **Opcional**: Integra evaluación multimodal para monitorear diversos tipos de datos de manera efectiva.

> **Nota**: Para configuración e instrucciones detalladas, consulta el [README de la Semana 3](./weeks/week-3/README.md).

---

## Semana 4: Optimización Avanzada y Ajuste Fino de Sistemas de IA 🔧
### Temas
- **Diseñando Sistemas de IA Escalables**:
  - Patrones arquitectónicos para escalabilidad en soluciones de IA.
  - Aprovechando la infraestructura de Azure para soportar despliegues de IA a gran escala.
- **Aprovechando Modelos de Lenguaje Pequeños**:
  - Introducción a modelos de lenguaje pequeños y sus aplicaciones.
  - Comprendiendo la arquitectura Phi-4 y sus beneficios.
- **Ajuste Fino de Modelos de Lenguaje Grandes (LLMs)**:
  - Técnicas para personalizar LLMs para tareas de dominio específico.
  - Herramientas y recursos disponibles en Azure para ajuste fino de modelos.
- **Mejorando el Rendimiento del Patrón RAG**:
  - Métodos para reducir latencia y mejorar precisión en implementaciones RAG.
  - Estudios de caso demostrando optimización de rendimiento.

### Sesión Práctica
- **Ajuste Fino de un Modelo Azure OpenAI**:
  - Experiencia práctica en personalizar un modelo OpenAI dentro de Azure.
  - Evaluando mejoras de rendimiento post ajuste fino.

### Tarea
- **Laboratorio**: Usa el notebook `lab.ipynb` para ajustar finamente un modelo Azure OpenAI y analizar las mejoras de rendimiento.  
- **Cuestionario**: Verifica tu conocimiento completando el `quiz.md` de la Semana 4, enfocándose en estrategias de optimización.  
- **Refuerzo**:  
  - Envía un análisis detallado de tus resultados, destacando ganancias de rendimiento.  
  - **Opcional**: Compara el modelo ajustado finamente con una línea base para evaluar el impacto de tus optimizaciones.

> **Nota**: Para configuración e instrucciones detalladas, consulta el [README de la Semana 4](./weeks/week-4/README.md).

---

## Semana 5: Construyendo Sistemas de IA Autónomos (Agentes) 🤖
### Temas
- **Comprendiendo Arquitecturas de Agentes**:
  - **Sistemas de Agente Único**: Explora la estructura y funcionalidad de agentes de IA independientes, incluyendo sus procesos de toma de decisiones y aplicaciones.
  - **Sistemas Multi-Agente**: Profundiza en sistemas donde múltiples agentes de IA interactúan, colaboran o compiten para lograr metas individuales o colectivas.

- **Diseñando Arquitecturas de Sistemas Multi-Agente en Azure**:
  - **Diseño de Sistemas**: Aprende a arquitecturar aplicaciones multi-agente usando servicios de Azure, asegurando escalabilidad, seguridad y eficiencia.
  - **Protocolos de Comunicación**: Comprende los métodos y protocolos que facilitan comunicación efectiva entre agentes.
  - **Estrategias de Coordinación**: Estudia estrategias para coordinar tareas entre agentes para optimizar rendimiento y utilización de recursos.

- **Inicio Rápido: Construyendo Agentes en Azure**:
  - **Servicio de Agentes de IA de Azure**: Introducción al servicio completamente gestionado de Azure para construir, orquestar y escalar agentes de IA.
  - **Herramientas de Desarrollo**: Descripción general de herramientas como Azure AI Foundry y Azure AI Studio para desarrollo de agentes.
  - **Mejores Prácticas de Despliegue**: Directrices para desplegar agentes de IA en entornos de producción, enfocándose en confiabilidad y rendimiento.

### Sesión Práctica
- **Prototipando un Sistema Multi-Agente**:
  - **Integración con Patrones RAG**: Implementa un sistema multi-agente que utiliza Generación Aumentada por Recuperación (RAG) para mejorar la recuperación de información y generación de respuestas.
  - **Colaboración de Agentes**: Configura agentes con roles distintos que colaboran para completar tareas complejas, demostrando comunicación efectiva entre agentes.
  - **Utilización de Servicios de Azure**: Aprovecha el Servicio de Agentes de IA de Azure y otros servicios relevantes de Azure para construir y desplegar tu sistema multi-agente.

### Tarea
- **Laboratorio**: Trabaja con el `lab.ipynb` para desarrollar un sistema multi-agente que integra patrones RAG y demuestra colaboración de agentes.  
- **Cuestionario**: Actualiza tu progreso completando el `quiz.md` de la Semana 5, enfocándose en arquitecturas basadas en agentes y sus aplicaciones prácticas.  
- **Refuerzo**:  
  - Proporciona documentación comprensiva detallando la arquitectura del sistema, roles de agentes, protocolos de comunicación y proceso de despliegue.  
  - Prepara una demo que ilustre la funcionalidad y efectividad de tu sistema multi-agente.  
  - **Opcional**: Investiga e implementa características avanzadas como modalidades de datos adicionales o capacidades de aprendizaje de agentes mejoradas.

> **Nota**: Para configuración e instrucciones detalladas, consulta el [README de la Semana 5](./weeks/week-5/README.md).