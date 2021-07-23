// Hide ugly input file button and replace it with a better looking
// label (masking as a button) and a span (displaying file status)
const actualBtn = document.getElementById('upload-profilepic-btn'); // Hidden
const fileChosen = document.getElementById('file-chosen'); // Span showing file status

actualBtn.addEventListener('change', function () {
  // On button change, update file status in span
  fileChosen.textContent = this.files[0].name;
});
