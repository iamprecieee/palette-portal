document.addEventListener('DOMContentLoaded', function() {
    const img = document.getElementById('artwork-image');
    const name = document.getElementById('price-name');
    const price = document.getElementById('price');
    const colorThief = new ColorThief();

    // Helper function to calculate saturation
    function getSaturation(rgb) {
        const max = Math.max(rgb[0], rgb[1], rgb[2]);
        const min = Math.min(rgb[0], rgb[1], rgb[2]);
        return (max - min) / max;
    }
    
    // Helper function to calculate warmth (redness)
    function getWarmth(rgb) {
        return rgb[0] - Math.max(rgb[1], rgb[2]);
    }

    // Function to apply best color
    function applyBestColor(img) {
        const palette = colorThief.getPalette(img, 10);
        let bestColor = palette[0];
        let maxScore = getSaturation(palette[0]) + getWarmth(palette[0]);

        for (let i = 1; i < palette.length; i++) {
            const score = getSaturation(palette[i]) + getWarmth(palette[i]);
            if (score > maxScore) {
                maxScore = score;
                bestColor = palette[i];
            }
        }

        name.style.color = `rgb(${bestColor[0]}, ${bestColor[1]}, ${bestColor[2]})`;
        price.style.color = `rgb(${bestColor[0]}, ${bestColor[1]}, ${bestColor[2]})`;
    }

    // Ensure image is loaded before extracting color
    if (img.complete) {
        applyBestColor(img);
    } else {
        img.addEventListener('load', function() {
            applyBestColor(img);
        });
    }


    $(document).ready(function() {
        $('.form-select select').each(function(index) {
            $(this).attr('id', 'select-' + index).select2({
                minimumResultsForSearch: Infinity, // Disable search box
                width: 'auto'
            });
        });
    });
});
