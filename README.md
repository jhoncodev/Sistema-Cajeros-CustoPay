# Sistema de Cajeros Multifuncionales CustoPay 🏧

> **Proyecto Académico** - Desarrollado para el curso de Análisis de Algoritmos y Estrategias de Programación

Sistema bancario simulado por consola que implementa una red de cajeros automáticos con gestión administrativa completa. Este proyecto demuestra la aplicación práctica de algoritmos fundamentales y programación orientada a objetos.

## ⚠️ Nota Importante
Este es un **proyecto académico con fines educativos**. No está diseñado para uso en producción y solo funciona mediante interfaz de consola.

## 🎯 Objetivo Académico

Implementar y demostrar el dominio de:
- **Algoritmos de ordenamiento** (QuickSort)
- **Algoritmos de búsqueda** (Búsqueda binaria)
- **Programación orientada a objetos** (Herencia, encapsulamiento)
- **Estructuras de datos complejas**
- **Validación y manejo de excepciones**

## 📋 Funcionalidades Implementadas

### Para Administradores
- ✅ Registro y autenticación de administradores
- ✅ Gestión completa de clientes (CRUD)
- ✅ Control de estados de cuenta (activo/inactivo)
- ✅ Administración de cajeros por regiones
- ✅ Cambio de estados de cajeros (activo/mantenimiento)

### Para Clientes
- ✅ Registro y autenticación de clientes
- ✅ Depósitos con desglose de billetes
- ✅ Retiros con cálculo automático de billetes
- ✅ Transferencias entre cuentas
- ✅ Pago de servicios básicos
- ✅ Consulta de saldos y movimientos

## 🧮 Algoritmos Implementados

### QuickSort
```python
def quickSort(listaDesordenada, campo):
    # Implementación recursiva para ordenar usuarios/cajeros
    # Complejidad: O(n log n) promedio, O(n²) peor caso
```

### Búsqueda Binaria
```python
def busquedaBinaria(lista, campo, valor):
    # Búsqueda eficiente en listas ordenadas
    # Complejidad: O(log n)
```

### Algoritmo de Desglose de Billetes
```python
def desgloseBilletesDinamico(monto, denominaciones, billetesDisponibles):
    # Distribución óptima de billetes para retiros
    # Enfoque greedy para minimizar cantidad de billetes
```

## 🏗️ Arquitectura del Código

```
├── 📁 Clases Base
│   ├── Usuario (clase padre)
│   ├── Administrador (hereda de Usuario)
│   └── Cliente (hereda de Usuario)
├── 📁 Clases de Negocio
│   ├── Cuenta
│   ├── Movimiento
│   └── Cajero
├── 📁 Módulos Funcionales
│   ├── Gestión de usuarios
│   ├── Operaciones bancarias
│   └── Administración de cajeros
└── 📁 Algoritmos
    ├── QuickSort
    ├── Búsqueda binaria
    └── Desglose de billetes
```

## 🌍 Regiones Simuladas

El sistema simula cajeros en 6 regiones del Perú:
- Cajamarca
- Lima  
- Loreto
- Cuzco
- Tacna
- Piura

## 💡 Conceptos Técnicos Aplicados

### Programación Orientada a Objetos
- **Herencia**: `Administrador` y `Cliente` heredan de `Usuario`
- **Encapsulamiento**: Métodos y atributos organizados lógicamente
- **Composición**: `Cliente` contiene una instancia de `Cuenta`

### Algoritmos y Estructuras de Datos
- **Listas dinámicas** para almacenar usuarios y cajeros
- **Ordenamiento eficiente** con QuickSort personalizado
- **Búsqueda optimizada** con implementación propia de búsqueda binaria
- **Algoritmo greedy** para distribución de billetes

### Validaciones y Manejo de Errores
- Validación exhaustiva de entradas del usuario
- Manejo de excepciones con `try-catch`
- Control de estados y permisos

## 📊 Complejidad Algorítmica

| Operación | Algoritmo | Complejidad |
|-----------|-----------|-------------|
| Ordenar usuarios | QuickSort | O(n log n) |
| Buscar usuario | Búsqueda binaria | O(log n) |
| Desglose billetes | Greedy | O(n) |

## 🎓 Aprendizajes Obtenidos

- Implementación práctica de algoritmos fundamentales
- Diseño de sistemas con múltiples actores (admin/cliente)
- Gestión de estados y validaciones complejas
- Aplicación de principios SOLID en Python
- Simulación de sistemas del mundo real

## 📝 Limitaciones (Por Diseño Académico)

- Solo funciona por consola (no GUI)
- Datos se pierden al cerrar el programa (no persistencia)
- No incluye conexión a base de datos
- No implementa seguridad real (solo simulada)
- Sin manejo de concurrencia
