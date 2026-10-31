# Agente de entrenamiento — CI público seguro

Este repositorio contiene una **capa pública y aislada de integración continua** para verificar que las pruebas automatizadas se ejecutan en GitHub Actions.

## Alcance

- Ejecuta pruebas locales y deterministas con Python.
- No se conecta a Binance ni a ningún exchange.
- No contiene claves, secretos, saldos, órdenes ni archivos de estado del proyecto privado.
- No ejecuta operaciones reales ni simuladas contra servicios externos.
- No reemplaza las pruebas completas del repositorio privado.

## Ejecución automática

GitHub Actions ejecuta la suite al hacer push, abrir o actualizar una solicitud de cambios y manualmente desde la pestaña **Actions**.

## Ejecutar las pruebas localmente

```bash
python -m pip install -e ".[test]"
python -m pytest -q
```

## Estado

Este repositorio es una base de automatización pública. Los resultados aquí **no deben interpretarse como certificación de rentabilidad, seguridad de una estrategia ni autorización para operar con capital real**.
