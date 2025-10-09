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
  const heroCarousel = document.querySelector('[data-landing-hero-carousel]');

  trackableElements.forEach((element) => {
    element.addEventListener('click', (event) => {
      const { landingTrack, landingTrackMeta } = event.currentTarget.dataset;
      trackLandingEvent(landingTrack, landingTrackMeta ? { meta: landingTrackMeta } : {});
    });
  });

  if (heroCarousel) {
    const track = heroCarousel.querySelector('.landing-hero-carousel-track');
    const slides = Array.from(heroCarousel.querySelectorAll('[data-landing-hero-slide]'));
    const prevButton = heroCarousel.querySelector('[data-landing-hero-prev]');
    const nextButton = heroCarousel.querySelector('[data-landing-hero-next]');
    const dotsContainer = heroCarousel.querySelector('[data-landing-hero-dots]');
    const AUTOPLAY_INTERVAL = 8000;
    let autoplayTimer = null;
    let currentIndex = 0;

    const goTo = (index) => {
      if (!track || slides.length === 0) {
        return;
      }

      currentIndex = (index + slides.length) % slides.length;

      track.style.transform = `translateX(-${currentIndex * 100}%)`;

      slides.forEach((slide, slideIndex) => {
        const isActive = slideIndex === currentIndex;
        slide.classList.toggle('is-active', isActive);
        slide.setAttribute('aria-hidden', isActive ? 'false' : 'true');
      });

      if (dotsContainer) {
        dotsContainer.querySelectorAll('.landing-hero-carousel-dot').forEach((dot, dotIndex) => {
          const isActive = dotIndex === currentIndex;
          dot.classList.toggle('is-active', isActive);
          dot.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        });
      }
    };

    const stopAutoplay = () => {
      if (autoplayTimer) {
        window.clearInterval(autoplayTimer);
        autoplayTimer = null;
      }
    };

    const startAutoplay = () => {
      stopAutoplay();

      if (slides.length <= 1) {
        return;
      }

      autoplayTimer = window.setInterval(() => {
        goTo(currentIndex + 1);
      }, AUTOPLAY_INTERVAL);
    };

    if (dotsContainer) {
      slides.forEach((_, slideIndex) => {
        const dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'landing-hero-carousel-dot';
        dot.setAttribute('aria-label', `Slajd ${slideIndex + 1} z ${slides.length}`);
        dot.setAttribute('aria-pressed', slideIndex === 0 ? 'true' : 'false');
        dot.addEventListener('click', () => {
          goTo(slideIndex);
          startAutoplay();
        });
        dotsContainer.append(dot);
      });
    }

    if (prevButton) {
      prevButton.addEventListener('click', () => {
        goTo(currentIndex - 1);
        startAutoplay();
      });
    }

    if (nextButton) {
      nextButton.addEventListener('click', () => {
        goTo(currentIndex + 1);
        startAutoplay();
      });
    }

    heroCarousel.addEventListener('mouseenter', stopAutoplay);
    heroCarousel.addEventListener('mouseleave', startAutoplay);
    heroCarousel.addEventListener('focusin', stopAutoplay);
    heroCarousel.addEventListener('focusout', startAutoplay);

    goTo(0);
    startAutoplay();
  }

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
