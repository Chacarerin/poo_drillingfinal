# 🚀 Sistema de Gestión Jerárquica de Vehículos

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Arquitectura](https://img.shields.io/badge/Architecture-OOP-orange?style=flat-square&logo=codeigniter&logoColor=white)](#)

Este proyecto representa la consolidación final (Drilling Final) de los conceptos avanzados de Programación Orientada a Objetos. Se ha diseñado una estructura jerárquica robusta para modelar un ecosistema de vehículos con sus respectivas especificaciones, categorizaciones y comportamientos.

## 🧠 Contexto Pedagógico y Teórico
El objetivo principal de esta arquitectura es demostrar un dominio técnico sobre el diseño de sistemas basados en la herencia múltiple y la composición. Al modelar un sistema de vehículos (que puede ir desde bicicletas hasta vehículos comerciales motorizados), se aborda el problema del acoplamiento de código. Un diseño jerárquico bien planificado previene la duplicación de código y permite que el software sea extensible; agregar un nuevo tipo de vehículo en el futuro requeriría mínimos cambios estructurales.

## ⚙️ Tecnologías y Frameworks Aplicados
* **Python (Standard Library)**: Se eligió la biblioteca estándar de Python sin dependencias de terceros para demostrar que un diseño de arquitectura de software sólido no depende de frameworks, sino de una correcta abstracción y modelado de datos.
* **Paradigma OOP Puro**: Se hace uso extensivo de clases base, constructores heredados (`super()`), y encapsulamiento estricto para proteger el estado de cada vehículo.

## 🛠️ Desglose Técnico (El "Cómo")
La arquitectura se divide en la declaración de las entidades base y su consumo lógico:
* **`vehiculos.py`**: Actúa como el núcleo de la lógica de negocio. Contiene las definiciones de clases base (superclases) y clases derivadas (subclases). Maneja las propiedades inherentes (marca, modelo, número de ruedas) y comportamientos específicos de la lógica de dominio.
* **`mainX.py`**: Los scripts de ejecución actúan como puntos de entrada (Entry Points) para instanciar, inicializar el estado del ecosistema y probar las interfaces públicas de los objetos, simulando un entorno de producción o de pruebas de integración.

*Desarrollado por Rubén Schnettler.*
