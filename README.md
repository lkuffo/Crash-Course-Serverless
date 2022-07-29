# Crash Course: Serverless

![](https://user-images.githubusercontent.com/2752551/30404911-d575539c-989d-11e7-9a74-df8533b95c6d.png)

## Introducción 
Como parte de este curso vamos a desarrollar tres funciones con Serverless Computing. Cada función contará con tests unitarios y despliegue automático en un ambiente de AWS. Finalmente, se realizan tests de integración automáticos. 


## Pre-requisitos
- **Git**: Necesitaremos Git para realizar cambios en sus repositorios de GitHub.
- **Python 3.x**: Necesitaremos Python 3 para realizar pruebas al código que escribamos.


## Funciones Lambda
Desarrollaremos tres funciones lambda:
- Una funcion que sirva una pagina web, accesible a traves de una URL pública. Para ello utilizaremos AWS Lambda + Serverless Framework + Python Flask.
- Una funcion que ejecute una suma de dos numeros, accesible a traves de una URL publica. Para ello utilizaremos AWS Lambda + Serverless Framework + Python.
- Una funcion que realice un proceso bajo horario en repeticion. Para ello utilizaremos AWS Lambda + Event Bridge + Serverless Framework + Python.


## Ambiente AWS
El ambiente AWS en el cual se van a desplegar las funciones provee a los asistentes de lo siguiente:
- **Cuenta IAM**: Para poder tener acceso al ambiente AWS. Esta cuenta tiene permisos para: Manipular Funciones Lambda y Event Bridge, Leer logs de CloudWatch, Leer Configuraciones de Red.
- **VPC y Networking**: Las funciones lambda por defecto no tienen acceso a internet, ni tampoco se puede acceder a ellas por defecto. Por lo que se proporciona una VPC, con Subnets y grupos de seguridad propicios para cambiar estas configuraciones por defecto.
- Region a utilizar: us-east-1

## CI/CD: Github Actions
El repositorio contiene tres acciones de GitHub que van de la mano con practicas de CI/CD para el manejo de nuestro software
1. Test Unitarios:
2. Despliegue con Serverless Framework: . Es decir, no realizaremos ningún despliegue localmente.
3. Test de Integración:


## Agenda 
### Parte teórica (45m)
- On Premise Computing
- Cluster Computing
- Super Computing
- Grid Computing
- Cloud Computing: Introducción
- Cloud Computing: Ventajas y Desventajas
- Cloud Computing: Proveedores
- Cloud Computing: Cómo funciona?
- Web Services: Introducción
- Web Services: Arquitecturas orientadas a Servicios
- Web Services: Microservicios
- AWS: Introducción
- AWS: Stack
- AWS: Arquitectura de una aplicación Web
- Serverless Computing
- Serverless Framework
- DevOps: Introducción 
- DevOps vs Agile vs Traditional
- DevOps: CI/CD
- DevOps: CI/CD con GitHub Actions

### Parte Práctica (1h 30m)
- Clonar Repositorio (Git) (5m)
- Codificación de Funciones Lambda (Python 3.x) (15m)
- Codificación de Pruebas Unitaria (5m) 
- Configuración de archivo serverless.yml para el despliegue de Funciones Lambda + Despliegue en AWS + Explicación del Stack AWS (30m) 
- Pruebas de las Funciónes Lambda + Explicaciones (10m)
- Configuración de GitHub action + Pruebas + Explicación (15m) 
- Prueba de Integración (10m)

