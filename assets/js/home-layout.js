// Start the avatar halfway across the banner edge, then keep it visible on scroll.
(() => {
  if (!document.querySelector('.profile-sidebar')) return;

  let scheduled = false;
  function updateScrollPosition() {
    document.documentElement.style.setProperty('--home-scroll', `${Math.max(window.scrollY, 0)}px`);
    scheduled = false;
  }
  function scheduleUpdate() {
    if (scheduled) return;
    scheduled = true;
    window.requestAnimationFrame(updateScrollPosition);
  }

  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('pageshow', scheduleUpdate);
  updateScrollPosition();
})();
