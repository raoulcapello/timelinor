let height = '0px';
let previousHeight = '0px';

document.querySelectorAll('.timeline').forEach((element, index) => {
  console.log('Element', index);

  previousHeight = height;

  // Skip the first timeline block
  if (index > 0) {
    let currentHeightDigits = parseInt(
      getComputedStyle(element)['height'].slice(0, -2)
    );
    let heightDigits = parseInt(previousHeight.slice(0, -2));

    if (heightDigits > currentHeightDigits) {
      // Set height to previous blocks height
      element.style.height = height;

      console.log('height set to:', height);
    }
  }

  height = getComputedStyle(element)['height'];

  console.log('height is:', height);
});
