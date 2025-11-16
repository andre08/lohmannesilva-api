
// Função para envio de mensagem (alerta na pagina)
function exibirMensagem(mensagem){
  const alertaComponente = document.getElementById("alerta")
  const alertaMensagem = document.getElementById("alertaMensagem")
  alertaMensagem.innerHTML = mensagem;
  alertaComponente.classList.remove('d-none', 'fade-out');
  alertaComponente.classList.add('fade-in');

  // Fecha automaticamente
  setTimeout(() => {
    alertaComponente.classList.remove('fade-in');
    alertaComponente.classList.add('fade-out');

    // Espera o fim da animação antes de esconder
    setTimeout(() => {
      alertaComponente.classList.add('d-none');
    }, 500); // mesmo tempo da transição no CSS
  }, 4000);      

  // Impede o Bootstrap de remover o alerta do DOM
  alertaComponente.addEventListener('close.bs.alert', event => {
    event.preventDefault();
    alertaComponente.classList.add('d-none');
  });
}