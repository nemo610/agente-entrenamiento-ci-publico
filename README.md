# Agente de entrenamiento — CI público seguro

Este repositorio contiene pruebas públicas aisladas y un ejecutor estándar de GitHub Actions gratuito que puede ejecutar, de forma programada o manual, la investigación **paper-only** del repositorio privado.

## Qué hace

- Ejecuta pruebas Python del repositorio privado `nemo610/agente-entrenamiento-python`.
- Vuelve a calcular el estudio histórico multiestrategia y actualiza el registro prospectivo de paper trading.
- Devuelve al repositorio privado únicamente el estado prospectivo, el último informe forward y un resumen pequeño de candidatos.
- No publica el código privado, el informe histórico completo, los resultados privados ni archivos como artefactos públicos.
- No envía órdenes reales ni órdenes a Binance.
- No cambia automáticamente parámetros de estrategia ni implica que el agente haya demostrado rentabilidad.

## Configuración única necesaria

GitHub no permite que el token automático de este repositorio lea otro repositorio privado. Por eso hace falta un token de acceso de alcance limitado. **No lo pegues en un chat, archivo ni código.**

1. En GitHub, crea un **Fine-grained personal access token** desde Settings → Developer settings → Personal access tokens → Fine-grained tokens.
2. Limita **Repository access** únicamente a `nemo610/agente-entrenamiento-python`.
3. Concede solo el permiso de repositorio **Contents: Read and write**. Define una fecha de expiración y guarda el token de forma segura.
4. En este repositorio público, abre Settings → Secrets and variables → Actions → New repository secret.
5. Nombre exacto: `GH_PRIVATE_REPO_TOKEN`. Pega el token como valor y guarda.
6. Abre Actions → **Private Agent Paper Training (Free Public Runner)** → Run workflow.

El flujo no se ejecuta en eventos de pull request. Solo corre por horario o por lanzamiento manual, para no entregar el secreto a código de contribuyentes externos. Si el token expira o no tiene el alcance requerido, el flujo fallará hasta renovar el secreto.

## Ejecución programada

La investigación paper se programa diariamente a las 00:17 UTC. También se puede iniciar manualmente desde Actions.

## Límite importante: Binance Spot Testnet

El ejecutor gratuito sirve para pruebas y simulaciones históricas, pero **no resuelve por sí mismo el bloqueo geográfico de Binance Testnet**. En una prueba anterior, Binance respondió HTTP 451 desde el entorno alojado de GitHub. Este flujo no intenta enviar órdenes ni presenta la conectividad Testnet como verificada. Esa parte debe validarse desde un entorno permitido por Binance.

## Seguridad e interpretación

Este repositorio no contiene el código privado del agente. No agregues eventos `pull_request` ni ejecutes código de pull requests en el flujo que usa `GH_PRIVATE_REPO_TOKEN`. Los informes y el estado persistente se escriben únicamente en el repositorio privado.

Los resultados históricos son exploratorios y no certifican rentabilidad futura ni autorizan operar con dinero real.
