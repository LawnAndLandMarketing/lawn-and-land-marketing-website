// Lawn & Land Marketing v38 — Mega Menu + Premium Footer

// ─ CURSOR GLOW ─
const glow = document.getElementById('cursorGlow');
if (glow && window.matchMedia('(pointer:fine)').matches) {
  document.addEventListener('mousemove', e => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
  });
} else if (glow) { glow.style.display = 'none'; }

// ─ SCROLL REVEAL ─
const revealEls = document.querySelectorAll('[data-reveal]');
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      const delay = e.target.dataset.delay || 0;
      setTimeout(() => e.target.classList.add('revealed'), parseInt(delay));
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
revealEls.forEach(el => revealObs.observe(el));

// ─ COUNTER ANIMATION ─
function animateCount(el) {
  const target = parseInt(el.dataset.count);
  const prefix = el.dataset.prefix || '';
  const suffix = el.dataset.suffix || '';
  const duration = 1800;
  const start = performance.now();
  const update = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(ease * target);
    el.textContent = prefix + current + suffix;
    if (progress < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}
const counterObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting && e.target.dataset.count) {
      animateCount(e.target);
      counterObs.unobserve(e.target);
    }
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-count]').forEach(el => counterObs.observe(el));

// ─ WORD CYCLE (hero) — slide up/down transition ─
const cycleEl = document.getElementById('heroCycle');
if (cycleEl) {
  const words = ['Landscaping Companies.', 'Lawn Care Businesses.', 'The Green Industry.'];
  let idx = 0;

  // Set initial transition
  cycleEl.style.transition = 'opacity 0.45s ease, transform 0.45s ease';

  setInterval(() => {
    // Slide out current word upward
    cycleEl.style.opacity = '0';
    cycleEl.style.transform = 'translateY(-18px)';

    setTimeout(() => {
      // Swap word, reset below (no transition)
      cycleEl.style.transition = 'none';
      cycleEl.style.transform = 'translateY(18px)';
      idx = (idx + 1) % words.length;
      cycleEl.textContent = words[idx];

      // Force reflow, then slide in
      void cycleEl.offsetHeight;
      cycleEl.style.transition = 'opacity 0.45s ease, transform 0.45s ease';
      cycleEl.style.opacity = '1';
      cycleEl.style.transform = 'translateY(0)';
    }, 420);
  }, 3400);
}

// ─ VIDEO FACADE ─
const videoFacade = document.getElementById('videoFacade');
const heroIframe  = document.getElementById('heroIframe');
if (videoFacade && heroIframe) {
  videoFacade.addEventListener('click', () => {
    heroIframe.src += '&autoplay=1';
    heroIframe.closest('.hero-video-wrap').classList.add('playing');
  });
}

// ─ MOBILE NAV ─
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
if (navToggle && navMenu) {
  navToggle.addEventListener('click', () => {
    const open = navMenu.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', open);
    navToggle.querySelectorAll('span')[0].style.transform = open ? 'rotate(45deg) translate(5px, 5px)' : '';
    navToggle.querySelectorAll('span')[1].style.opacity = open ? '0' : '1';
    navToggle.querySelectorAll('span')[2].style.transform = open ? 'rotate(-45deg) translate(5px,-5px)' : '';
  });
}

// ─ MEGA MENU — mobile click toggles ─
document.querySelectorAll('.nav-item.nav-mega > .nav-link').forEach(btn => {
  btn.addEventListener('click', () => {
    if (window.innerWidth <= 768) {
      const item = btn.closest('.nav-item');
      // Close others
      document.querySelectorAll('.nav-item.nav-mega').forEach(i => {
        if (i !== item) i.classList.remove('open');
      });
      item.classList.toggle('open');
    }
  });
});

// Close mega panels on outside click
document.addEventListener('click', e => {
  if (!e.target.closest('.nav-mega')) {
    document.querySelectorAll('.nav-item.nav-mega').forEach(i => i.classList.remove('open'));
  }
});

// Legacy dropdown toggles (non-mega)
document.querySelectorAll('.nav-item.nav-dropdown > .nav-link').forEach(btn => {
  btn.addEventListener('click', () => {
    if (window.innerWidth <= 768) {
      btn.closest('.nav-item').classList.toggle('open');
    }
  });
});

// ─ SERVICES TABS ─
const tabs = document.querySelectorAll('.svc-tab');
const panels = document.querySelectorAll('.svc-panel');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    panels.forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    const target = document.querySelector(`.svc-panel[data-panel="${tab.dataset.tab}"]`);
    if (target) target.classList.add('active');
  });
});

// ─ FAQ ACCORDION ─
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
      const a = i.querySelector('.faq-a');
      if (a) a.hidden = true;
    });
    if (!isOpen) {
      item.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
      const a = item.querySelector('.faq-a');
      if (a) a.hidden = false;
    }
  });
});

// Testimonial video click-to-play
document.querySelectorAll('.testi-video-wrap').forEach(wrap => {
  wrap.addEventListener('click', () => {
    const videoId = wrap.dataset.videoid;
    if (!videoId || wrap.classList.contains('playing')) return;
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`;
    iframe.allow = 'autoplay; encrypted-media';
    iframe.allowFullscreen = true;
    wrap.appendChild(iframe);
    wrap.classList.add('playing');
  });
});
