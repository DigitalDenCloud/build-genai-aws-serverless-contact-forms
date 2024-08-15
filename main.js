		// Contact form handling
            var $contact = $('#contact');
            var $form = $contact.find('form');
            var $submit = $form.find('input[type="submit"]');

            $form.submit(function(event) {
                event.preventDefault();

                // Disable submit button (using template's existing disabled class)
                $submit.addClass('disabled');

                // Send data asynchronously
                $.ajax({
                    url: "YOUR_API_ENDPOINT_HERE",
                    type: "POST",
                    data: JSON.stringify(Object.fromEntries(new FormData($form[0]))),
                    contentType: "application/json",
                    success: function(result) {
                        $form.find('.response').remove();
                        $form.append('<div class="response success">Message sent successfully!</div>');
                        $form[0].reset();

                        // Close the form after 3 seconds using template's hash navigation
                        setTimeout(function() {
                            location.hash = '';
                        }, 3000);
                    },
                    error: function(error) {
                        $form.find('.response').remove();
                        $form.append('<div class="response error">There was an error sending your message. Please try again.</div>');
                    },
                    complete: function() {
                        // Re-enable submit button
                        $submit.removeClass('disabled');
                    }
                });
            });