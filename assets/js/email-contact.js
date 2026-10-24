(() => {
  const link = document.querySelector('#profile .network-icon a[href^="mailto:"]');
  if (!link) return;

  const icon = link.querySelector('svg');
  if (!icon) return;

  const mailto = link.getAttribute('href');
  const address = decodeURIComponent(mailto.slice(7).split('?')[0]);
  const socialLinks = link.closest('.network-icon');
  const trigger = document.createElement('button');
  trigger.type = 'button';
  trigger.className = 'email-contact-toggle';
  trigger.setAttribute('aria-label', 'Show email address');
  trigger.setAttribute('aria-expanded', 'false');
  trigger.setAttribute('aria-controls', 'profile-email-contact');
  trigger.title = 'Show email address';
  const buttonIcon = icon.cloneNode(true);
  buttonIcon.setAttribute('aria-hidden', 'true');
  buttonIcon.setAttribute('focusable', 'false');
  trigger.append(buttonIcon);

  const panel = document.createElement('div');
  panel.id = 'profile-email-contact';
  panel.className = 'email-contact';
  panel.hidden = true;
  panel.setAttribute('role', 'region');
  panel.setAttribute('aria-label', 'Email contact');
  panel.innerHTML = `
    <p class="email-contact-address"></p>
    <div class="email-contact-actions">
      <button class="email-contact-copy" type="button">Copy email</button>
      <a class="email-contact-open">Open email app</a>
    </div>
    <p class="email-contact-status" role="status" aria-live="polite" aria-atomic="true"></p>
  `;
  panel.querySelector('.email-contact-address').textContent = address;
  panel.querySelector('.email-contact-open').href = mailto;
  const copyButton = panel.querySelector('.email-contact-copy');
  const status = panel.querySelector('.email-contact-status');

  function setOpen(open) {
    panel.hidden = !open;
    trigger.setAttribute('aria-expanded', String(open));
    const label = open ? 'Hide email address' : 'Show email address';
    trigger.setAttribute('aria-label', label);
    trigger.title = label;
    copyButton.textContent = 'Copy email';
    status.textContent = '';
  }

  trigger.addEventListener('click', () => setOpen(panel.hidden));

  function closeOnEscape(event) {
    if (event.key === 'Escape' && !panel.hidden) {
      event.preventDefault();
      setOpen(false);
      trigger.focus();
    }
  }
  trigger.addEventListener('keydown', closeOnEscape);
  panel.addEventListener('keydown', closeOnEscape);

  copyButton.addEventListener('click', async () => {
    copyButton.disabled = true;
    status.textContent = '';
    try {
      await navigator.clipboard.writeText(address);
      copyButton.textContent = 'Copied!';
      status.textContent = 'Email address copied.';
    } catch {
      status.textContent = 'Copy unavailable. Select the address above to copy it manually.';
    } finally {
      copyButton.disabled = false;
    }
  });

  socialLinks.after(panel);
  link.replaceWith(trigger);
})();
