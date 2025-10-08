// Placeholder for future landing page interactions.
// Example: smooth scrolling, FAQ accordion toggles, telemetry hooks.
const LANDING_EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

document.addEventListener('DOMContentLoaded', () => {
  const newsletterForm = document.querySelector('[data-landing-newsletter-form]');

  if (newsletterForm) {
    const emailInput = newsletterForm.querySelector('input[type="email"]');
    const message = newsletterForm.querySelector('[data-landing-newsletter-message]');

    const setMessage = (text, variant) => {
      if (!message) {
        return;
      }

      message.textContent = text;
      message.classList.remove('is-error', 'is-success');

      if (variant) {
        message.classList.add(variant);
      }
    };

    const markInvalid = (text) => {
      if (!emailInput) {
        return;
      }

      emailInput.setAttribute('aria-invalid', 'true');
      setMessage(text, 'is-error');
      emailInput.focus();
    };

    if (emailInput) {
      emailInput.addEventListener('input', () => {
        emailInput.removeAttribute('aria-invalid');
        setMessage('', null);
      });
    }

    newsletterForm.addEventListener('submit', (event) => {
      event.preventDefault();

      if (!emailInput) {
        return;
      }

      const emailValue = emailInput.value.trim();

      if (!emailValue) {
        markInvalid('Podaj adres e-mail.');
        return;
      }

      if (!LANDING_EMAIL_REGEX.test(emailValue)) {
        markInvalid('Wpisz poprawny adres e-mail (np. imie@domena.pl).');
        return;
      }

      emailInput.removeAttribute('aria-invalid');
      setMessage('Dziękujemy! Potwierdź zapis w wiadomości, którą właśnie wysłaliśmy.', 'is-success');
      newsletterForm.reset();
      emailInput.blur();
    });
  }

  // eslint-disable-next-line no-console
  console.debug('Landing page assets loaded.');
});
