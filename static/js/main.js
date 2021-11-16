const btnDelete = document.querySelectorAll('.btn-delete')

//Selecciono todos los items, los recorro y por cada evento popea un mensaje
//esperando la confirmacion del usuario para realizar la accion y si no la obtiene
//elimina la peticion al servidor
if(btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e => {
            if(!confirm('¿Estas seguro de querer eliminar este articulo?')) {
                e.preventDefault();
            }
        }))
    }
    )
}