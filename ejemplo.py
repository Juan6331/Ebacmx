a=10
b=20
c=30*a*b
print('Resultado=',c)
d=c*100
print('resultado final0',d)
'''Generar un directorio local para que sea el repositorio espejo
En VS Code ir a la línea de navegación de comando (SHIFT-CMD-P)
Hacer login en GitHub (desde el ícono de cuenta en la esquina izquierda inferior): Sign In with GitHub. Validar que el usuario se encuentre activo.
Clonado de Repositorio desde Github en VS Code
"Git: Clone" - escoger "Clone from GitHub", si está conectado, aparecerán los distintos Repositorios de tu GitHub ahí
Se Luego de escoger el archivo local de "espejo", se conectarán ambos repositorios. Se puede ver como el directorio local tiene ahora el archivo README
puede esperar a que VS Code obtenga la lista de GitHub, o se puede poner directamente el repositorio: https://github.com/GuzVinueza/testebac2
Importante:La selección del directorio es del raíz, no es necesario generar un directorio con el mismo nombre
Generar un archivo nuevo local y replicarlo en Github
De los pasos más necesarios. Se genera un archivo test.py localmente, que luego se replica a Github
Se construye el archivo y se lo guarda en el folder seleccionado del repositorio
Se debe tener en cuenta que el folder abierto para VS Code debe ser el folder del repositorio
Luego de eso, se hace un "Git Commit" - se ingresa los comentarios de la subida (p.ej. primera versión, integración 0.1, etc.)
Finalmente se hace un "Git Push"
Se verifica en ambos repositorios que esté el archivo con la última versión
Sincronizar cambios desde Github al repositorio local
En Github, directamente, se hacen cambios al archivo y se guardan
Desde VS Code, se hace un "Git Pull" y automáticamente se ven los cambios en el archivo
Se puede hacer una vez más, para repetirlo'''
