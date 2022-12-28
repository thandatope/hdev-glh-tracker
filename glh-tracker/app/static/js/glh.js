

document.addEventListener('DOMContentLoaded', () => {
   // Functions to open and close a modal
   function openModal($el, id, name, date, duration) {
      $el.classList.add('is-active');
      modalId = $el.querySelector('#record-id');
      modalName = $el.querySelector('#session-name')
      modalDate = $el.querySelector('#session-date')
      modalDuration = $el.querySelector('#session-duration')
      modalId.value = id;
      modalName.value = name;
      modalDate.value = date;
      modalDuration.value = duration;
   }

   function closeModal($el) {
      $el.classList.remove('is-active');
   }

   function closeAllModals() {
      (document.querySelectorAll('.modal') || []).forEach(($modal) => {
         closeModal($modal);
      });
   }

   // Add a click event on buttons to open a specific modal
   (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
      const modal = $trigger.dataset.target;
      const id = $trigger.dataset.id;
      const name = $trigger.dataset.name;
      const date = $trigger.dataset.date;
      const duration = $trigger.dataset.duration;
      const $target = document.getElementById(modal);

      $trigger.addEventListener('click', () => {
         openModal($target, id, name, date, duration);
      });
   });
   // Add a click event on various child elements to close the parent modal
   (document.querySelectorAll('.delete, .button') || []).forEach(($close) => {
      const $target = $close.closest('.modal');

      $close.addEventListener('click', () => {
         closeModal($target);
      });
   });

   // Add a keyboard event to close all modals
   document.addEventListener('keydown', (event) => {
      const e = event || window.event;

      if (e.keyCode === 27) { // Escape key
         closeAllModals();
      }
   });
});
