(function() {
    'use strict';

    // Create a button element
    var copyButton = document.createElement('button');
    copyButton.innerHTML = 'Copy Href Attributes Starting with /p/ and /reel/';
    copyButton.style.position = 'fixed';
    copyButton.style.top = '10px';
    copyButton.style.right = '10px';
    copyButton.style.zIndex = '9999';

    // Append the button to the body of the document
    document.body.appendChild(copyButton);

    // Add click event listener to the button
    copyButton.addEventListener('click', function() {
        // Find all anchor elements on the page with href attributes starting with /p/ or /reel/
        var filteredAnchorElements = document.querySelectorAll('a[href^="/p/"], a[href^="/reel/"]');

        // Check if any matching anchor elements are found
        if (filteredAnchorElements.length > 0) {
            // Extract and concatenate href attributes with single quotes and commas
            var extractedHrefs = Array.from(filteredAnchorElements).map(function(element) {
                var hrefValue = element.getAttribute('href');
                return "'" + hrefValue + "',";
            }).join('\n');

            // Copy the extracted href attributes to the clipboard using the Clipboard API
            navigator.clipboard.writeText(extractedHrefs)
                .then(function() {
                    // Alert the user that the href attributes have been copied (you can customize this part)
                    alert('Href attributes starting with /p/ and /reel/ copied to clipboard:\n' + extractedHrefs);
                })
                .catch(function(err) {
                    console.error('Unable to copy to clipboard', err);
                });
        } else {
            // Alert the user if no matching anchor elements are found
            alert('No anchor elements with href attributes starting with /p/ or /reel/ found on this page.');
        }
    });
})();
