// Keep the archive at hand on desktop and out of the way on smaller screens.
const timeline = document.querySelector('.post-timeline');
const narrow = window.matchMedia('(max-width: 900px)');
const setTimelineLayout = () => { timeline.open = !narrow.matches; };
setTimelineLayout();
narrow.addEventListener('change', setTimelineLayout);
