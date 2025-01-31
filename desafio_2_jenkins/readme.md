# Desafío 2: Jenkins

## Descripción

Este desafío está enfocado en la implementación de una pipeline de Integración Continua/Despliegue Continuo (CI/CD) utilizando Jenkins. El objetivo es automatizar el proceso de construcción, prueba y despliegue de una aplicación, asegurando una entrega eficiente y confiable.

## Contenido

El desafío abarca los siguientes temas:

- **Instalación y configuración de Jenkins**: Implementación de Jenkins en un entorno local o en un servidor remoto.
- **Creación de pipelines**: Definición y configuración de pipelines para automatizar procesos de construcción y despliegue.
- **Integración con sistemas de control de versiones**: Conexión de Jenkins con repositorios como GitHub para monitorear cambios en el código fuente.
- **Automatización de pruebas**: Ejecución de pruebas automatizadas para garantizar la calidad del código antes del despliegue.
- **Despliegue automatizado**: Implementación de estrategias para desplegar automáticamente la aplicación en diferentes entornos.

## Requisitos

- Instancia de Jenkins instalada y configurada.
- Acceso a un repositorio de código fuente (por ejemplo, en GitHub).
- Conocimientos básicos de pipelines y scripts de Jenkins.

## Instrucciones

1. **Clonar este repositorio en tu máquina local**:
   ```bash
   git clone https://github.com/jcavaiuolo/devOpsRepo.git
   ```
2. **Navegar al directorio del desafío 2**:
   ```bash
   cd devOpsRepo/desafio_2_jenkins
   ```
3. **Configurar Jenkins**:
   - Crear una nueva tarea en Jenkins y configurar el repositorio clonado como fuente.
   - Definir una pipeline que incluya etapas de construcción, prueba y despliegue según las necesidades de la aplicación.
4. **Ejecutar la pipeline**:
   - Iniciar la pipeline y monitorear cada etapa para asegurar su correcta ejecución.
   - Verificar que la aplicación se despliegue correctamente al finalizar la pipeline.

## Recursos adicionales

- [Documentación oficial de Jenkins](https://www.jenkins.io/doc/)
- [Guía de pipelines de Jenkins](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
