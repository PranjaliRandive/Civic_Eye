function showSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
    // Show clicked section
    document.getElementById(sectionId).classList.add('active');
  }