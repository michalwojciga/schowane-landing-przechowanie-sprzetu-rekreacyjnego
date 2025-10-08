const LANDING_EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const LANDING_EVENT_ENDPOINT = '/landing/events';

const trackLandingEvent = (name, detail = {}) => {
  if (!name) {
    return;
  }

  const payload = JSON.stringify({
    event: name,
    detail,
    ts: new Date().toISOString(),
  });

  if (navigator.sendBeacon) {
    try {
      const blob = new Blob([payload], { type: 'application/json' });
      navigator.sendBeacon(LANDING_EVENT_ENDPOINT, blob);
      return;
    } catch (error) {
      // eslint-disable-next-line no-console
      console.debug('Beacon tracking failed, falling back to fetch.', error);
    }
  }

  if (window.fetch) {
    fetch(LANDING_EVENT_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: payload,
      keepalive: true,
    }).catch(() => {
      // eslint-disable-next-line no-console
      console.debug('Landing event tracking fetch failed.');
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const newsletterForm = document.querySelector('[data-landing-newsletter-form]');
  const trackableElements = document.querySelectorAll('[data-landing-track]');

  trackableElements.forEach((element) => {
    element.addEventListener('click', (event) => {
      const { landingTrack, landingTrackMeta } = event.currentTarget.dataset;
      trackLandingEvent(landingTrack, landingTrackMeta ? { meta: landingTrackMeta } : {});
    });
  });

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
      trackLandingEvent('newsletter-subscribe');
    });
  }

  // eslint-disable-next-line no-console
  console.debug('Landing page assets loaded.');
});
