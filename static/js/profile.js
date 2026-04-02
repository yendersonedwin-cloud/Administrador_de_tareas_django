function showSuccess(e) {
  // Evitamos que recargue mientras solo probamos diseño
  e.preventDefault(); 
  
  const msg = document.getElementById('successMsg');
  msg.style.display = 'block';
  
  setTimeout(() => {
    msg.style.display = 'none';
  }, 3000);
}

function confirmLogout() {
  if (confirm('¿Estás seguro de que quieres cerrar sesión?')) {
    alert("Cerrando sesión...");
    // window.location.href = "/logout/"; // Ruta de Django
  }
}

// Cerrar modal de password al hacer clic fuera
const modalPw = document.getElementById('modalPw');
if(modalPw) {
    modalPw.addEventListener('click', function(e) {
      if (e.target === this) this.classList.add('hidden');
    });
}