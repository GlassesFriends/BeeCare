function WorkerLogOut(url) {
    Swal.fire({
        title: '¿Deseas cerrar sesión?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#e74a3b',
        cancelButtonColor: '#4e73df',
        confirmButtonText: 'Cerrar sesión',
        cancelButtonText: 'Cancelar',
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = url
        }
    })
}