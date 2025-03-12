---
layout: page
title: Meetings
permalink: /meetings/
order: 3
---
### Telecons

Telecons are held approximately every two weeks on Mondays at 09:00 AM Mountain time, but this can fluctuate depending on holidays/conferences/etc. See the calendar below for the next telecon time. Telecon notes are shared on [Google Drive](https://drive.google.com/drive/u/0/folders/1AhFUli3SGW9DHvIh81tFxPMgLtYSPXDm), and presentations can be found on the [PyHC YouTube Channel](https://www.youtube.com/@pythoninheliophysicscommun3732).

<br>

### Events

#### [Community Meetings]({% link
_pages/meetings/community_meetings/community_meetings.md %})

#### [Conference Sessions]({% link
_pages/meetings/conference_sessions/conference_sessions.md %})

#### [Summer Schools]({% link
_pages/meetings/summer_schools/summer_schools.md %})

<br>

### Calendars

PyHC meetings and telecon times are available as a [Google calendar](https://calendar.google.com/calendar?cid=NG42Z3YyaWZncDZyZ25rOGF1N2pzZjF1azBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ):
<br>
<div id="pyhccalendar-container"></div>
<br>

Additionally, there is a more [general calendar](https://helioanalytics.io/events-calendar) that serves as an exhaustive list of events related to the Heliophysics and space physics communities. If you have an event you'd like added to this calendar, please email: <a href="mailto:pyhc-confidential@lasp.colorado.edu">pyhc-confidential@lasp.colorado.edu</a>
<br><br>

<div id="helioanalyticscalendar-container"></div>

<script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function() {
        // Initial setup with a slight delay to ensure all elements are loaded
        setTimeout(setupGoogleCalendars, 500);
        
        // Set up a MutationObserver to detect theme attribute changes
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'data-theme') {
                    setupGoogleCalendars();
                }
            });
        });
        
        // Start observing document for data-theme attribute changes
        observer.observe(document.documentElement, { 
            attributes: true,
            attributeFilter: ['data-theme'] 
        });
    });

    function setupGoogleCalendars() {
        const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        
        // Create calendar iframes
        const pyhcContainer = document.getElementById('pyhccalendar-container');
        const helioContainer = document.getElementById('helioanalyticscalendar-container');
        
        // Clear existing content
        pyhcContainer.innerHTML = '';
        helioContainer.innerHTML = '';
        
        // Create PyHC calendar iframe with dark mode support
        createCalendarIframe(
            pyhcContainer, 
            'https://calendar.google.com/calendar/embed',
            {
                height: '600',
                wkst: '1',
                bgcolor: isDark ? '%23121212' : '%23f9e79f',
                showTitle: '0',
                showDate: '1',
                showPrint: '0',
                showTabs: '1',
                showCalendars: '0',
                showNav: '1',
                src: 'NG42Z3YyaWZncDZyZ25rOGF1N2pzZjF1azBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ',
                color: '%237CB342',
                ctz: timezone
            }
        );
        
        // Create Helioanalytics calendar iframe with dark mode support
        createCalendarIframe(
            helioContainer,
            'https://calendar.google.com/calendar/embed',
            {
                height: '600',
                wkst: '1',
                bgcolor: isDark ? '%23121212' : '%23ffffff',
                src: 'aWJwbWhrMTFlMWEyMTFpa3V0bGY1M2d0ZnNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ',
                color: '%23D50000',
                ctz: timezone
            }
        );
    }
    
    function createCalendarIframe(container, baseUrl, params) {
        const iframe = document.createElement('iframe');
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        
        // Build URL with parameters
        let url = baseUrl + '?';
        for (const [key, value] of Object.entries(params)) {
            url += `${key}=${value}&`;
        }
        
        iframe.src = url;
        iframe.width = '100%';
        iframe.height = '600';
        iframe.frameBorder = '0';
        iframe.scrolling = 'no';
        iframe.style.border = 'none';
        iframe.style.transition = 'filter 0.3s ease';
        
        // Apply styles for dark mode
        if (isDark) {
            iframe.style.filter = 'hue-rotate(180deg) invert(92%) contrast(90%)';
        }
        
        // Add the iframe to the container
        container.appendChild(iframe);
        
        // Add event listeners to modify the iframe content once it's loaded
        iframe.onload = function() {
            if (isDark) {
                try {
                    // Access the iframe content and add CSS to force dark mode
                    const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
                    
                    if (iframeDocument) {
                        // Create a style element
                        const style = iframeDocument.createElement('style');
                        style.textContent = `
                            body, .view-container, .view-cap-container, .mv-container {
                                background-color: #121212 !important;
                                color: #e0e0e0 !important;
                            }
                            .view-container-border {
                                background-color: #333 !important;
                            }
                            .cal-header { 
                                background-color: #121212 !important;
                                color: #e0e0e0 !important;
                            }
                        `;
                        iframeDocument.head.appendChild(style);
                    }
                } catch (e) {
                    console.warn('Could not inject styles into iframe due to Same-Origin Policy', e);
                }
            }
        };
    }
</script>
