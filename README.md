# README - Sistema de Recopilación de Información de Propiedades
## Introducción al Proyecto
Este proyecto desarrolla un sistema integral para la recopilación, gestión y análisis de información sobre propiedades, dirigido principalmente al sector inmobiliario de los Alpes. Utiliza prácticas avanzadas de ingeniería de software, como el Diseño Guiado por el Dominio (DDD), para crear un modelo robusto que facilita la administración eficiente de datos sobre compañías, inquilinos, contratos, transacciones, localización, y más. El sistema se apoya en varios contextos acotados para separar claramente las distintas áreas de interés y facilitar el desarrollo, mantenimiento, y escalabilidad del software.

El proyecto integra datos tanto internos como de terceros (por ejemplo, Rues, Google Maps, IGAC), para proporcionar una vista completa y precisa de las propiedades, mejorando así la toma de decisiones y la capacidad de análisis comparativo de ventas y alquileres. Su arquitectura flexible permite adaptarse a las necesidades cambiantes del mercado y a diferentes regulaciones locales.

## Estructura del proyecto
La imagen Alpes AS-IS.jpg pertenece al el flujo de “Adquisición y enriquecimiento de datos automatizado” AS-IS usando el método EventStorming

La imagen Alpes TO-BE.jpg pertenece al el flujo de “Adquisición y enriquecimiento de datos automatizado” TO-BE usando el método EventStorming

En la carpeta as_is que contiene el mapa de contexto (as_is_context_map.cml) y la estructura de dominio (as_is_domains.cml) de la arquitectura actual del proyecto.

En la carpeta to_be que contiene el mapa de contexto (to_be_context_map.cml) y la estructura de dominio (to_be_domains.cml) de la arquitectura desesada del proyecto.

En la carpeta src-gen se almacenaron las imagenes generadas de los mapas de contexto.



## Cómo Instalar Context Mapper
Context Mapper es una herramienta de modelado para DDD y arquitecturas de microservicios, que facilita la especificación y visualización de contextos acotados y sus relaciones. A continuación, se detalla cómo instalarlo y configurarlo para su uso:

### Requisitos Previos
Java JDK 11 o superior instalado en su sistema.
Un IDE que soporte Context Mapper, como Eclipse o Visual Studio Code.
Pasos de Instalación
Descargar Context Mapper: Visita la página oficial de Context Mapper y descarga la última versión compatible con tu IDE. Para usuarios de Eclipse, Context Mapper se puede instalar directamente desde el Eclipse Marketplace.

### Instalación en Eclipse:

* Abre Eclipse y navega a Help > Eclipse Marketplace....
* Busca "Context Mapper" y sigue las instrucciones para instalarlo.
### Instalación en Visual Studio Code:

* Asegúrate de tener instalada la extensión Java Extension Pack.
* Busca "Context Mapper" en la sección de extensiones y instálalo.
* Configuración Inicial
* Después de instalar Context Mapper, reinicia tu IDE para completar la configuración. No se requieren pasos adicionales específicos; Context Mapper estará listo para usar con los proyectos existentes o nuevos.

## Cómo Usar Context Mapper en GitPod
GitPod ofrece un entorno de desarrollo basado en la nube, permitiendo trabajar con proyectos desde cualquier navegador. Para usar Context Mapper en GitPod:

* Instala la extencion de gitpod en chrome o Abre el proyecto en un workspace de gitpod 
* El proyecto esta configurado para instalar requirimientos de forma automatica
* Contex Mapper estara listo
