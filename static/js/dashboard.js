let activeCard = null;

function openDetail(el) {
    activeCard = el;
    // Extraemos los datos de los data-attributes del HTML
    const id = el.getAttribute('data-id');
    const titulo = el.getAttribute('data-titulo');
    const desc = el.getAttribute('data-desc');

    document.getElementById('detailPanel').classList.remove('hidden');
    document.getElementById('detTitle').value = titulo;
    document.getElementById('detDesc').value = desc;

    // ESTO ES LO QUE FALTA: Conectar con las rutas de Django
    // Si tus rutas en urls.py cambian, estas también deben cambiar
    document.getElementById('editForm').action = "/editar/" + id + "/";
    document.getElementById('deleteForm').action = "/eliminar/" + id + "/";

    document.querySelectorAll('.task-card').forEach(c => c.style.borderColor = 'transparent');
    activeCard.style.borderColor = 'var(--teal)';
}

function closeDetail() {
    document.getElementById('detailPanel').classList.add('hidden');
    if (activeCard) activeCard.style.borderColor = 'transparent';
}

function submitDelete() {
    // 1. Obtener el título de la tarea activa para mostrarlo en el modal
    const currentTitle = document.getElementById('detTitle').value;
    document.getElementById('deleteTaskName').innerText = currentTitle;

    // 2. Mostrar el modal
    const modal = document.getElementById('customConfirmModal');
    modal.classList.remove('hidden');
    
    // Bloquear scroll de fondo
    document.body.style.overflow = 'hidden';

    // 3. Configurar el botón de confirmación
    document.getElementById('confirmDeleteBtn').onclick = function() {
        document.getElementById('deleteForm').submit();
    };
}

function closeCustomConfirm() {
    document.getElementById('customConfirmModal').classList.add('hidden');
    document.body.style.overflow = 'auto';
}