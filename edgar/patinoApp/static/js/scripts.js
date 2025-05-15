document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('a.button, button');

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      alert('¡Botón presionado!');
    });
  });
});
